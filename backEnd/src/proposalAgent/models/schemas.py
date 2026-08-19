from pydantic import BaseModel, Field
from enum import Enum


# -----------INPUT SCHEMA-----------#
class ProposalRequest(BaseModel):
    title: str
    description: str
    budget: float
    call_notes: str
    prospect_url: str
    additional_context: str


# -----------AGENT 1 OUTPUT SCHEMA-----------#
class ParsedCallData(BaseModel):
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
    prospect_url: str = ""  # URL for reference


# -----------Research Planner JSON-----------#
class ResearchPlanner(BaseModel):
    pages: list[str]
    questions: list[str]


# ----------SCRAPED DATA-------------#
class ScrapedData(BaseModel):
    title: str
    link: str
    snippet: str
    rating: float | None = None
    ratingCount: int | None = None


# -----------AGENT RESEARCH PLANNER-----------#
class ResearchPlannerQuestion(BaseModel):
    links: list[str]
    questions: list[str]


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
class ProposalSections(BaseModel):
    executive_summary: str
    situtation_analysis: str
    proposed_approach: str
    scope_and_deliverables: str
    timeline: str
    investment: str
    case_studies: str
    why_us: str
    next_steps: str


# -----------AGENT 5 OUTPUT SCHEMA-----------#
class SectionScore(BaseModel):
    section_name: str
    score: int = Field(..., ge=1, le=10)  # Score between 1 and 10
    feedback: str  # whats wrong or right
    needs_regeneration: bool  # should this be rewritten or not


class ReviewResult(BaseModel):
    reviewed_sections: ProposalSections  # Improved versions
    section_scores: list[SectionScore]
    overall_score: int = Field(..., ge=1, le=10)
    flags: list[str]  # any major issues for human attention
    suggestions: list[str]  # Recommendations for user


# -----------PIPELINE STATE-----------#
class PipelineStatus(str, Enum):
    PARSING = "parsing"
    RESEARCHING = "researching"
    RETRIEVING = "retrieving"
    GENERATING = "generating"
    REVIEWING = "reviewing"
    COMPLETE = "complete"
    ERROR = "error"


class PipelineState(BaseModel):
    status: PipelineStatus
    parsed: ParsedCallData | None = None
    research: ResearchOutput | None = None
    retrieved: RetrievedContext | None = None
    sections: ProposalSections | None = None
    review: ReviewResult | None = None
    error: str | None = None


# -----------HUMAN IN THE LOOP-----------#
class RegenerateRequest(BaseModel):
    section_name: str  # Which section to redo
    instructions: str = ""  # Any specific instructions for regeneration
    # eg, "Make the pricing more specific or Add more details about SEO"


# ------------RESEARCH SCHEMAS-----------#


class ResearchPlannerData(BaseModel):
    pages: list[str]
    scraped_preview: str
    serperData: list[dict]
    parsedData: ParsedCallData


class ExtractedFacts(BaseModel):
    company_summary: str
    target_audience: str
    services_offered: list[str]
    current_marketing: list[str]
    gaps: list[str]
    competitors: list[str]
    opportunities: list[str]
    recent_news: str = ""
    tech_stack: list[str] = []
