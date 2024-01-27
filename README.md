# Flask To-Do List

A simple To-Do List web application built using Flask, MongoDB, and Bootstrap.

## Project Overview

This project implements a basic To-Do List web application where users can add, edit, and delete tasks. The application is built using the Flask web framework, MongoDB as the database, and Bootstrap for styling.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Getting Started](#getting-started)
4. [Project Structure](#project-structure)

## Features

- Add, edit, and delete tasks.
- Mark tasks as completed.
- Responsive design using Bootstrap.

## Prerequisites

- Python 3.x
- MongoDB
- Flask
- Flask-PyMongo

## Getting Started

1. Clone the Repository:

    ```bash
    git clone https://github.com/your-username/flask-todo-list.git
    cd flask-todo-list
    ```

2. Install Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure MongoDB:

    - Make sure MongoDB is installed and running.
    - Update the MongoDB URI in `config/__init__.py`:

      ```python
      app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo'
      ```

4. Run the Application:

    ```bash
    python run.py
    ```

    The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Project Structure

```plaintext
project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
│       └── index.html
│
├── config/
│   └── __init__.py
│
└── run.py
