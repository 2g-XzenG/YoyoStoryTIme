import logging
from flask import Blueprint, request, jsonify
from services.story_generator.story_api import generate_story_text
from services.story_generator.prompts import format_prompt

# Configure logging (only once)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Create Blueprint for story API
story_bp = Blueprint("story", __name__)

@story_bp.route('/generate', methods=['POST'])
def generate_story():
    """
    API for generating a story.
    """
    try:
        # Ensure JSON data is present
        if not request.is_json:
            logging.warning("Invalid request: Content-Type is not JSON")
            return jsonify({"error": "Invalid request, Content-Type must be application/json"}), 400

        data = request.get_json()
        characters = data.get("characters", [])
        scene = data.get("scene", "")

        # Log received data
        logging.debug(f"Received characters: {characters}")
        logging.debug(f"Received scene: {scene}")

        # Validate input
        if not characters or not scene:
            logging.warning("Missing characters or scene in request")
            return jsonify({"error": "Characters and scene are required."}), 400

        # Format prompt
        prompt = format_prompt(characters, scene)
        logging.debug(f"Generated prompt: {prompt}")

        # Generate story
        story_text = generate_story_text(prompt)
        logging.info("Story generated successfully")

        return jsonify({"story": story_text}), 200

    except Exception as e:
        logging.error(f"Error generating story: {str(e)}", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500
