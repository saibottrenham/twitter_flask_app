from user import User
from database import Database
from twitter_utils import get_request_token, \
    get_oauth_verifier, get_access_token

Database.initalise(user="tobiasmahnert", database="test")

email = input("Enter your email: ")
user = User.load_from_db_by_email(email)

if not user:
    request_token = get_request_token()
    oauth_verifier = get_oauth_verifier(request_token)
    access_token = get_access_token(request_token, oauth_verifier)

    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")

    user = User(email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
    user.save_to_db()

for tweet in user.twitter_request(
        'https://api.twitter.com/1.1/search/tweets.json?q=boobs+filter:images',
        'GET'
    )['statuses']:
    print(tweet['text'])

