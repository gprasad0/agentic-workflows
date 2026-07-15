from fastapi import APIRouter
from src.proposalAgent.api.proposals import createProposal
from src.proposalAgent.api.proposals import getProposal
from src.proposalAgent.models.schemas import (
    parsedCallData,
    ResearchOutput,
    RetrievedContext,
    ProposalSections,
    SectionScore,
    ProposalRequest,
)

router = APIRouter()


@router.post("/proposalAgent")
async def add_proposal(body: ProposalRequest):
    proposalData = await createProposal(body)
    return proposalData


@router.get("/proposalAgent/{proposal_id}")
async def retrieve_proposal(proposal_id: int):
    proposalData = await getProposal(proposal_id)
    return proposalData
