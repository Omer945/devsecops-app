FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Utilisateur non root (bonne pratique sécurité)
RUN useradd -m user
USER user

EXPOSE 80
CMD ["python", "app.py"]
