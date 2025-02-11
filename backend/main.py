from flask import Flask, request, send_from_directory, jsonify
import os

def create_app():
    """
    Initialize and configure the Flask application.
    """
    app = Flask(__name__, static_folder="../frontend/web", static_url_path="/")

    # Register the API blueprint
    from backend.api.story import story_bp  # Adjust import path if necessary
    from backend.api.tts import tts_bp  # Import the TTS blueprint
    app.register_blueprint(story_bp, url_prefix="/api/story")
    app.register_blueprint(tts_bp, url_prefix="/api/tts")  # Register the TTS blueprint

    # Serve the index.html file for the root URL
    @app.route("/")
    def index():
        print(f"Serving index.html from {app.static_folder}", flush=True)
        return send_from_directory(app.static_folder, "index.html")

    # Serve static files (CSS, JS, images, etc.)
    @app.route("/<path:filename>")
    def static_files(filename):
        print(f"Serving static file: {filename} from {app.static_folder}", flush=True)
        return send_from_directory(app.static_folder, filename)

    # Serve shared resources
    @app.route("/shared_resources/<path:filename>")
    def shared_resources(filename):
        shared_resources_path = os.path.join("shared_resources", filename)
        print(f"Serving shared resource: {filename} from {shared_resources_path}", flush=True)
        if not os.path.exists(shared_resources_path):
            print(f"File not found: {shared_resources_path}", flush=True)
        else:
            print(f"File exists: {shared_resources_path}", flush=True)
        return send_from_directory("../shared_resources", filename)

    return app

if __name__ == "__main__":
    app = create_app()
    print("Flask app created and running", flush=True)
    app.run(debug=True, host="0.0.0.0", port=8008)