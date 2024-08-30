# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install Git (required for cloning repositories)
RUN apt-get update && apt-get install -y git && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Clone the repository directly into /app
RUN git clone https://github.com/OrphLab/myjourney-sc.git . && \
    git pull origin main  

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run your application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

# Expose the port your application will run on
EXPOSE 8080