.. _quickstart:

クイックスタート
=====================

.. Quickstart
   ==========

.. module:: requests.models

.. Eager to get started? This page gives a good introduction in how to get started
   with Requests. This assumes you already have Requests installed. If you do not,
   head over to the :ref:`Installation <install>` section.

はじめましょうか?
このページはRequestsを使い方の紹介をします。ここではRequestsはインストールされているものとします。
まだの場合は、 :ref:`Installation <install>` の章を見て下さい。

.. First, make sure that:

最初に、以下を確認して下さい。 :

.. Requests is :ref:`installed <install>`
.. Requests is :ref:`up-to-date <updates>`

* Requestsが :ref:`インストールされている <install>`
* Requestsを :ref:`最新版にアップデートしている <updates>`

.. Let's get started with some simple examples.

いくつかの簡単な例をやってみましょう。

.. Make a Request
   ------------------

リクエストの生成
---------------------

.. Making a request with Requests is very simple.

Requestsを使ってリクエストを生成することはとても簡単です。

.. Begin by importing the Requests module::

Requestsモジュールをインポートすることから始めます。 ::

    >>> import requests

.. Now, let's try to get a webpage. For this example, let's get GitHub's public
   timeline ::

ではウェブページを取得してみましょう。
今回の例では、GitHubのパブリックなタイムラインを取得してみましょう。 ::

    >>> r = requests.get('https://github.com/timeline.json')

.. Now, we have a :class:`Response` object called ``r``. We can get all the
   information we need from this object.

現在、 ``r`` と呼ばれる :class:`Response` オブジェクトがあります。
これから必要な情報を全て取得することができます。

.. Requests' simple API means that all forms of HTTP request are as obvious. For
   example, this is how you make an HTTP POST request::

RequestsのシンプルなAPIは、HTTPリクエストの全てのフォームデータであることがわかります。
例えば、以下の例はHTTPのPOSTリクエストをどうやって作成するかを示しています。 ::

    >>> r = requests.post("http://httpbin.org/post")

.. Nice, right? What about the other HTTP request types: PUT, DELETE, HEAD and
   OPTIONS? These are all just as simple::

いいでしょ?
PUT、DELETE、HEAD、OPTIONSなどの他のHTTPリクエストについてもとてもシンプルです。 ::

    >>> r = requests.put("http://httpbin.org/put")
    >>> r = requests.delete("http://httpbin.org/delete")
    >>> r = requests.head("http://httpbin.org/get")
    >>> r = requests.options("http://httpbin.org/get")

.. That's all well and good, but it's also only the start of what Requests can
   do.

以上が全てですが、Requestsができることのさわりしか見ていません。

.. Passing Parameters In URLs
   --------------------------

URLにパラメーターを渡す
-----------------------------

.. You often want to send some sort of data in the URL's query string. If
   you were constructing the URL by hand, this data would be given as key/value
   pairs in the URL after a question mark, e.g. ``httpbin.org/get?key=val``.
   Requests allows you to provide these arguments as a dictionary, using the
   ``params`` keyword argument. As an example, if you wanted to pass
   ``key1=value1`` and ``key2=value2`` to ``httpbin.org/get``, you would use the
   following code::

しばしばURLのクエリ文字列にある種のデータを追加して送信したい時があるかもしれません。
手動でURLを作成する場合、このデータはクエスション記号の後のURLにキー/バリューのペアで与えて下さい。
例: ``httpbin.org/get?key=val`` 。
Requestsは、 ``params`` キーワード引数を使ってこれらの引数を辞書として渡すことができます。
例として、 ``key1=value1`` と ``key2=value2`` を ``httpbin.org/get`` に渡したい場合、
以下のコードでできます。 ::

    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.get("http://httpbin.org/get", params=payload)

.. You can see that the URL has been correctly encoded by printing the URL::

URLを表示して、URLが正しくエンコードされたか見ることができます。 ::

    >>> print r.url
    u'http://httpbin.org/get?key2=value2&key1=value1'


.. Response Content
   ----------------

レスポンスの内容
-------------------

.. We can read the content of the server's response. Consider the GitHub timeline
   again::

サーバーのレスポンスの内容を見ることができます。 ::

    >>> import requests
    >>> r = requests.get('https://github.com/timeline.json')
    >>> r.text
    '[{"repository":{"open_issues":0,"url":"https://github.com/...

.. Requests will automatically decode content from the server. Most unicode
   charsets are seamlessly decoded.

Requestsはサーバーからの内容を自動的にデコードします。
ほとんどのユニコード文字はシームレスにデコードされます。

.. When you make a request, Requests makes educated guesses about the encoding of
   the response based on the HTTP headers. The text encoding guessed by Requests
   is used when you access ``r.text``. You can find out what encoding Requests is
   using, and change it, using the ``r.encoding`` property::

リクエストを作成した時、RequestsはHTTPヘッダーに基づいたレスポンスのエンコーディングについて推測する
``r.text`` にアクセスした時に、Requestsで使われているテキストのエンコーディングは推測されます。
Requestsで使われているエンコーディングは調べることができ、 ``r.encoding`` プロパティを使って変更することができます。

    >>> r.encoding
    'utf-8'
    >>> r.encoding = 'ISO-8859-1'

.. If you change the encoding, Requests will use the new value of ``r.encoding``
   whenever you call ``r.text``.

エンコーディングを変更した場合、Requestsは

.. Requests will also use custom encodings in the event that you need them. If
   you have created your own encoding and registered it with the ``codecs``
   module, you can simply use the codec name as the value of ``r.encoding`` and
   Requests will handle the decoding for you.

Requests

.. Binary Response Content
   -----------------------

バイナリのレスポンスの本文
---------------------------------

.. You can also access the response body as bytes, for non-text requests::

テキスト以外のリクエストに、バイトとしてレスポンスボディにアクセスできます。 ::

    >>> r.content
    b'[{"repository":{"open_issues":0,"url":"https://github.com/...

.. The ``gzip`` and ``deflate`` transfer-encodings are automatically decoded for you.

``gzip`` や ``deflate`` のようなTransfer-Encodingは自動的にデコードされます。

.. For example, to create an image from binary data returned by a request, you can
   use the following code:

リクエストによって返されたバイナリデータから画像を作成する例として、以下のようなコードになります。 :

    >>> from PIL import Image
    >>> from StringIO import StringIO
    >>> i = Image.open(StringIO(r.content))


.. JSON Response Content
   ---------------------

JSONのレスポンスの内容
------------------------

.. There's also a builtin JSON decoder, in case you're dealing with JSON data::

JSONデータを扱う場合に、JSONをデコードする機能もあります。 ::

    >>> import requests
    >>> r = requests.get('https://github.com/timeline.json')
    >>> r.json
    [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...

.. In case the JSON decoding fails, ``r.json`` simply returns ``None``.

JSONのデコードに失敗した場合、 ``r.json`` は単純に ``None`` を返します。


.. Raw Response Content
   --------------------

生のレスポンスの内容
-----------------------

.. In the rare case that you'd like to get the absolute raw socket response from the server,
   you can access ``r.raw``::

サーバーからの生のソケットレスポンスの全てを取得したい稀なケースでは、 ``r.raw`` にアクセスできます。 ::

    >>> r.raw
    <requests.packages.urllib3.response.HTTPResponse object at 0x101194810>

    >>> r.raw.read(10)
    '\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'


.. Custom Headers
   --------------

カスタムヘッダー
---------------------

.. If you'd like to add HTTP headers to a request, simply pass in a ``dict`` to the
   ``headers`` parameter.

リクエストにHTTPヘッダーを追加したい場合、 ``headers`` パラメーターに  ``dict`` を渡すだけです。

.. For example, we didn't specify our content-type in the previous example::

例えば、前の例のようにコンテントタイプを指定する必要はありません。 ::

    >>> import json
    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}
    >>> headers = {'content-type': 'application/json'}

    >>> r = requests.post(url, data=json.dumps(payload), headers=headers)


.. More complicated POST requests
   ------------------------------

さらに複雑なPOSTリクエスト
---------------------------------

.. Typically, you want to send some form-encoded data — much like an HTML form.
   To do this, simply pass a dictionary to the `data` argument. Your
   dictionary of data will automatically be form-encoded when the request is made::

一般的にHTMLのフォームのようにエンコードしたデータを送信したい場合、
これをするのは簡単で、 `data` 引数に辞書を渡すだけです。
データの辞書はリクエストを生成する時に自動的にエンコードされます。

    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.post("http://httpbin.org/post", data=payload)
    >>> print r.text
    {
      // ...snip... //
      "form": {
        "key2": "value2",
        "key1": "value1"
      },
      // ...snip... //
    }

