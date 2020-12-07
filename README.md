# Docker-Rest-Api

[![Python Version](https://img.shields.io/badge/python-3.8.5-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.1.4-brightgreen.svg)](https://djangoproject.com)
[![Docker Version](https://img.shields.io/badge/docker-19.03.14-brightgreen.svg)](https://docs.docker.com/engine/install/ubuntu/)

# Description

Example Restful Api with Django and Django Rest framework using Docker.

# ⚡ Used Technologies
- Django
- Django rest framework
- PostgreSQL
- Docker
- Docker-Compose

# Development & Production

```bash
docker-compose up --build -d
```
### Once the services are running, we need to create the database migrations:

```bash
docker-compose run django_rest_api python manage.py migrate
```
