FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD ../requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
