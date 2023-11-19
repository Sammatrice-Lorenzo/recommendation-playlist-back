FROM python:3.11.5

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY requirements.txt /app/requirements.txt
COPY . /app

# Installez les dépendances Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]