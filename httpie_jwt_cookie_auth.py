"""
JWT Cookie Auth plugin for HTTPie.

"""
import jwt

from httpie.plugins import AuthPlugin
from httpie.context import Environment

try:
    import urlparse
except ImportError:
    import urllib.parse

__version__ = '0.1.0'
__author__ = 'Nick Satterly'
__licence__ = 'MIT'


class JwtCookieAuth:

    def __init__(self, jwt_token, jwt_secret):

        self.jwt_token = jwt_token

        if jwt_secret == '':
            self.jwt_secret = None
            self.jwt_verify = False
        else:
            self.jwt_secret = jwt_secret
            self.jwt_verify = True

        config = Environment().config
        self.jwt_cookie = config.get('jwt_cookie_name', 'access_token')
        self.jwt_xsrf = config.get('jwt_xsrf_header', 'X-XSRF-TOKEN')

    def __call__(self, r):

        try:
            payload = jwt.decode(self.jwt_token, key=self.jwt_secret, verify=self.jwt_verify)
        except jwt.exceptions.DecodeError:
            raise ValueError("JWT could not be decoded")
        xsrf_token = payload.get('xsrfToken')

        if xsrf_token:
            r.headers[self.jwt_xsrf] = xsrf_token

        r.headers['Cookie'] = self.jwt_cookie + '=' + self.jwt_token

        return r


class JwtCookieAuthPlugin(AuthPlugin):

    name = 'JWT cookie auth'
    auth_type = 'jwt-cookie'
    description = 'Put JWT token in a cookie and copy xsrfToken value to headers'

    def get_auth(self, jwt_token, jwt_secret):
        return JwtCookieAuth(jwt_token, jwt_secret)
