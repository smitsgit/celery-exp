from pandas_datareader import data
from celery_app import app
import time


@app.task
def get_stock_info(delay):
    print('hello Celery--------')
    time.sleep(delay)
    print('Whats up')
    return 10

@app.task
def call_back(num, zoom=1, name='hello'):
    print("Everything is done------")
    print("Everything is done------")
    print("### {} - {}".format(zoom, name))
    return sum(num)

@app.task
def short_call_back(num):
    print("short_call_back is done------")
    print("short_call_back is done------")
    return sum(num)

