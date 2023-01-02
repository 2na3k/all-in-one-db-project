FROM python:3.10.4

WORKDIR /app
COPY script/init_postgres.py init.py
COPY requirements.txt requirements.txt

RUN apt-get install wget
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "init.py"]