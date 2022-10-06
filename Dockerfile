FROM python:3.9

EXPOSE 8080
RUN mkdir -p /usr/src/test-app/

WORKDIR /usr/src/test-app/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./ ./
RUN pip install --upgrade pip

COPY serviceapi/token.json .
COPY credentials1.json .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt