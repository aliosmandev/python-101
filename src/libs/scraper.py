from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ..utils.selectors import constants
from typing import Dict, List
from pydantic import BaseModel

class Post(BaseModel):
    text: str

class TwitterResponse(BaseModel):
    title: str
    posts: List[Post]

async def twitterScrape(username: str) -> TwitterResponse:
    driver = webdriver.Chrome()
    driver.get(f"https://twitter.com/{username}")
    wait = WebDriverWait(driver, 30)
    waitTwo = WebDriverWait(driver, 30)

    profileTitle = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, constants.title))).text

    posts = waitTwo.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, constants.posts)))
    
    post_texts = [post.text for post in posts]

    driver.close()

    return TwitterResponse(
        title=profileTitle,
        posts=[Post(text=post_text) for post_text in post_texts]
    )
