from background_task import calculate_fibo

job = calculate_fibo.delay(20)


while True:
    print(job.state)
    if job.ready():
        print(job.result)
        break
