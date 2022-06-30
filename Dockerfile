From python:3.8.5-alpine
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/