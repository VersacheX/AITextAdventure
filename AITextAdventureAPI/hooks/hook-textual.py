# PyInstaller hook for Textual.
# Textual's widgets/__init__.py uses __getattr__ for lazy imports, so the
# static analyser misses almost every widget module. collect_submodules()
# forces every subpackage to be included in the frozen bundle.

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hiddenimports = (
    collect_submodules('textual')
    + collect_submodules('rich')
)

# Bundle Textual's CSS/TCSS theme files and any other package data it ships.
datas = collect_data_files('textual')