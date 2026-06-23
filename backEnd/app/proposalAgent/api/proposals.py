from app.proposalAgent.models.schemas import (
    ProposalRequest,
    parsedCallData,
)
from app.proposalAgent.models.db_models import get_connection

from app.llm.client import client
from app.proposalAgent.agents.prompts import parseDataPrompt


async def createProposal(body: ProposalRequest):
    parsedData = await parseData(body)
    researchedData = await researchProposal(parsedData)

    db_connection = get_connection()
    # Implement proposal generation logic here
    cursor = db_connection.cursor()
    cursor.execute(
        """
        INSERT INTO proposals ( prospect_url, call_notes, title, description, budget, additional_context)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            body.prospect_url,
            body.call_notes,
            body.title,
            body.description,
            body.budget,
            body.additional_context,
        ),  # prevents SQL injection by using parameterized queries
    )
    proposal_id = cursor.lastrowid
    db_connection.commit()
    db_connection.close()
    return {"message": "Proposal generated successfully", "proposal_id": proposal_id}


async def getProposal(proposal_id: int):
    db_connection = get_connection()
    cursor = db_connection.cursor()
    cursor.execute(
        """
        SELECT * FROM proposals WHERE id = ?
        """,
        (proposal_id,),
    )
    proposal_data = cursor.fetchone()
    db_connection.close()
    if proposal_data:
        return dict(proposal_data)
    else:
        return {"message": "Proposal not found"}


async def parseData(body: ProposalRequest):
    prompt = parseDataPrompt.format(ProposalRequest=body.model_dump_json(indent=2))
    parsed_data = await client.generate_structured(prompt, parsedCallData)
    print(
        f"Raw LLM response for structured output:\n{parsed_data.model_dump_json(indent=2)}\n"
    )

    return parsed_data


async def researchProposal(parsedData: parsedCallData):
    return {
        "research_output": "Research output based on the provided proposal request.",
        "retrieved_context": "Retrieved context relevant to the proposal.",
    }
