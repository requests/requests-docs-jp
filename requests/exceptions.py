# -*- coding: utf-8 -*-

"""
requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.

"""


class RequestException(RuntimeError):
    """
    .. There was an ambiguous exception that occurred while handling your
       request.

    リクエストを処理している時に発生した不明瞭な例外がある時
    """


class HTTPError(RequestException):
    """
    .. An HTTP error occurred.

    HTTPエラーが発生した時
    """
    response = None


class ConnectionError(RequestException):
    """
    .. A Connection error occurred.

    コネクションエラーが発生した時
    """


class SSLError(ConnectionError):
    """An SSL error occurred."""


class Timeout(RequestException):
    """The request timed out."""


class URLRequired(RequestException):
    """
    .. A valid URL is required to make a request.

    リクエストを作成するために正しいURLを要求する時
    """


class TooManyRedirects(RequestException):
    """
    .. Too many redirects.

    リダイレクトの回数が多い時
    """


class MissingSchema(RequestException, ValueError):
    """The URL schema (e.g. http or https) is missing."""


class InvalidSchema(RequestException, ValueError):
    """See defaults.py for valid schemas."""


class InvalidURL(RequestException, ValueError):
    """ The URL provided was somehow invalid. """
