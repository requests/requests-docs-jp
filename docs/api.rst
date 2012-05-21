.. _api:

API
===

.. module:: requests

.. This part of the documentation covers all the interfaces of Requests.  For
   parts where Requests depends on external libraries, we document the most
   important right here and provide links to the canonical documentation.

ドキュメントのこの章は、Requestsのインターフェースを全てカバーしています。 
Requestsが外部ライブラリに依存している部分については、大事な部分だけをここでは取り上げ、
その他はドキュメントのリンクを載せます。

.. Main Interface
   --------------

メインのインターフェース
------------------------------

.. All of Request's functionality can be accessed by these 7 methods.
   They all return an instance of the :class:`Response <Response>` object.

Requestの機能の全ては、以下の7つのメソッドを使ってアクセスできます。
これらは全て :class:`Response <Response>` オブジェクトのインスタンスを返します。

.. autofunction:: request

---------------------


.. autoclass:: Response
   :inherited-members:

---------------------

.. autofunction:: head
.. autofunction:: get
.. autofunction:: post
.. autofunction:: put
.. autofunction:: patch
.. autofunction:: delete


-----------------

.. autofunction:: session

例外
~~~~~~~~~~

.. Exceptions
   ~~~~~~~~~~

.. module:: requests

.. autoexception:: RequestException
.. autoexception:: ConnectionError
.. autoexception:: HTTPError
.. autoexception:: URLRequired
.. autoexception:: TooManyRedirects


.. _configurations:

.. Configurations
   --------------

コンフィグレーション
----------------------------

.. automodule:: requests.defaults


.. _async:

Async
-----

.. module:: requests.async


.. autofunction:: map
.. autofunction:: request
.. autofunction:: head
.. autofunction:: get
.. autofunction:: post
.. autofunction:: put
.. autofunction:: patch
.. autofunction:: delete



.. Utilities
   ---------

ユーティリティ
------------------

.. These functions are used internally, but may be useful outside of
   Requests.

これらの関数は内部で使われていますが、Requests以外で使う場合も便利かもしれません。

.. module:: requests.utils

Status Code Lookup
~~~~~~~~~~~~~~~~~~

.. autofunction:: requests.codes

::

    >>> requests.codes['temporary_redirect']
    307

    >>> requests.codes.teapot
    418

    >>> requests.codes['\o/']
    200

.. Cookies
   ~~~~~~~

クッキー
~~~~~~~~~~~~~~

.. autofunction:: dict_from_cookiejar
.. autofunction:: cookiejar_from_dict
.. autofunction:: add_dict_to_cookiejar


.. Encodings
   ~~~~~~~~~

エンコード
~~~~~~~~~~~~~~

.. autofunction:: get_encodings_from_content
.. autofunction:: get_encoding_from_headers
.. autofunction:: get_unicode_from_response
.. autofunction:: decode_gzip


Internals
---------

These items are an internal component to Requests, and should never be
seen by the end user (developer). This part of the API documentation
exists for those who are extending the functionality of Requests.


Classes
~~~~~~~

.. autoclass:: requests.Response
   :inherited-members:

.. autoclass:: requests.Request
   :inherited-members:

.. _sessionapi:

.. autoclass:: requests.Session
   :inherited-members:

