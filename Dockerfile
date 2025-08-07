# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables to avoid buffering
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "main.py"]
