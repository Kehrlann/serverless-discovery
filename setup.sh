#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d "$SCRIPT_DIR"/venv ]; then
    virtualenv -p python3 venv
fi
source "$SCRIPT_DIR"/venv/bin/activate

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi