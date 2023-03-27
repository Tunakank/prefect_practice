import datetime
import pprint
from prefect import flow
from tasks.api_tasks import apiTasks


@flow(name="call_api_test", version="1.0", flow_run_name="{date}")
def call_api_test(date: datetime.datetime):
    """  """
    call_api_response = apiTasks.call_api()
    print(call_api_response)

    call_rss_feed_response = apiTasks.call_rss_feed()
    pprint.pprint(call_rss_feed_response)


call_api_test(date=datetime.datetime.utcnow())
