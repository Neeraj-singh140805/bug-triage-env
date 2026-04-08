FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir gradio fastapi uvicorn openai

EXPOSE 7860

CMD ["python", "app.py"]