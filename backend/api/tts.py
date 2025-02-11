import logging
from flask import Blueprint, request, jsonify
from backend.services.tts_generator.tts_api import generate_tts_audio
import os

# Configure logging (only once)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Create Blueprint for TTS API
tts_bp = Blueprint("tts", __name__)

@tts_bp.route('/read', methods=['POST'])
def read_story():
    """
    API for reading a story using TTS.
    """
    try:
        # Ensure JSON data is present
        if not request.is_json:
            logging.warning("Invalid request: Content-Type is not JSON")
            return jsonify({"error": "Invalid request, Content-Type must be application/json"}), 400

        data = request.get_json()
        story_text = data.get("story", "")

        # Log received data
        logging.debug(f"Received story: {story_text}")

        # Validate input
        if not story_text:
            logging.warning("Missing story text in request")
            return jsonify({"error": "Story text is required."}), 400

        # Generate audio for the story
        audio_path = generate_tts_audio(story_text)
        logging.info("Audio generated successfully")

        return jsonify({"audio_url": f"/shared_resources/audio/{os.path.basename(audio_path)}"}), 200

    except Exception as e:
        logging.error(f"Error generating audio: {str(e)}", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500