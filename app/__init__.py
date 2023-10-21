# Import necessary modules from the Flask library.
from flask import Flask

# Import our own custom configuration and extensions.
from config import Config
from app.extensions import db

# Define a function to create the Flask application instance.
def create_app(config_class=Config):
    # Create a new Flask web server instance.
    app = Flask(__name__)

    # Configure our Flask app using settings from our custom configuration.
    app.config.from_object(config_class)

    # Initialize Flask extensions, in this case, the database.
    # This pattern makes it easy to add more extensions later.
    db.init_app(app)

    # Register the blueprints for different parts of the app.
    # Blueprints allow you to organize the app into distinct components.

    # Register the main blueprint. This doesn't have a URL prefix, 
    # so routes defined here will be at the root level.
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Register the posts blueprint. Routes defined here will be prefixed with '/posts'.
    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    # Register the questions blueprint. Routes defined here will be prefixed with '/questions'.
    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    # Define a simple route directly in this function for testing purposes.
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    # Return the configured Flask app instance.
    return app
