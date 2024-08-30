# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install Git (if needed for cloning)
RUN apt-get update && apt-get install -y git && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy application files into the container
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py

# Specify the command to run your application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

# Expose the port your application will run on
EXPOSE 8080