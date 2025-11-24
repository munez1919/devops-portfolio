FROM python:3.11-slim AS build

WORKDIR /app

# Копируем requirements.txt в build stage
COPY requirements.txt .

RUN pip install --upgrade pip && pip wheel -r requirements.txt --wheel-dir /wheels


# ---------- STAGE 2 ----------
FROM python:3.11-slim

WORKDIR /app

# Копируем wheels
COPY --from=build /wheels /wheels

# Копируем requirements.txt еще раз!
COPY requirements.txt .

RUN pip install --no-index --find-links=/wheels -r requirements.txt

# Копируем всё приложение
COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]

