# Use the official Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy everything from the local directory into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 (for FastAPI/Flask)
EXPOSE 8000

# Start the FastAPI/Flask server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
