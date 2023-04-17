FROM python:3.11.3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
  apt-get -y install fortune fortunes-off fortunes-bofh-excuses

COPY . .

CMD [ "python", "./main.py" ]