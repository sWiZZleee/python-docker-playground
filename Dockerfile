FROM python:3.7-alpine

WORKDIR /app

COPY lib/ /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]

