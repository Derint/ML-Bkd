# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set environment variables to prevent Python from writing pyc files and to buffer outputs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY ../requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port Quart will run on
EXPOSE 5000

# Set the QUART_APP environment variable
ENV QUART_APP=app.main:create_app

# Set the command to run the Quart app
CMD ["quart", "run"]
