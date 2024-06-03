# Python Twitter Scrape

## Overview
This project is a simple Twitter scraper built with FastAPI and Selenium. It allows you to scrape tweets from a specified Twitter user.

## Features
- Scrape tweets from a Twitter user.
- Retrieve the profile title and posts.
- Asynchronous processing with FastAPI.
- JSON response with scraped data.

## Requirements
- Python 3.8+
- Selenium
- FastAPI
- Uvicorn
- WebDriver (e.g., ChromeDriver)

## Installation

### 1. Clone the repository:

```sh
git clone https://github.com/osmandlsmn/python-101.git
cd twitter-scrape
```

### 2. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the requirements:

```sh
pip install -r requirements.txt
```

### 4. Run the application:

```sh
make run
```

#### Alternatively, you can run the application directly with Uvicorn:

```sh
uvicorn src.main:app --host 0.0.0.0 --port 3000 --reload
````

### Project Structure

```
twitter-scrape/
├── src/
│   ├── main.py
│   └── utils/
│       └── selectors.py
├── requirements.txt
├── Makefile
└── README.md
```