FROM python:3.13-slim

# set working directory
WORKDIR /app

# i now install system dependencies (for nltk, pymongo, pandas)
RUN apt-get update && apt-get install -y gcc g++ libffi-dev && rm -rf /var/lib/apt/lists/*

# and copy requirements first (for caching)
COPY requirements.txt .

# install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# need to download nltk data
RUN python -m nltk.downloader -d /usr/local/share/nltk_data vader_lexicon
ENV NLTK_DATA=/usr/local/share/nltk_data

# and copy source code
COPY app/ app/
COPY data/ data/

# to create non-root user
RUN useradd -m appuser
USER appuser

# and expose port
EXPOSE 8000

# now i run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]