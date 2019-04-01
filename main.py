from Scraper import RedditScraper

if __name__ == "__main__":
    search_bot = RedditScraper()
    # Searches list of sub reddits for the query word
    search_bot.search(['all'], 'query')