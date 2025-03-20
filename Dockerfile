# 1️⃣ Use Python 3.10 as the base image
FROM python:3.10

# 2️⃣ Set the working directory inside the container
WORKDIR /app

# 3️⃣ Copy all project files into the container
COPY . .

# 4️⃣ Install dependencies from requirements.txt (without cache to reduce size)
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Set the command to start your FastAPI or Flask app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
