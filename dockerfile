# Use the official n8n image as the base image
FROM n8nio/n8n:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install youtube_transcript_api
RUN pip3 install youtube-transcript-api

# Start n8n (this is inherited from the base image)
