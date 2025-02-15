# Python 3.9
FROM python:3.9

# Setting working directory
WORKDIR /app

# Copying files
COPY . .

# Instalation of dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
