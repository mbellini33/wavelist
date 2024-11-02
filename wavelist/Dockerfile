# Usa un'immagine di base leggera con Python
FROM python:3.9-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia il file requirements.txt e installa le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il contenuto del progetto (incluso static e altri file Python)
COPY wavelist/ .

# Espone la porta 8000
EXPOSE 8080

# Esegue l'app FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]