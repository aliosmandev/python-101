from fastapi import FastAPI
from .libs.scraper import twitterScrape, TwitterResponse

app = FastAPI()

app.title = "Twitter Scraper"
app.description = "A simple Twitter scraper"
app.version = "0.0.1"

@app.post("/twitter/scrape", response_model=TwitterResponse)
async def scrape(username: str):
    return await twitterScrape(username)

