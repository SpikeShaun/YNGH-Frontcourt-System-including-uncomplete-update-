@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting Flask application...
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host=0.0.0.0 --port=8000
