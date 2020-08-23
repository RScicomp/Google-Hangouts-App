# Google Hangouts App
Feeling lonely? Head to this app on https://hangcall.herokuapp.com/hangouts to join some google hangout rooms!

## Demo
<img src="demo hangcalls.gif"  width="1000" height="900"/>
## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/Google-Hangouts-App.git
$ cd Google-Hangouts-App

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb Google-Hangouts-App

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

