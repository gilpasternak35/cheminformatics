from celery import Celery

# Initialize Celery
CELERY_RESULT_BACKEND = 'rpc://'
app = Celery('workerA', broker='pyamqp://guest@localhost//', backend = CELERY_RESULT_BACKEND)

@app.task(name = "task.trim_string")
def trim_string(inp: str) -> str:
    return inp.rstrip()

