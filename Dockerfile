FROM python:3.8.6
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY bot.py ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./bot.py" ]
