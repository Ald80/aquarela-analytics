FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# COPY ./requirements.txt ./requirements.txt
# COPY ./alembic ./alembic
# COPY ./database ./database
# COPY ./exceptions ./exceptions
# COPY ./models ./models
# COPY ./routes ./routes
# COPY ./schemas ./schemas
# COPY ./tests ./tests
# COPY ./alembic.ini ./alembic.ini
# COPY ./main.py ./main.py

EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload