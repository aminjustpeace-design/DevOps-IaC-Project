
# Infrastructure as Code (IaC) Automation Script

import sys
import subprocess
import venv
import json
import os
from pathlib import Path


# Define project paths
BASE_DIR = Path(__file__).resolve().parent

VENV_DIR = BASE_DIR / ".venv"
DATA_DIR = BASE_DIR / "data"
CONFIG_DIR = BASE_DIR / "config"

REQUIREMENTS_FILE = BASE_DIR / "requirements.txt"
APP_FILE = BASE_DIR / "app.py"

DATA_FILE = DATA_DIR / "tasks.json"
CONFIG_FILE = CONFIG_DIR / "settings.json"


# Identify Python inside the virtual environment
if os.name == "nt":
    VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe"
else:
    VENV_PYTHON = VENV_DIR / "bin" / "python"


# Check required project files
def check_requirements():
    print("\n[1/6] Checking project requirements...")

    required_files = [
        APP_FILE,
        REQUIREMENTS_FILE,
        BASE_DIR / "templates" / "index.html",
        BASE_DIR / "static" / "style.css"
    ]

    for file in required_files:
        if not file.is_file():
            raise FileNotFoundError(
                f"Required file is missing: {file}"
            )

    print("Python version:", sys.version.split()[0])
    print("All required project files are available.")


# Create virtual environment
def create_virtual_environment():
    print("\n[2/6] Checking virtual environment...")

    if VENV_PYTHON.is_file():
        print("Virtual environment already exists. Reusing it.")

    elif VENV_DIR.exists():
        raise RuntimeError(
            "Existing virtual environment is incomplete."
        )

    else:
        print("Creating virtual environment...")
        venv.EnvBuilder(with_pip=True).create(VENV_DIR)
        print("Virtual environment created successfully.")


# Install required dependencies
def install_dependencies():
    print("\n[3/6] Installing required dependencies...")

    subprocess.run(
        [
            str(VENV_PYTHON),
            "-m",
            "pip",
            "--disable-pip-version-check",
            "install",
            "-r",
            str(REQUIREMENTS_FILE)
        ],
        cwd=BASE_DIR,
        check=True
    )

    subprocess.run(
        [str(VENV_PYTHON), "-m", "pip", "check"],
        cwd=BASE_DIR,
        check=True
    )

    print("Dependencies are ready.")


# Create necessary directories
def create_directories():
    print("\n[4/6] Creating required directories...")

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    print("Data directory is ready.")
    print("Configuration directory is ready.")


# Create JSON files without overwriting existing content
def create_json_file(file_path, content):
    try:
        with file_path.open("x", encoding="utf-8") as file:
            json.dump(content, file, indent=4)

        print(f"Created: {file_path.name}")

    except FileExistsError:
        print(f"Already exists: {file_path.name}. Preserving file.")


# Generate required application files
def create_configuration_files():
    print("\n[5/6] Creating application files...")

    create_json_file(DATA_FILE, [])

    default_config = {
        "host": "127.0.0.1",
        "port": 5000
    }

    create_json_file(CONFIG_FILE, default_config)


# Start the Flask application
def start_application():
    print("\n[6/6] Starting Flask application...")

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config = json.load(file)

    print("Application URL:")
    print(f"http://{config['host']}:{config['port']}")
    print("Press Ctrl+C to stop the application.", flush=True)

    subprocess.run(
        [str(VENV_PYTHON), str(APP_FILE)],
        cwd=BASE_DIR,
        check=True
    )


# Main automation process
def main():
    print("=" * 50)
    print("INFRASTRUCTURE AS CODE AUTOMATION")
    print("To-Do List Web Application")
    print("=" * 50)

    try:
        check_requirements()
        create_virtual_environment()
        install_dependencies()
        create_directories()
        create_configuration_files()
        start_application()

    except KeyboardInterrupt:
        print("\nApplication stopped by user.")

    except subprocess.CalledProcessError as error:
        print("\nDeployment failed.")
        print("Command failed:", error)
        sys.exit(1)

    except (OSError, ValueError, RuntimeError, KeyError) as error:
        print("\nSetup error:", error)
        sys.exit(1)


# Execute automation
if __name__ == "__main__":
    main()
