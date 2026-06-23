from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from user_api.routers import auth_router
from user_api.services.auth_service import init_db


def create_app() -> FastAPI:
    app = FastAPI(title="AITextAdventure - Old User API", version="0.1")

    # CORS (allow local dev)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # include routers
    app.include_router(auth_router.router)

    @app.on_event("startup")
    def _startup():
        try:
            init_db()
        except Exception:
            pass

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()
