# Fibonacci Lab

A simple browser frontend for the supplied `FIBB.py` Fibonacci project. Python calculates the sequence; the browser displays the result.

## Run locally

1. Install Python 3.9 or newer.
2. Open a terminal in this folder.
3. Run `python app.py` (on some systems, use `python3 app.py`).
4. Open **http://127.0.0.1:8000** in your browser.
5. Press `Ctrl+C` in the terminal to stop the server.

No packages or build steps are needed. Iterative mode supports 1–100 terms; recursive mode supports 1–30 terms because the original pure recursion becomes slow with larger inputs.

**Files:** `FIBB.py` contains the original algorithm, `app.py` serves the page and API, and `index.html` contains the interface.

GitHub Pages can host only the HTML portion; it cannot execute this Python backend. Run locally or deploy to a Python capable host for the working API.
