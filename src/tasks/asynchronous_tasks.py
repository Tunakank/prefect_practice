import asyncio
from prefect import task


class asynchronousTasks():
    # 非同期処理がしたい場合はasync/awaitをつける
    @task
    async def asynchronous_test1(text):
        """ 非同期処理のテスト用1 """
        await asyncio.sleep(3)
        print(f"_asynchronous_test1 done! {text}")

    @task
    async def asynchronous_test2(text):
        """ 非同期処理のテスト用2 """
        await asyncio.sleep(5)
        print(f"_asynchronous_test2 done! {text}")
