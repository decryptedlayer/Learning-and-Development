from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session
from flask.json import jsonify
import os


class OAuthPY:

    def __init__(self):
        client_key = ''
        client_secret = ''
        oauth_base_url = 'https://github.com/login/oauth/authorize'
        token_url = 'https://github.com/login/oauth/access_token'
        secret_key = os.urandom(24)

        app = Flask(__name__)
        app.config['SECRET_KEY'] = secret_key

    def main(self):
        print("hello world")


if __name__ == '__main__':
    oa = OAuthPY()
    oa.main()
