from fastapi import APIRouter
from app.proposalAgent.api.proposals import proposal
from app.proposalAgent.models.schemas import (
    parsedCallData,
    ResearchOutput,
    RetrievedContext,
    ProposalSections,
    SectionScore,
    ProposalRequest,
)

router = APIRouter()


@router.post("/proposalAgent")
async def get_proposal(body: ProposalRequest):
    proposalData = proposal(body)
    return proposalData
