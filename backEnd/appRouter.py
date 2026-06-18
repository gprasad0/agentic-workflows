from fastapi import APIRouter
from app.proposalAgent.api.proposals import proposal

router = APIRouter()


@router.get("/proposalAgent")
async def get_proposal():
    proposalData = proposal()
    return proposalData
