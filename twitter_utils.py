import constants
import oauth2
import urllib.parse as urlparse

consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET_KEY)


def get_request_token():
    client = oauth2.Client(consumer)
    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
        print("An Error ocurred getting the request token from twitter!")
    return dict(urlparse.parse_qsl(content.decode('utf-8')))


def get_oauth_verifier(request_token):
    print("Go to the following site")
    print(get_oauth_verifier_url(request_token))
    return input("What is the pin?: ")


def get_oauth_verifier_url(request_token):
    return f"{constants.AUTHORIZATION_URL}?oauth_token={request_token['oauth_token']}"


def get_access_token(request_token, oauth_verifier):
    token = oauth2.Token(request_token['oauth_token'], request_token["oauth_token_secret"])
    token.set_verifier(oauth_verifier)
    client = oauth2.Client(consumer, token)
    response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
    return dict(urlparse.parse_qsl(content.decode('utf-8')))
