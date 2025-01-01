# Use a slimmer Python base image to reduce image size
FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/