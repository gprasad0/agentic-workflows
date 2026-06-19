# from contextlib import asynccontextmanager
# from fastapi import FastAPI

# from proposalAgent.models.db_models import create_tables

# print("Hello from main.py!")  # Debug statement to confirm the file is being executed


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("Initializing database...")
#     create_tables()

#     yield

#     print("Shutting down...")


# app = FastAPI(lifespan=lifespan)
# print("Shutting down...")
