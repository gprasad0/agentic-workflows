from fastapi import FastAPI
from app.proposalAgent.api.proposals import proposal

print(
    "Hello from main.py!", proposal()
)  # Debug statement to confirm the file is being executed
app = FastAPI()


@app.get("/")
async def root():
    return proposal()
