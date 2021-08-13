FROM python:3
ADD requirements.txt /app/requirements.txt
ADD app.py /app/app.py
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py","--host=0.0.0.0"]