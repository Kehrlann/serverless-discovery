#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"


source ${SCRIPT_DIR}/venv/bin/activate
cd ${SCRIPT_DIR}
find . -name "*.py" | entr python -m unittest