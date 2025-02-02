from flask import Blueprint, request, jsonify
from app.services.story_generator.story_api import generate_story_text
from app.services.story_generator.prompts import format_prompt

story_bp = Blueprint("story", __name__)

@story_bp.route('/generate', methods=['POST'])
def generate_story():
    """
    API for generating a story.
    """
    try:
        data = request.json
        characters = data.get("characters", [])
        scene = data.get("scene", "")

        # Validate input
        if not characters or not scene:
            return jsonify({"error": "Characters and scene are required."}), 400

        # Format prompt
        prompt = format_prompt(characters, scene)

        # Generate story
        story_text = generate_story_text(prompt)
        return jsonify({"story": story_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
