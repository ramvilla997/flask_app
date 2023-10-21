
# Flask Application Structure Tutorial

This repository contains a structured Flask application that utilizes Flask Blueprints and Flask-SQLAlchemy to organize and manage a large-scale Flask web application.

## Overview

Flask offers flexibility to grow from a small to large application. For better manageability, it's advisable to break down the application into organized components. This repository demonstrates how to effectively utilize Flask Blueprints to achieve this modular architecture. 

The application consists of three main components:

1. **Main Blueprint**: Contains the home page and primary routes.
2. **Posts Blueprint**: For managing blog posts.
3. **Questions Blueprint**: Deals with questions and answers.

## Project Structure

```
.
└── flask_app
    ├── app
    │   ├── extensions.py
    │   ├── __init__.py
    │   ├── main
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── models
    │   │   ├── post.py
    │   │   └── question.py
    │   ├── posts
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── questions
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   └── templates
    │       ├── base.html
    │       ├── index.html
    │       ├── posts
    │       │   ├── categories.html
    │       │   └── index.html
    │       └── questions
    │           └── index.html
    ├── app.db
    └── config.py
```

## Prerequisites

- Python 3 local environment. Follow [this guide](URL_HERE) to set it up.
- Basic understanding of Flask concepts like routes, view functions, and templates. Check out the [basic Flask tutorial](URL_HERE).
- Basic knowledge of HTML. Review the [HTML tutorial series](URL_HERE).
- Familiarity with Flask-SQLAlchemy concepts. See the [Flask-SQLAlchemy guide](URL_HERE).

## Setup & Run

1. Clone the repository: 
    ```bash
    git clone https://github.com/ramvilla997/flask_app.git
    ```

2. Navigate to the project directory:
    ```bash
    cd flask_app
    ```

3. Install the required dependencies (preferably in a virtual environment):
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python run.py
    ```

Visit `http://localhost:5000` in your browser to access the application.

## Contribution

Feel free to raise issues, provide feedback, or contribute to the project. We appreciate your input!

---

You can now place this `README.md` in the root of your `flask_app` directory. Make sure to replace the `URL_HERE` placeholders with actual URLs where needed.




