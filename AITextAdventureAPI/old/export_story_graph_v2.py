"""
export_story_graph_v2.py

A full narrative-engineering export suite.

Exports:
 - Mermaid swimlane flowchart
 - CSV nodes + edges (with grouping metadata)
 - JSON (nodes, edges, groups, summaries, validation)
 - Validation report (dangling tasks, missing NPCs, cycles, etc.)

Run:
    python -m tools.export_story_graph_v2
"""

from pathlib import Path
import csv
import json
from collections import defaultdict, deque
from game import constants as const

OUT = Path.cwd() / "story_export_v2"
OUT.mkdir(exist_ok=True)


# ------------------------------------------------------------
# GROUPING LOGIC
# ------------------------------------------------------------

def group_for_task(task_id: str) -> str:
    """
    Infer story arc grouping from task_id naming conventions.
    """
    parts = task_id.split("_")

    # main story
    if task_id.startswith("main_story"):
        return "main_story"

    # biome + size (primary, large, mid, small)
    if parts[0] in (
        "desert", "forest", "grassland", "mountains",
        "shallows", "snow", "swamp"
    ):
        if len(parts) >= 3:
            return f"{parts[0]}_{parts[1]}_{parts[2]}"
        elif len(parts) >= 2:
            return f"{parts[0]}_{parts[1]}"
        return parts[0]

    return "misc"


# ------------------------------------------------------------
# NODE + EDGE BUILDERS
# ------------------------------------------------------------

def build_nodes():
    nodes = {}

    # Tasks
    for t in const.TASKS:
        tid = t.get("task_id")
        nodes[tid] = {
            "id": tid,
            "type": "task",
            "label": f"{tid}\\n({t.get('type')})",
            "group": group_for_task(tid)
        }

    # NPCs
    for n in const.NPCS:
        nid = n.get("npc_id") or n.get("id")
        if nid:
            nodes[nid] = {
                "id": nid,
                "type": "npc",
                "label": f"NPC: {n.get('name')}",
                "group": "npc"
            }

    # Dungeons
    for d in getattr(const, "DUNGEON_SETTINGS", []):
        did = d.get("dungeon_id")
        if did:
            nodes[did] = {
                "id": did,
                "type": "dungeon",
                "label": f"Dungeon: {d.get('display_name')}",
                "group": "dungeon"
            }

    return nodes


def build_edges():
    edges = []
    for t in const.TASKS:
        tid = t.get("task_id")
        src_group = group_for_task(tid)

        for ev in t.get("task_complete_events", []) or []:
            et = ev.get("event_type")
            params = ev.get("params", {}) or {}

            def add(dst, label):
                edges.append({
                    "src": tid,
                    "dst": dst,
                    "label": label,
                    "src_group": src_group,
                    "dst_group": group_for_task(dst) if dst in node_groups else "npc_or_misc"
                })

            if et == "award_task":
                tgt = params.get("task_id")
                if tgt:
                    add(tgt, "award_task")

            elif et in ("create_npc", "initiate_dialog"):
                npc = params.get("npc_id")
                if npc:
                    add(npc, et)

            elif et == "create_dungeon":
                did = params.get("dungeon_id")
                if did:
                    add(did, et)

            elif et == "begin_combat":
                boss = params.get("boss_mob_id") or params.get("combat_target")
                if boss:
                    add(boss, "begin_combat")

    return edges


# ------------------------------------------------------------
# VALIDATION SUITE
# ------------------------------------------------------------

def validate_graph(nodes, edges):
    report = {}

    node_ids = set(nodes.keys())
    task_ids = {nid for nid, d in nodes.items() if d["type"] == "task"}

    # Build adjacency only for edges that reference known nodes.
    outgoing = defaultdict(list)
    incoming = defaultdict(list)
    missing_nodes = []

    for e in edges:
        src = e.get("src")
        dst = e.get("dst")
        # If either end is unknown, record as missing and skip adding to graph
        if src not in node_ids or dst not in node_ids:
            missing_nodes.append(e)
            continue
        outgoing[src].append(dst)
        incoming[dst].append(src)

    # Dangling tasks (no incoming)
    dangling = [t for t in task_ids if not incoming.get(t)]

    # Dead ends (no outgoing)
    dead_ends = [t for t in task_ids if not outgoing.get(t)]

    # Cycle detection (Kahn’s algorithm) — operate only on known nodes and filtered edges
    indeg = {n: len(incoming.get(n, [])) for n in node_ids}
    q = deque([n for n in node_ids if indeg.get(n, 0) == 0])
    visited = 0

    while q:
        n = q.popleft()
        visited += 1
        for nxt in outgoing.get(n, []):
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)

    cycles_exist = visited != len(node_ids)

    report["missing_nodes"] = missing_nodes
    report["dangling_tasks"] = dangling
    report["dead_end_tasks"] = dead_ends
    report["cycles_detected"] = cycles_exist

    return report


# ------------------------------------------------------------
# SUMMARIES
# ------------------------------------------------------------

def summarize(nodes, edges):
    groups = defaultdict(lambda: {"tasks": 0, "npcs": 0, "dungeons": 0, "edges": 0})

    for n in nodes.values():
        g = n["group"]
        if n["type"] == "task":
            groups[g]["tasks"] += 1
        elif n["type"] == "npc":
            groups[g]["npcs"] += 1
        elif n["type"] == "dungeon":
            groups[g]["dungeons"] += 1

    for e in edges:
        groups[e["src_group"]]["edges"] += 1

    return groups


# ------------------------------------------------------------
# MERMAID SWIMLANES
# ------------------------------------------------------------

def write_mermaid_swimlanes(nodes, edges, path: Path):
    groups = defaultdict(list)
    for n in nodes.values():
        groups[n["group"]].append(n)

    lines = ["flowchart LR"]

    # Subgraphs
    for g, items in groups.items():
        lines.append(f"  subgraph {g}")
        for n in items:
            if n["type"] == "task":
                lines.append(f'    {n["id"]}["{n["label"]}"]')
            elif n["type"] == "npc":
                lines.append(f'    {n["id"]}({n["label"]})')
            else:
                lines.append(f'    {n["id"]}{{"{n["label"]}"}}')
        lines.append("  end")

    # Edges
    for e in edges:
        lines.append(f'  {e["src"]} -->|{e["label"]}| {e["dst"]}')

    path.write_text("\n".join(lines), encoding="utf-8")


# ------------------------------------------------------------
# CSV EXPORT
# ------------------------------------------------------------

def write_csv(nodes, edges, node_path: Path, edge_path: Path):
    with node_path.open("w", newline='', encoding="utf-8") as nf:
        writer = csv.DictWriter(nf, fieldnames=["id", "type", "label", "group"])
        writer.writeheader()
        for n in nodes.values():
            writer.writerow(n)

    with edge_path.open("w", newline='', encoding="utf-8") as ef:
        writer = csv.DictWriter(ef, fieldnames=["src", "dst", "label", "src_group", "dst_group"])
        writer.writeheader()
        for e in edges:
            writer.writerow(e)


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------

def main():
    global node_groups

    nodes = build_nodes()
    node_groups = {n: d["group"] for n, d in nodes.items()}
    edges = build_edges()

    validation = validate_graph(nodes, edges)
    summaries = summarize(nodes, edges)

    write_mermaid_swimlanes(nodes, edges, OUT / "story_flow_swimlanes.mmd")
    write_csv(nodes, edges, OUT / "nodes_v2.csv", OUT / "edges_v2.csv")

    raw = {
        "nodes": list(nodes.values()),
        "edges": edges,
        "summaries": summaries,
        "validation": validation
    }
    (OUT / "story_raw_v2.json").write_text(json.dumps(raw, indent=2))

    print("Export complete →", OUT)


if __name__ == "__main__":
    main()
