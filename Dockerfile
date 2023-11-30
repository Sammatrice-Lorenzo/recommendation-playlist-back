FROM python:3.11.5

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Permet de lancer le container sans un fichier de demmarage
# CMD ["tail", "-f", "/dev/null"]
ENTRYPOINT ["python", "__init__.py"]
