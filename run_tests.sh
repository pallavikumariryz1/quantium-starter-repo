#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Activate the virtual environment
if [ -d "venv" ]; then
    source venv/Scripts/activate
else
    echo "Virtual environment not found!"
    exit 1
fi

# Run the test suite
echo "Running test suite..."
pytest

# Capture exit code
EXIT_CODE=$?

# Return proper exit status
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
