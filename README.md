
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

1. Clone the repository: 
    ```bash
    git clone https://github.com/ramvilla997/flask_app.git
    ```

Certainly! Here's a concise and organized breakdown of the installation steps:

---

## Installation Guide

### **Step 1 — Installing Flask and Flask-SQLAlchemy**

#### **1.1 Setting Up the Environment**

Navigate to your `flask_app` directory and activate your virtual environment:

```bash
$ cd path/to/flask_app
$ source my_env/bin/activate
```

#### **1.2 Installing Required Packages**

With the virtual environment active, install the necessary packages using `pip`:

```bash
$ pip install Flask Flask-SQLAlchemy
```

### **Step 2 — Setting Flask Environment Variables**

#### **2.1 Specifying Application Directory**

Set the `app` package as the directory where Flask should locate the `create_app()` factory function:

```bash
$ export FLASK_APP=app
```
_Note: Typically, for single-file Flask applications, this step involves specifying a `app.py` file. However, in this structured approach, the `app` refers to the project's main directory containing the `__init__.py` file._

#### **2.2 Enabling Development Mode**

Enable the Flask development mode for a better debugging experience:

```bash
$ export FLASK_ENV=development
```

### **Step 3 — Running the Application**

To run the application, use the `flask run` command:

```bash
$ flask run
```

#### **3.1 Testing the Application**

With your development server running, open your browser and visit:

[http://127.0.0.1:5000/test/](http://127.0.0.1:5000/test/)

You should see a page with the heading: **Testing the Flask Application Factory Pattern**.

---

That's it! You've successfully set up and run your Flask application using the Application Factory Pattern.






