import datetime
import asyncio
from prefect import flow
from tasks.simple_tasks import simpleTasks
from tasks.parallel_tasks import parallelTasks
from tasks.asynchronous_tasks import asynchronousTasks


@flow(name="output_foobar",  # フローの名前
      version="1.0",  # バージョン
      flow_run_name="{name}-on-{date:%A}"  # フロー実行時の名称
      )
def output_text(name: str, date: datetime.datetime):
    """ 文章を出力するflow(並列処理) """
    # 上記は`@flow(description="文章を出力するflow")`でもOK

    # 1つずつ順次実行される
    text = simpleTasks.get_foobar()
    simpleTasks.print_text(text)

    # `.submit()`を末尾につけると並列実行になる
    # 関数の引数は`.submit()`の方に書く
    parallelTasks.parallel_test1.submit(1234)
    parallelTasks.parallel_test2.submit("ABCD")


@flow(name="asynchronous_output_foobar",
      version="1.0",
      flow_run_name="{name}-on-{date:%A}"
      )
async def asynchronous_output_text(name: str, date: datetime.datetime):
    """ 文章を出力するflow(非同期処理) """
    text = simpleTasks.get_foobar()
    simpleTasks.print_text(text)

    # 以下は非同期処理を行う
    await asynchronousTasks.asynchronous_test1(1234)
    await asynchronousTasks.asynchronous_test2("ABCD")

    print("First asynchronous test is done!")

    # 以下は非同期で並列処理を行う
    await asynchronousTasks.asynchronous_test1.submit(1234)
    await asynchronousTasks.asynchronous_test2.submit("ABCD")


# フロー実行
output_text(name="marvin", date=datetime.datetime.utcnow())
asyncio.run(
    asynchronous_output_text(
        name="marvin", date=datetime.datetime.utcnow()
    )
)
