FROM python:3
COPY requirements.txt /
WORKDIR /gridpoint_back
COPY . .
RUN pip install -r /requirements.txt
EXPOSE 8000