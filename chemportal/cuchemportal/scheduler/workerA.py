from celery import Celery

# Initialize Celery
CELERY_RESULT_BACKEND = 'rpc://'
app = Celery('workerA', broker='pyamqp://guest@localhost//', backend = CELERY_RESULT_BACKEND)

@app.task(name = "task.concatenate_strings")
def concatenate_strings(a: str, b: str) -> str:
    return str(a) + str(b)
