# Weather API

## Cloning repository

1. Type `git clone` to clone this repository.

```bash
git clone git@github.com:jllemus/weather-project.git
```
2. Change directory into weather-project folder.

```bash
cd weather-project
```
## Setup

1. Install [Docker engine](https://pip.pypa.io/en/stable/) and [Docker compose](https://docs.docker.com/compose/install/) in your system.

2. Add the environment variables file `.env` in the root folder and change its content using the following commands:

```bash
touch .env
echo "API_URL=http://api.openweathermap.org/data/2.5/weather" >> .env
echo "API_KEY=<your_api_key>" >> .env
```
- Note: Don't forget to replace <your_api_key> with the correct appkey otherwise you will get an 401 unauthorized HTTP response.

## Running server

1. Run project migrations

```bash
docker-compose run django python manage.py migrate && docker-compose down
```

2. In Linux run the following command in the root of the project:

```bash
docker-compose up --build
```

## Testing Code

Run the following comand to execute django tests:
```bash
docker-compose run django python manage.py test && docker-compose down
```

## Usage

Use cURL to get data from API:
```bash
curl -X GET "http://localhost:8000/weather/?country=co&city=Bogota"
```