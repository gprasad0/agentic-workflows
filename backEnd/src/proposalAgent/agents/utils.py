# from backend.src.proposalAgent.models.schemas import ParsedCallData

# async def scrapeInternetData(toolJson: list[dict], url: str, parsed_data: ParsedCallData):
#     """
#     Scrapes data from the internet.
#     Uses the scrape tool and serper tool functions to gather information about a company.
#     """
#     messages = [
#         {
#             "role":"system",
#             "content": f"You are a research planner assistant. Your task is to gather info about the company from the internet\
#                         You will be given a URL - {url} to scrape and a list of tools to use. \
#                         There will be two tools available to you: {toolJson}. scraper_tool is a scraper that can scrape \
#                         homepage links, and serper_search_tool is used to search for public information about the company."
#         }
#     ]


# async def handleTool(tool_name):
#     if tool_name == "scrape_homepage":
#         // call the scrape homepage again
#     elif tool_name == "serper":
#         //call the serper tool
