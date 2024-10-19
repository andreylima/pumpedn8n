# Use the official n8n image as the base image
FROM python:3-alpine3.14

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install youtube_transcript_api
RUN pip3 install youtube-transcript-api# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# Start n8n (this is inherited from the base image)
