FROM python:3.11-alpine

WORKDIR /opt
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["./run.sh"]