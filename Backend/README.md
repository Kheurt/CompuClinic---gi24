# Compuclinic API

## Summary
An API built with `Django Rest Framework` to manage a Healthcare Structure.

It includes: 
  - A package for managing consultations, payment and Medical FIle operations ( Creation, modification, ...)
  - A package for managing the human ressources, the infrastructures and the different services of a Healthcare Structure.
  - A package for managing authentication and authorizations...

## Getting Started
You need to have `Python v3.9` installed.

After cloning the repo, the first thing to do is to create a virtual environment, an activate it to use it:
```
# On Linux-like OS

python3 -m venv env
. env/bin/active
```

After creating a virtual environment, you need to download all the dependecies of the project, by doing :
```
pip install -r requirements.txt
```

When you are done with the installations of the dependencies, you need to migrate the database : 

```
python3 manage.py makemigrations
python3 manage.py migrate
```

You can then launch the server with

```
python manage.py runserver
```
