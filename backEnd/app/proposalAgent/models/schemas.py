from pydantic import BaseModel, Field
from enum import Enum


# -----------INPUT SCHEMA-----------#
class ProposalRequest(BaseModel):
    title: str = Field(..., example="New Marketing Strategy")
    description: str
    budget: float
    call_notes: str
    prospect_url: str
    additional_context: str


# -----------AGENT 1 OUTPUT SCHEMA-----------#
class parsedCallData(BaseModel):
    prospect_name: str
    company_name: str
    industry: str
    company_size: str
    goals: list[str]  # what they want to achieve
    pain_points: list[str]  # what challenges they are facing - current pain points
    services_needed: list[str]  # what services they are looking for
    budget_signals: str = ""  # Any budget mentions
    timeline: str = ""  # Any timeline mentions
    decision_makers: list[str] = []  # Any decision makers mentioned
    current_solution: str = ""  # What they are currently using (if mentioned)
    competitors: list[str] = []  # Any competitors mentioned


# -----------AGENT 2 OUTPUT SCHEMA-----------#


class ResearchOutput(BaseModel):
    company_summary: str  # what the company does
    target_audience: str  # who they are targeting
    services_offered: list[str]  # what services they offer
    current_marketing: list[str]  # what marketing strategy they are currently using
    gaps: list[str]  # any gaps in their current strategy
    competitors: list[str]  # who their competitors are
    oppurtunities: list[str]  # where you can help
    recent_news: str = ""  # any recent news about the company
    tech_stack: list[str] = []  # what tech stack they are using


# -----------AGENT 3 OUTPUT SCHEMA-----------#


class RetrievedContext(BaseModel):
    relevant_proposal_sections: list[str] = []  # past proposal snippets
    case_studies: list[str] = []  # Matching case studies
    service_descriptions: list[str] = []  # Relevant service details
    pricing_references: list[str] = []  # past Pricing for similar scope
    sources: list[str] = []  # source document names


# -----------AGENT 4 OUTPUT SCHEMA-----------#
