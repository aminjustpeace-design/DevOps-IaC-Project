
# Automated Deployment of a To-Do List Web Application Using Python IaC

## 1. Project Overview

This project was developed for ITNB4624 - Cloud Computing with DevOps.

The project demonstrates Infrastructure as Code (IaC) using Python to automate the deployment of a simple To-Do List Web Application developed using Flask.

The automation script prepares the application environment, installs dependencies, creates the required directories and configuration files, and starts the application automatically.

## 2. Project Objectives

- Automate the application deployment process.
- Reduce manual installation and configuration.
- Ensure consistent and repeatable deployment.
- Preserve existing application data during repeated execution.
- Implement version control using Git and GitHub.

## 3. Application Features

- Add new tasks.
- Display existing tasks.
- Mark tasks as completed.
- Delete tasks.
- Display total, completed and pending tasks.
- Store task records in a JSON file.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development and IaC |
| Flask 3.1.2 | Web application framework |
| HTML | Web interface |
| CSS | Interface styling |
| JSON | Data storage and configuration |
| Python venv | Virtual environment |
| Python subprocess | Automated command execution |
| Git | Version control |
| GitHub | Source code repository |

## 5. Prerequisites

Before running the project, ensure the following:

- Python 3 with pip and venv support is installed.
- Git is installed for cloning the repository.
- Internet access is available for initial dependency installation.
- Permission to create files and directories in the project folder.
- Port 5000 is available.
- Access to the private GitHub repository has been granted.

The project was tested on Windows using Python 3.15.2.

Visual Studio Code is optional for editing the source code.

## 6. Installation and Deployment

### Step 1: Clone the repository

    git clone https://github.com/aminjustpeace-design/DevOps-IaC-Project.git

### Step 2: Enter the project directory

    cd DevOps-IaC-Project

### Step 3: Run the IaC script

    python setup.py

The script automatically prepares the environment and starts the application.

Manual Flask installation and virtual environment activation are not required.

### Step 4: Access the application

Open a web browser and navigate to:

http://127.0.0.1:5000

### Step 5: Stop the application

Press Ctrl+C in the terminal.

## 7. Infrastructure as Code Workflow

The setup.py script performs the following operations:

1. Checks that all required project files exist.
2. Creates or reuses a Python virtual environment.
3. Installs and validates the required dependencies.
4. Creates the data and configuration directories.
5. Generates the required JSON files.
6. Starts the Flask web application automatically.

## 8. Project Structure

    DevOps-IaC-Project/
    |-- app.py
    |-- setup.py
    |-- requirements.txt
    |-- README.md
    |-- .gitignore
    |-- templates/
    |   |-- index.html
    |-- static/
    |   |-- style.css
    |-- .venv/
    |-- data/
    |   |-- tasks.json
    |-- config/
        |-- settings.json

The .venv, data and config directories are generated automatically by the IaC script and excluded from version control.

## 9. Design Decisions

### Python-Based Automation

Python was selected because its standard libraries provide file management, virtual environment creation and command execution without requiring additional infrastructure management tools.

### Virtual Environment

A virtual environment isolates the application's dependencies from other Python projects and reduces dependency conflicts.

### Dependency Management

The Flask version is specified in requirements.txt to improve deployment consistency.

### Idempotency

The script checks for an existing virtual environment and preserves existing JSON files. Directory creation uses exist_ok=True to prevent errors when directories already exist.

The running application should be stopped before executing the script again.

### JSON Storage

JSON was selected because the application is small and does not require a separate database server.

### Error Handling

The script handles missing project files, failed subprocess commands and other setup errors. Deployment stops when an error is detected.

### Version Control

Git and GitHub are used to track changes and maintain the project source code.

## 10. Testing Results

The following manual tests were performed:

| Test ID | Test Description | Actual Result | Status |
|---|---|---|---|
| TC01 | Application startup | Application successfully launched | Pass |
| TC02 | Add tasks | Three tasks added successfully | Pass |
| TC03 | Complete task | Completion status updated correctly | Pass |
| TC04 | Delete task | Selected task removed successfully | Pass |
| TC05 | JSON data storage | Two remaining records stored correctly | Pass |
| TC06 | Repeated IaC execution | Existing resources reused | Pass |
| TC07 | Data preservation | Existing tasks retained after restart | Pass |
| TC08 | Error handling | Missing requirements file detected | Pass |
| TC09 | Clean environment deployment | Application deployed successfully in a separate project folder | Pass |

Total tests: 9
Passed: 9
Failed: 0

All nine planned manual test scenarios passed.

## 11. Troubleshooting

### Missing requirements.txt

Ensure that all project source files are available in the project directory.

### Dependency installation failure

Check the internet connection and Python installation before running setup.py again.

### Port 5000 already in use

Stop the existing application instance before starting another deployment.

### Incomplete virtual environment

Stop the application, remove only the incomplete .venv directory, and execute setup.py again.

## 12. Project Limitations

- The application uses a local Flask development server.
- Python must be installed before executing the automation script.
- Initial dependency installation may require internet access.
- Deployment was tested on Windows.
- Clean deployment testing was performed using a separate cloned project folder on the same machine.
- Concurrent deployment executions have not been tested.
- Transitive dependency versions are not fully pinned.

## 13. Repository

https://github.com/aminjustpeace-design/DevOps-IaC-Project

## 14. Course Information

Course: Cloud Computing with DevOps

Course Code: ITNB4624

Assessment: Group Assignment (40%)

Topic: Infrastructure as Code with Python
