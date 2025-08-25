# --- Base build ---
FROM python:alpine3.22 AS base
# RUN apk add --no-cache gcc 
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Dev image --
# bind mounted source
FROM base AS dev
# EXPOSE 5000
CMD ["flask", "--app", "app.py", "--debug", "run", "--host=0.0.0.0", "--port=5000"]


# --- Prod ---
# Prod image — copy code into container
FROM base AS prod
RUN pip install --no-cache-dir gunicorn
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]