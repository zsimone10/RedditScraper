import praw
from settings import reddit_creds as credentials
class RedditScraper:

    def __init__(self):
        """
        Initializes PRAW instance with the information from settings.py
        """
        self.reddit = praw.Reddit(
                                    client_id=credentials["id"],
                                    client_secret=credentials["secret"],
                                    password=credentials["password"],
                                    user_agent=credentials["user_agent"],
                                    username=credentials["username"],
                                )

    def search(self, subs_to_search, query):
        """ Basic Search function seraches a list of subreddits for a query word

        Args:
            subs_to_search: List of subreddit names (strings)
            query: search query

        Returns: None

        """
        for sub in subs_to_search:
            for submission in self.reddit.subreddit(sub).search(query):
                print(submission.title)
