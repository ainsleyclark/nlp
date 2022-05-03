FROM python:latest

WORKDIR /app

ADD start.sh /
RUN chmod +x /start.sh

COPY . .

CMD [ "python3", "main.py"]
