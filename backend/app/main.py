from flask import Flask
from app.api.story import story_bp

def create_app():
    """
    Initialize Flask application and register blueprints.
    """
    app = Flask(__name__)
    
    # Register API routes
    app.register_blueprint(story_bp, url_prefix="/api/story")
    
    return app

if __name__ == "__main__":
    print(11111)
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
