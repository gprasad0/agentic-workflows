from app.proposalAgent.models.schemas import ProposalRequest
from app.proposalAgent.models.db_models import get_connection


def proposal(body: ProposalRequest):
    db_connection = get_connection()
    # Implement proposal generation logic here
    cursor = db_connection.cursor()
    cursor.execute(
        """
        INSERT INTO proposals (prospect_name, company_name, prospect_url, call_notes, title, description, budget, additional_context)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
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