.. There are many times that you want to send data that is not form-encoded. If you pass in a ``string`` instead of a ``dict``, that data will be posted directly.

エンコードされていないデータを送りたい場合が何度もあると思います。
``dict`` の代わりに ``string`` を渡した場合、データは直接送信されます。

.. For example, the GitHub API v3 accepts JSON-Encoded POST/PATCH data::

例えば、GitHubのAPI v3はJSONエンコードされたPOST/PATCHデータを受け取ります。 ::

    >>> import json
    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}

    >>> r = requests.post(url, data=json.dumps(payload))


.. POST a Multipart-Encoded File
   -----------------------------

マルチパートでエンコードされたファイルのPOST
---------------------------------------------------

.. Requests makes it simple to upload Multipart-encoded files::

RequestsはMultipartエンコードのファイルをアップロードすることが簡単にできます。 ::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': open('report.xls', 'rb')}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      // ...snip... //
      "files": {
        "file": "<censored...binary...data>"
      },
      // ...snip... //
    }

.. You can set the filename explicitly::

ファイル名を明示的に指定して下さい。 ::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': ('report.xls', open('report.xls', 'rb'))}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      // ...snip... //
      "files": {
        "file": "<censored...binary...data>"
      },
      // ...snip... //
    }

.. If you want, you can send strings to be received as files::

ファイルとして受け取りたい場合に文字列を送信することができます。 ::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      // ...snip... //
      "files": {
        "file": "some,data,to,send\\nanother,row,to,send\\n"
      },
      // ...snip... //
    }

.. Setting filename explicitly::

ファイル名を明示的に指定して下さい。 ::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': ('report.xls', open('report.xls', 'rb'))}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      "origin": "179.13.100.4",
      "files": {
        "file": "<censored...binary...data>"
      },
      "form": {},
      "url": "http://httpbin.org/post",
      "args": {},
      "headers": {
        "Content-Length": "3196",
        "Accept-Encoding": "identity, deflate, compress, gzip",
        "Accept": "*/*",
        "User-Agent": "python-requests/0.8.0",
        "Host": "httpbin.org:80",
        "Content-Type": "multipart/form-data; boundary=127.0.0.1.502.21746.1321131593.786.1"
      },
      "data": ""
    }

.. Sending strings to be received as files::

ファイルとして受け取る文字列の送信 ::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      "origin": "179.13.100.4",
      "files": {
        "file": "some,data,to,send\\nanother,row,to,send\\n"
      },
      "form": {},
      "url": "http://httpbin.org/post",
      "args": {},
      "headers": {
        "Content-Length": "216",
        "Accept-Encoding": "identity, deflate, compress, gzip",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "python-requests/0.11.1",
        "Host": "httpbin.org",
        "Content-Type": "multipart/form-data; boundary=127.0.0.1.502.41433.1335385481.788.1"
      },
      "json": null,
      "data": ""
    }


.. Response Status Codes
   ---------------------

レスポンスステータスコード
--------------------------------

.. We can check the response status code::

レスポンスのステータスコードを確認することができます。 ::

    >>> r = requests.get('http://httpbin.org/get')
    >>> r.status_code
    200

.. Requests also comes with a built-in status code lookup object for easy
   reference::

Requestsは簡単に参照できるように、組み込みのステータスコードのルックアップオブジェクト
があります。 ::

    >>> r.status_code == requests.codes.ok
    True

.. If we made a bad request (non-200 response), we can raise it with
   :class:`Response.raise_for_status()`::

不正なリクエスト(200以外のレスポンス)を作りたい場合は、
:class:`Response.raise_for_status()` で例外を発生させることができます。 ::

    >>> _r = requests.get('http://httpbin.org/status/404')
    >>> _r.status_code
    404

    >>> _r.raise_for_status()
    Traceback (most recent call last):
      File "requests/models.py", line 832, in raise_for_status
        raise http_error
    requests.exceptions.HTTPError: 404 Client Error

.. But, since our ``status_code`` for ``r`` was ``200``, when we call
   ``raise_for_status()`` we get::

しかし呼び出した時は、 ``status_code`` が ``200`` だったので ::

    >>> r.raise_for_status()
    None

.. All is well.

全て上手くいきました。


.. Response Headers
   ----------------

レスポンスヘッダー
-----------------------

