## Project Flask Dream-Team
### An employee management web app.<br>
This project was bootstrapped with:

- [Pipenv](https://pipenv.readthedocs.io/en/latest/) with latest Python 3.7
- Flask 1.0.2
- Flask-Bootstrap 3.3.7.1
- Flask-Login 0.4.1
- Flask-Migrate 2.3.0
- Flask-SQLAlchemy 2.3.2
- Flask-WTF 0.14.2

### Run Demo

Setup PostgreSQL in **instance/config.py**.<br>

```python
SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgresuser:postgrespassword@localhost/dreamteam_db'
```

```bash
$ pipenv shell
$ export FLASK_CONFIG=development
$ export FLASK_APP=run.py
$ flask run
```

Runs the app in the development mode.<br>
Open [http://localhost:5000](http://localhost:5000) to view it in the browser.

![screenshot 1](screenshots/flask1.png)
![screenshot 2](screenshots/flask2.png)
![screenshot 3](screenshots/flask3.png)
![screenshot 4](screenshots/flask4.png)

#### Improvements

- This boilerplate code used extensively new python package manager **Pipenv**. Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important Pipfile.lock, which is used to produce **deterministic builds**.

:point_right: https://pipenv.readthedocs.io/en/latest/

### TODO

Still in alpha-development, needed to enhance this app with Docker container for production ready.
