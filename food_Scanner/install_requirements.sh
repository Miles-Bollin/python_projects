#!/usr/bin/env bash

set -e

echo "Checking Python installation..."

if ! command -v python3 >/dev/null 2>&1; then
	echo "Error: Python 3 is not installed or is not in PATH."
	exit 1
fi

echo "Python found:"
python3 --version

if [ ! -f requirements.txt ]; then
	echo "Error: requirements.txt was not found."
	exit 1
fi

if [ ! -d .venv ]; then
	echo "Creating Python virtual environment..."
	python3 -m venv .venv
else
	echo "Existing .venv found."
fi

echo "Installing Python dependencies..."

.venv/bin/python -m pip install -r requirements.txt

echo "Installation complete."
echo "To activate the virtual environment, run:"
echo "source .venv/bin/activate"
