FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    chromium-driver chromium curl unzip gnupg2 \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/lib/chromium:/usr/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
