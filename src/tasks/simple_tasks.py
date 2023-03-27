from datetime import timedelta
from prefect import task
from prefect.tasks import task_input_hash


class simpleTasks():
    @task
    def get_foobar():
        """ foobarを返します """
        return "foobar"

    @task(retries=2,  # 失敗した際のリトライ回数
          retry_delay_seconds=60,  # 失敗した際、何秒待って再実行するか
          cache_key_fn=task_input_hash,  # タスクのキャッシュ設定
          cache_expiration=timedelta(minutes=1)  # キャッシュの有効期限
          )
    def print_text(text):
        """ 文章の出力 """
        print(text)
