
# To-Do List Web Application Using Python IaC

## 1. Project Overview

This project demonstrates Infrastructure as Code (IaC) using Python to automatically set up and run a To-Do List Web Application.

The application allows users to add, complete and delete tasks.

## 2. Technologies Used

- Python
- Flask 3.1.2
- HTML and CSS
- JSON
- Git and GitHub

## 3. Prerequisites

- Python with pip and venv support
- Git
- Internet connection for dependency installation
- Permission to create files and folders
- Access to the private GitHub repository
- Available port 5000

The project was tested on Windows.

## 4. How to Run

Clone the repository:

    git clone https://github.com/aminjustpeace-design/DevOps-IaC-Project.git

Open the project folder:

    cd DevOps-IaC-Project

Run the setup script:

    python setup.py

Open the application in a web browser:

    http://127.0.0.1:5000

Press Ctrl+C in CMD to stop the application.

## 5. Infrastructure as Code Automation

The setup.py script automatically:

- Checks required project files.
- Creates or reuses the virtual environment.
- Installs and checks dependencies.
- Creates data and configuration folders.
- Generates the required JSON files.
- Starts the Flask application.

## 6. Design Decisions

- Python: Used to automate the setup process.
- Virtual environment: Prevents dependency conflicts.
- JSON: Provides simple data storage without a database server.
- Idempotency: Existing folders, configuration files and task records are preserved when the script is run again.
- Error handling: Detects missing files and failed commands.
- GitHub: Tracks source code changes and development progress.

Stop the running application before executing setup.py again.

## 7. Testing Results

| Test | Result |
|---|---|
| Application startup | Pass |
| Add tasks | Pass |
| Complete tasks | Pass |
| Delete tasks | Pass |
| JSON data storage | Pass |
| Repeated IaC execution | Pass |
| Data preservation | Pass |
| Missing file error handling | Pass |
| Fresh project deployment | Pass |

All nine planned manual tests passed.

Testing was performed locally on the same Windows laptop. 
The application is intended for local development, not production deployment.

