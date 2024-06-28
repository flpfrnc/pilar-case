FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

# set the working directory in the container
WORKDIR /app

# copy requirements into the container
COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy the rest of the app into the container
COPY . .

COPY ./entrypoint.sh /entrypoint.sh

# grants executable permission to the entrypoint cmd file
RUN chmod +x /entrypoint.sh

# run the application
ENTRYPOINT ["/entrypoint.sh"]