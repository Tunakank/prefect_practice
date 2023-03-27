import requests
# import feedparser
from prefect import task


class apiTasks():
    @task
    def call_api() -> dict:
        """ Apiを叩き、dict型で返す """
        response = requests.get("http://time.jsontest.com/").json()
        return response

    @task
    def call_rss_feed() -> dict:
        """ RSSフィード """
        # return feedparser.parse({ここにurl})
        return {}
