FROM agrigorev/zoomcamp-model:2025

WORKDIR /code

COPY main.py .
RUN pip install --no-cache-dir fastapi uvicorn requests
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
