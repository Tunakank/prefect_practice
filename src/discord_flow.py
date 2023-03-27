# import os
import sys
from prefect import flow
# from tasks.api_tasks import apiTasks
from tasks.discord_task import discordTasks


@flow(name="discord", version="1.2")
def discord(DISCORD_WEBHOOK_URL: str):
    # 実行するたびに確認しに行ってしまうのでコメントアウト
    # call_rss_feed_response = apiTasks.call_rss_feed()
    # discordTasks.send_message(
    #     content=call_rss_feed_response.entries[0].link, webhook_url=os.environ["DISCORD_WEBHOOK_URL"])
    discordTasks.send_message(
        content="call_rss_feed_response.entries[0].link", webhook_url=DISCORD_WEBHOOK_URL)


if __name__ == "__main__":
    DISCORD_WEBHOOK_URL = sys.argv[1]
    discord(DISCORD_WEBHOOK_URL)
