import os
import requests
import json
from dotenv import load_dotenv

# .env読み込み
load_dotenv()


webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
main_content = {'content': '送るテキスト'}
headers = {'Content-Type': 'application/json'}

response = requests.post(
    webhook_url, json.dumps(main_content), headers=headers)
