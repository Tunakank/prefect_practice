import time
from prefect import task


class parallelTasks():
    @task
    def parallel_test1(text):
        """ 並列実行のテスト用1 """
        time.sleep(3)
        print(f"_parallel_test1 done! {text}")

    @task
    def parallel_test2(text):
        """ 並列実行のテスト用2 """
        time.sleep(5)
        print(f"_parallel_test2 done! {text}")
