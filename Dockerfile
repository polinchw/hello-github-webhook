FROM python:3.6-alpine

ADD . /app/

WORKDIR /app

RUN pip install 'pip==20.1'
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9090

ENTRYPOINT ["python", "main.py"]