.. We can view the server's response headers using a Python dictionary::

Pythonの辞書形式で簡単にサーバーのレスポンスヘッダーを見ることができます。 ::

    >>> r.headers
    {
        'status': '200 OK',
        'content-encoding': 'gzip',
        'transfer-encoding': 'chunked',
        'connection': 'close',
        'server': 'nginx/1.0.4',
        'x-runtime': '148ms',
        'etag': '"e1ca502697e5c9317743dc078f67693f"',
        'content-type': 'application/json; charset=utf-8'
    }

.. The dictionary is special, though: it's made just for HTTP headers. According to
   `RFC 2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`_, HTTP
   Headers are case-insensitive.

辞書とはいえ、特別です。辞書はHTTPヘッダーを作成するためだけに作られます。
`RFC 2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`_ によると、HTTPヘッダーは大文字と小文字を区別しません。

.. So, we can access the headers using any capitalization we want::

そこで、任意の大文字と小文字を使用してヘッダーにアクセスできます。 ::

    >>> r.headers['Content-Type']
    'application/json; charset=utf-8'

    >>> r.headers.get('content-type')
    'application/json; charset=utf-8'

.. If a header doesn't exist in the Response, its value defaults to ``None``::

レスポンスにはないヘッダーを参照すると、値はデフォルトの ``None`` になります。

    >>> r.headers['X-Random']
    None


.. Cookies
   -------

クッキー
-------------

.. If a response contains some Cookies, you can get quick access to them::

レスポンスにクッキーが含まれているなら、簡単にアクセスして取得することができます。 ::

    >>> url = 'http://httpbin.org/cookies/set/requests-is/awesome'
    >>> r = requests.get(url)

    >>> print r.cookies
    {'requests-is': 'awesome'}

.. To send your own cookies to the server, you can use the ``cookies``
   parameter::

サーバーにクッキーを送信するには、 ``cookies`` パラメーターを使うことができます。 ::

    >>> url = 'http://httpbin.org/cookies'
    >>> cookies = dict(cookies_are='working')

    >>> r = requests.get(url, cookies=cookies)
    >>> r.text
    '{"cookies": {"cookies_are": "working"}}'


.. Basic Authentication
   --------------------

ベーシック認証
-----------------

.. Many web services require authentication. There many different types of
   authentication, but the most common is HTTP Basic Auth.

ほとんどのウェブサービスは認証システムが必要です。
認証には様々な種類がありますが、最も一般的なのはHTTPベーシック認証です。

.. Making requests with Basic Auth is extremely simple::

ベーシック認証を使ったリクエストを作成することはとても簡単です。 ::

    >>> from requests.auth import HTTPBasicAuth
    >>> requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
    <Response [200]>

.. Due to the prevalence of HTTP Basic Auth, requests provides a shorthand for
   this authentication method::

HTTPベーシック認証の
Requestsはこの認証を手動で行うためのメソッドがあります。

    >>> requests.get('https://api.github.com/user', auth=('user', 'pass'))
    <Response [200]>

.. Providing the credentials as a tuple in this fashion is functionally equivalent
   to the ``HTTPBasicAuth`` example above.

この方法で、タプルとして認証情報を与えることは、上記の ``HTTPBasicAuth`` の例と機能的には同等です。

.. Digest Authentication
   ---------------------

ダイジェスト認証
--------------------

.. Another popular form of web service protection is Digest Authentication::

他の人気があるウェブサービスの認証システムはダイジェスト認証です。 ::

    >>> from requests.auth import HTTPDigestAuth
    >>> url = 'http://httpbin.org/digest-auth/auth/user/pass'
    >>> requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
    <Response [200]>


.. OAuth Authentication
   --------------------

OAuth認証
--------------

.. Miguel Araujo's `requests-oauth <http://pypi.python.org/pypi/requests-oauth>`_
   project provides a simple interface for establishing OAuth connections.
   Documentation and examples can be found on the requests-oauth
   `git repository <https://github.com/maraujop/requests-oauth>`_.

Miguel Araujoの `requests-oauth <http://pypi.python.org/pypi/requests-oauth>`_ プロジェクトは
OAuth接続を確立するための簡単なインターフェースを提供しています。
ドキュメントとサンプルは、requests-oauthの `git repository <https://github.com/maraujop/requests-oauth>`_ にあります。

