from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.proposalAgent.models.db_models import create_tables
from appRouter import router

print(
    "Hello from main.py!", flush=True
)  # Debug statement to confirm the file is being executed


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing database...", flush=True)
    create_tables()

    yield

    print("Shutting down...", flush=True)


app = FastAPI(lifespan=lifespan)
app.include_router(router)
