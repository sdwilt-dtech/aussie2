import subprocess
import sys


def run(command):
    print(f"\n>>> {command}")
    subprocess.run(command, shell=True, check=True)


def main():
    commands = {
        "test": "pytest",
        "lint": "flake8 .",
        "format": "black .",
        "check": "flake8 . && black --check . && pytest",
        "install": "python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt",
        "clean": 'find . -name "*.pyc" -delete && find . -name "__pycache__" -type d -exec rm -r {} +',
    }

    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Usage: python cli.py [install|test|lint|format|check|clean]")
        sys.exit(1)

    run(commands[sys.argv[1]])


if __name__ == "__main__":
    main()
