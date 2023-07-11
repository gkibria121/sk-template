@echo off
pip install -r requirements.txt

python -c "import nltk; nltk.download('words')"
