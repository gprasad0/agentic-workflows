import asyncio
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Any
from backend.config import settings


async def scrape_homepage_and_extract_links(base_url: str) -> Dict[str, Any]:
    """
    Scrapes a homepage, extracts the readable text, and returns a deduplicated
    list of internal links found on the page.
    """
    # 1. We use a realistic User-Agent to avoid basic bot-blockers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # 2. Async HTTP request using httpx
        async with httpx.AsyncClient(
            headers=headers, timeout=10.0, follow_redirects=True
        ) as client:
            response = await client.get(base_url)
            response.raise_for_status()  # Raise an exception for bad status codes (404, 500)

            # 3. Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # 4. Extract and normalize all internal links BEFORE decomposing the header/footer
            internal_links = set()
            base_domain = urlparse(base_url).netloc

            for a_tag in soup.find_all("a", href=True):
                href = a_tag["href"]

                # Skip mailto:, tel:, anchor links, and javascript actions : skip useless links
                if href.startswith(("mailto:", "tel:", "#", "javascript:")):
                    continue

                # Normalize relative URLs (e.g., '/about' -> 'https://example.com/about')
                full_url = urljoin(base_url, href)

                # Strip trailing slashes to prevent duplicates (e.g., /about and /about/)
                full_url = full_url.rstrip("/")

                # Only keep internal links (belonging to the same domain)
                if urlparse(full_url).netloc == base_domain:
                    internal_links.add(full_url)

            # 5. Clean the text (Remove scripts, styles, and extra whitespace)
            for script_or_style in soup(
                ["script", "style", "noscript", "header", "footer"]
            ):
                script_or_style.decompose()

            clean_text = soup.get_text(separator=" ", strip=True)

            return {
                "success": True,
                "url": base_url,
                "content_preview": clean_text[:1000]
                + "...",  # Just returning the first 1000 chars for safety
                "internal_links": list(internal_links),
            }

    except Exception as e:
        return {"success": False, "url": base_url, "error": str(e)}


async def serper_tool(query: str):
    """Scrapes google with the query params given"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://google.serper.dev/search",
            headers={
                "X-API-KEY": settings.SERPER_API_KEY,
                "Content-Type": "application/json",
            },
            json={"q": query},
        )

    return response.json()


# # --- Testing the Scraper ---
# async def main():
#     target_url = "https://scrapeme.live/shop/"  # A safe practice target
#     print(f"Scraping {target_url}...\n")

#     result = await scrape_homepage_and_extract_links(target_url)

#     if result["success"]:
#         print(f"Found {len(result['internal_links'])} internal links.")
#         print("\nTop 5 links:")
#         for link in result["internal_links"][:5]:
#             print(f"- {link}")
#         print("\nContent Preview:")
#         print(result["content_preview"])
#     else:
#         print(f"Failed to scrape: {result.get('error')}")


# if __name__ == "__main__":
#     asyncio.run(main())
