from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from pytube import YouTube

app = Flask(__name__)

# Existing home route
@app.route('/')
def home():
    return "Hello from Flask!"

# New transcription route
@app.route('/transcribe', methods=['POST'])
def transcribe():
    data = request.get_json()
    
    # Check if 'urls' is in the POST data
    if not data or 'urls' not in data:
        return jsonify({"error": "No URLs provided"}), 400
    
    urls = data['urls']
    
    transcripts = {}
    
    for url in urls:
        video_id = get_video_id(url)
        transcript, error = get_transcript(video_id, language='pt')
        
        if transcript:
            transcripts[url] = transcript
        else:
            transcripts[url] = f"Error: {error}"
    
    return jsonify(transcripts), 200

# Function to get the video ID from the YouTube URL
def get_video_id(youtube_url):
    yt = YouTube(youtube_url)
    return yt.video_id

# Function to get the transcript of a video using YouTubeTranscriptApi
def get_transcript(video_id, language='pt'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    except TranscriptsDisabled:
        return None, "Transcripts are disabled for this video."
    except Exception as e:
        return None, f"An error occurred: {str(e)}"
    
    full_transcript = " ".join([entry['text'] for entry in transcript])
    return full_transcript, None

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