.. Redirection and History
   -----------------------

リダイレクトとヒストリー
------------------------------

.. Requests will automatically perform location redirection while using the GET
   and OPTIONS verbs.

Requestsは、冪等メソッドを使っている時に自動的にリダイレクトを行います。

.. GitHub redirects all HTTP requests to HTTPS. We can use the ``history`` method
   of the Response object to track redirection. Let's see what Github does::

GitHubは全てのHTTPリクエストをHTTPSにリダイレクトします。何が起こるか見てみましょう ::

    >>> r = requests.get('http://github.com')
    >>> r.url
    'https://github.com/'
    >>> r.status_code
    200
    >>> r.history
    [<Response [301]>]

.. The :class:`Response.history` list contains a list of the
   :class:`Request` objects that were created in order to complete the request. The list is sorted from the oldest to the most recent request.

:class:`Response.history` は、
リクエストが完了したときに作られる :class:`Request` オブジェクトがリストとして入っています。
リストはリクエストの古いものから最も新しいものの順に並べ替えられます。

.. If you're using GET, HEAD, or OPTIONS, you can disable redirection
   handling with the ``allow_redirects`` parameter::

GET、HEAD、OPTIONSを使う場合、 ``allow_redirects`` パラメーターを使うことでリダイレクトの処理を
無効にすることができます。 ::

    >>> r = requests.get('http://github.com', allow_redirects=False)
    >>> r.status_code
    301
    >>> r.history
    []

.. If you're using POST, PUT, PATCH, DELETE or HEAD, you can enable
   redirection as well::

POST、PUT、PATCHを使う場合、明示的にリダイレクトを有効にすることができます。 ::

    >>> r = requests.post('http://github.com', allow_redirects=True)
    >>> r.url
    'https://github.com/'
    >>> r.history
    [<Response [301]>]


.. Timeouts
   --------

タイムアウト
------------------

.. You can tell requests to stop waiting for a response after a given number of
   seconds with the ``timeout`` parameter::

``timeout`` パラメーターに秒数を与えると、Requestsに与えた秒数で応答の待機を止めることができます。 ::

    >>> requests.get('http://github.com', timeout=0.001)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    requests.exceptions.Timeout: Request timed out.

.. Note

.. admonition:: 注意:

    .. ``timeout`` only effects the connection process itself, not the
       downloading of the response body.

    ``timeout`` は、レスポンスの本文をダウンロードせず接続の処理だけにしか影響しません。


.. Errors and Exceptions
   ---------------------

エラーと例外
-------------------

.. In the event of a network problem (e.g. DNS failure, refused connection, etc),
   Requests will raise a :class:`ConnectionError` exception.

ネットワークの問題が起こった時(例えば、DNSのエラーやコネクションの切断等)に、Requestsは :class:`ConnectionError` の例外を発生します。

.. In the event of the rare invalid HTTP response, Requests will raise
   an  :class:`HTTPError` exception.

稀に不正なHTTPレスポンスがあった時に、Requestsは :class:`HTTPError` の例外を発生します。

.. If a request times out, a :class:`Timeout` exception is raised.

リクエストがタイムアウトした場合、 :class:`Timeout` の例外を発生します。

.. If a request exceeds the configured number of maximum redirections, a
   :class:`TooManyRedirects` exception is raised.

リクエストが設定されたリダイレクトの最大数超えた場合、 :class:`TooManyRedirects` の例外を発生します。

.. All exceptions that Requests explicitly raises inherit from
   :class:`requests.exceptions.RequestException`.

全ての例外は、 :class:`requests.exceptions.RequestException` を継承して明示的に発生させます。

.. You can refer to :ref:`Configuration API Docs <configurations>` for immediate
   raising of :class:`HTTPError` exceptions via the ``danger_mode`` option or
   have Requests catch the majority of
   :class:`requests.exceptions.RequestException` exceptions with the ``safe_mode``
   option.

``danger_mode`` オプションにして :class:`HTTPError` の例外をすぐに発生させることや 、
``safe_mode`` オプションで :class:`requests.exceptions.RequestException` でRequestsが捕まえる代表的な例外を取得するためには、
:ref:`Configuration API Docs <configurations>` を見てください。

-----------------------

.. Ready for more? Check out the :ref:`advanced <advanced>` section.

さらなる準備はできましたか?
:ref:`advanced <advanced>` の章をチェックして下さい。
