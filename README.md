# PYTHON TWITTER FLASK APP

A small flask app that will allow a user to login to twitter and
perform searches which will return a small sample of tweets that have been 
subject to sentiment analysis.

The user and his credentials are being saved in a postgresDB, using psycop2 to 
connect to it.

positive sentiments are marked as green
negative sentiments are marked red
neutral sentiments are marked blue

### setup

Install postgresql

change the database conection to point to your postgresql db instance
inside app.py on line 10
```
Database.initalise(<your database args>)
```

`constants.py`
```
CONSUMER_KEY = '<your twitter app consumer_key>'
CONSUMER_SECRET_KEY = '<your twitter app consumer_secret_key>'

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
```

### install requirements

```
pip install -r requirements.txt
```

### run 

```
python app.py
```

