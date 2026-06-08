from fastapi import FastAPI

# from app.proposalAgent import proposals

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
