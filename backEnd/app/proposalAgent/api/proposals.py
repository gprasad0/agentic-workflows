from app.proposalAgent.models.schemas import ProposalRequest
from app.proposalAgent.models.db_models import get_connection


def createProposal(body: ProposalRequest):
    db_connection = get_connection()
    # Implement proposal generation logic here
    cursor = db_connection.cursor()
    cursor.execute(
        """
        INSERT INTO proposals ( prospect_url, call_notes, title, description, budget, additional_context)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            body.title,
            body.description,
            body.budget,
            body.call_notes,
            body.prospect_url,
            body.additional_context,
        ),
    )
    proposal_id = cursor.lastrowid
    db_connection.commit()
    db_connection.close()
    return {"message": "Proposal generated successfully", "proposal_id": proposal_id}


def getProposal(proposal_id: int):
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
