FROM python:3.12.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0"]