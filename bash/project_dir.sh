mkdir -p src/utils src/config
mkdir -p data/raw data/clean
mkdir -p notebooks

touch src/main.py src/config/config.py
touch .env

wget https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore