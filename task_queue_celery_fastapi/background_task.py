from celery import Celery
from time import sleep

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//', backend='rpc://')


@app.task
def calculate_fibo(n: int):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    sleep(5)
    return b