import json
import requests
from prefect import task


class discordTasks():
    @task
    def send_message(content: str, webhook_url: str) -> dict:
        """ discordへメッセージを送信する """
        main_content = {'content': content}
        headers = {'Content-Type': 'application/json'}

        requests.post(webhook_url, json.dumps(main_content), headers=headers)
