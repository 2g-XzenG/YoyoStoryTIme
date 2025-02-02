from flask import Flask, send_from_directory
from api.story import story_bp  # Adjust import path if necessary

def create_app():
    """
    Initialize and configure the Flask application.
    """
    app = Flask(__name__, static_folder="frontend/web", static_url_path="/")

    # Register the API blueprint
    app.register_blueprint(story_bp, url_prefix="/api/story")

    # Serve the index.html file for the root URL
    @app.route("/")
    def index():
        return send_from_directory(app.static_folder, "index.html")

    # Serve static files (CSS, JS, images, etc.)
    @app.route("/<path:filename>")
    def static_files(filename):
        return send_from_directory(app.static_folder, filename)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8008)
