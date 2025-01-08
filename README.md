<img width="1070" alt="GitHub Repo Cover" src="https://github.com/corbado/corbado-php/assets/18458907/aa4f9df6-980b-4b24-bb2f-d71c0f480971">

# Python Django Passkeys Example Application

This is a sample implementation of the [Corbado passkeys-first authentication solution](https://www.corbado.com) using
Python with Django. The following packages are being used:

- [Corbado web-js](https://github.com/corbado/javascript/tree/develop/packages/web-js) 
- [Corbado Python](https://github.com/corbado/corbado-python)

## File structure

- `project`: The Django project
- `project/settings.py`: The Django settings file
- `project/context_processors.py`: The context processor that adds Corbado environment variables to the template context
- `project/middleware.py`: The middleware that adds the authenticated user to the request object
- `project/urls.py`: The Django project URL configuration
- `project/templates`: The Django project templates
- `project/templates/base.html`: The base template that acts as a layout to all other templates
- `project/utils/authentication.py`: Provides utilities for authentication state
- `main`: Our main application
- `main/models.py`: Defines our custom user model
- `main/views.py`: Contains the views for our application
- `main/urls.py`: The URL configuration for our application
- `main/decorators.py`: Decorator to force authentication on API routes
- `main/mixins.py`: Mixin to force authentication on class-based views

## Setup

### Prerequisites

Please follow the steps in [Getting started](https://docs.corbado.com/overview/getting-started) to create and configure
a project in the [Corbado developer panel](https://app.corbado.com/).

You need to have [Python](https://www.python.org/downloads/) and `pip` installed to run it.

### Configure environment variables

Use the values you obtained in [Prerequisites](#prerequisites) to configure the following variables inside a `.env`
file you create in the root folder of this project:

```sh
CORBADO_PROJECT_ID=pro-XXX
CORBADO_API_SECRET=corbado1_XXX
CORBADO_FRONTEND_API=https://${CORBADO_PROJECT_ID}.frontendapi.cloud.corbado.io
CORBADO_BACKEND_API=https://backendapi.cloud.corbado.io
```

## Usage

### Run the project locally

Run

```bash
python -m venv venv
```

to create a virtual environment.

Then, activate the virtual environment with

```bash
source venv/bin/activate
```

or

```bash
venv\Scripts\activate
```

on Windows.

To install all dependencies, run

```bash
pip install -r requirements.txt
```

Migrate your database by running 
    
```bash
python manage.py migrate
```


Now you can start the server by running 

```bash
python manage.py runserver 3000
```

## Passkeys support

- Community for Developer Support: https://bit.ly/passkeys-community
- Passkeys Debugger: https://www.passkeys-debugger.io/
- Passkey Subreddit: https://www.reddit.com/r/passkey/
