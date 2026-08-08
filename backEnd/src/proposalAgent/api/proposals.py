from src.outreachAgent.nodes import scrape

# from src.proposalAgent.agents.utils import scrapeInternetData
from src.proposalAgent.models.schemas import (
    ProposalRequest,
    ParsedCallData,
    ResearchPlanner,
)
from src.proposalAgent.models.db_models import get_connection
from src.proposalAgent.services.scrapeBeautifulSoup import (
    scrape_homepage_and_extract_links,
    serper_tool,
)
from src.llm.client import client
from src.proposalAgent.agents.prompts import parseDataPrompt, RESEARCH_PLANNER_PROMPT
import json
from src.proposalAgent.agents.toolsDefinition import scraper_tool, serper_search_tool

url = "https://www.hcltech.com/"


researchTools = [scraper_tool, serper_search_tool]

# use scraper and serper to get data -> use this data in the research planner to decide
# -> which pages to scrape and using the serper data which questions to ask
# using the scraper again scrape the decide pages
# using the serper data and the scraped data and the parsed call data synthesize a research output

# Check if serper is working and if the scraper is working


async def createProposal(body: ProposalRequest) -> dict:
    # parsedData = await parseData(body)
    # researchedData = await researchProposalOrchestrator(parsedData)
    scrapedData = await scrape_homepage_and_extract_links("https://innovkraft.com/")
    # serperData = await serper_tool("https://innovkraft.com/")
    # scrapedData = await scrapeInternetData(researchTools, url, parsedData)
    # safe_output = json.dumps(scrapedData, ensure_ascii=True, indent=2)
    # print("scrapedData-->", safe_output)
    # db_connection = get_connection()
    # # Implement proposal generation logic here
    # cursor = db_connection.cursor()
    # cursor.execute(
    #     """
    #     INSERT INTO proposals ( prospect_url, call_notes, title, description, budget, additional_context)
    #     VALUES (?, ?, ?, ?, ?, ?)
    #     """,
    #     (
    #         body.prospect_url,
    #         body.call_notes,
    #         body.title,
    #         body.description,
    #         body.budget,
    #         body.additional_context,
    #     ),  # prevents SQL injection by using parameterized queries
    # )
    # proposal_id = cursor.lastrowid
    # db_connection.commit()
    # db_connection.close()
    # return {"message": "Proposal generated successfully", "proposal_id": proposal_id}
    return {"message": "Proposal generated successfully"}


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
    parsed_data = await client.generate_structured(prompt, ParsedCallData)
    print(
        f"Raw LLM response for structured output:\n{parsed_data.model_dump_json(indent=2)}\n"
    )

    return parsed_data


async def researchProposalOrchestrator(parsedData: ParsedCallData):
    userPrompt = f"Here is the parsed discovery call data:\n\n{parsedData.model_dump_json(indent=2)}"

    researchPlanner = await client.generate_structured(
        userPrompt, ResearchPlanner, RESEARCH_PLANNER_PROMPT
    )
    print(
        f"Raw LLM response for researchPlanner:\n{researchPlanner.model_dump_json(indent=2)}\n"
    )
    return {
        "research_output": "Research output based on the provided proposal request.",
        "retrieved_context": "Retrieved context relevant to the proposal.",
    }


async def filter_relevant_links(
    scraped_links: list[str], relevant_keywords: list[str]
) -> list[str]:
    """Filter the scraped links based on relevant keywords."""
    filtered_links = []
    for link in scraped_links:
        if any(keyword.lower() in link.lower() for keyword in relevant_keywords):
            filtered_links.append(link)
    return filtered_links
