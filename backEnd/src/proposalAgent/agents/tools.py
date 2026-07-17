scraper_tool = {
    "type": "function",
    "function": {
        "name": "scrape_page",
        "description": "",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL of the page to scrape",
                }
            },
            "required": ["url"],
        },
    },
}

serper_tool = {
    "type": "function",
    "function": {
        "name": "serpenter_tool",
        "description": """Search Google for information about a company. 
        Use this to find news, reviews, or public information.""",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "Search query"}},
            "required": ["query"],
        },
    },
}
