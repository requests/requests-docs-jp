.. _advanced:

高度な使い方
=================

.. Advanced Usage
   ==============

.. This document covers some of Requests more advanced features.

この文章は、Requestsのより高度な機能を幾つか紹介します。

.. Session Objects
   ---------------

セッションオブジェクト
-----------------------------

.. The Session object allows you to persist certain parameters across
   requests. It also persists cookies across all requests made from the
   Session instance.

セッションオブジェクトは、リクエスト間で特定のパラメータを保持することができます。
セッションインターフェースから作られた全てのリクエストにわたってクッキーを保持します。

.. A session object has all the methods of the main Requests API.

セッションオブジェクトは、主要なRequestsのAPIのメソッドを全て持っています。

.. Let's persist some cookies across requests::

リクエスト間でいくつかのクッキーを保持してみましょう ::

    s = requests.session()

    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get("http://httpbin.org/cookies")

    print r.text
    # '{"cookies": {"sessioncookie": "123456789"}}'


.. Sessions can also be used to provide default data to the request methods::

セッションは、リクエストのメソッドにデフォルトのデータを提供するために使用することができます ::

    headers = {'x-test': 'true'}
    auth = ('user', 'pass')

    with requests.session(auth=auth, headers=headers) as c:

        # both 'x-test' and 'x-test2' are sent
        c.get('http://httpbin.org/headers', headers={'x-test2': 'true'})


.. Any dictionaries that you pass to a request method will be merged with the session-level values that are set. The method-level parameters override session parameters.

リクエストメソッドに渡す任意の辞書が設定されているセッションレベルの値とマージされます。
メソッドレベルのパラメータは、セッションパラメータを上書きします。

.. Remove a Value From a Dict Parameter

   Sometimes you'll want to omit session-level keys from a dict parameter. To do this, you simply set that key's value to ``None`` in the method-level parameter. It will automatically be omitted.

.. admonition:: 辞書パラメーターから値を削除する

    時々、辞書パラメーターからセッションレベルのキーを省略したい場合もあるかもしれません。
    それをするには、メソッドのパラメーターのキーの値を ``None`` セットするだけです。
    それは自動的に省略されます。

.. All values that are contained within a session are directly available to you. See the :ref:`Session API Docs <sessionapi>` to learn more.

セッション内に含まれている全ての値が直接使用可能です。
詳しくは :ref:`Session API Docs <sessionapi>` を見て下さい。

.. Request and Response Objects
   ----------------------------

リクエストオブジェクトとレスポンスオブジェクト
----------------------------------------------

.. Whenever a call is made to requests.*() you are doing two major things. First,
   you are constructing a ``Request`` object which will be sent of to a server
   to request or query some resource. Second, a ``Response`` object is generated
   once ``requests`` gets a response back from the server. The response object
   contains all of the information returned by the server and also contains the
   ``Request`` object you created originally. Here is a simple request to get some
   very important information from Wikipedia's servers::

requests.*() が呼ばれるたびに2つの主要なことをやっています。
一番目が ``リクエスト`` オブジェクトが作成され、これがいくつかのリソースを要求したり、照会するサーバーに送信したりします。
二番目が　``requests``　がサーバーから返されたレスポンスを取得した時に ``レスポンス`` オブジェクトが生成されます。
レスポンスオブジェクトはサーバーによって返された全ての情報を持っていて、作成した ``リクエスト`` オブジェクトも含まれています。
Wikipediaのサーバーからとても重要な情報をいくつか取得するための簡単なリクエストを送信する処理は以下のとおりです。 ::

    >>> response = requests.get('http://en.wikipedia.org/wiki/Monty_Python')

.. If we want to access the headers the server sent back to us, we do this::

サーバーが送り返してきたヘッダーにアクセスするには以下のようにします。 ::

    >>> response.headers
    {'content-length': '56170', 'x-content-type-options': 'nosniff', 'x-cache':
    'HIT from cp1006.eqiad.wmnet, MISS from cp1010.eqiad.wmnet', 'content-encoding':
    'gzip', 'age': '3080', 'content-language': 'en', 'vary': 'Accept-Encoding,Cookie',
    'server': 'Apache', 'last-modified': 'Wed, 13 Jun 2012 01:33:50 GMT',
    'connection': 'close', 'cache-control': 'private, s-maxage=0, max-age=0,
    must-revalidate', 'date': 'Thu, 14 Jun 2012 12:59:39 GMT', 'content-type':
    'text/html; charset=UTF-8', 'x-cache-lookup': 'HIT from cp1006.eqiad.wmnet:3128,
    MISS from cp1010.eqiad.wmnet:80'}

.. However, if we want to get the headers we sent the server, we simply access the
   request, and then the request's headers::

しかしながら、サーバーに送信したヘッダーを取得したい場合は、単純にリクエストにアクセスしてリクエストのヘッダーを取得して下さい。 ::

    >>> response.request.headers
    {'Accept-Encoding': 'identity, deflate, compress, gzip',
    'Accept': '*/*', 'User-Agent': 'python-requests/0.13.1'}


.. SSL Cert Verification
   ---------------------

SSL証明書の検証
---------------------

.. Requests can verify SSL certificates for HTTPS requests, just like a web browser. To check a host's SSL certificate, you can use the ``verify`` argument::

RequestsはウェブブラウザのようにHTTPSリクエストのSSL証明書を検証することができます。
ホストのSSL証明書をチェックするために、 ``verify`` 引数を使うことができます。

    >>> requests.get('https://kennethreitz.com', verify=True)
    requests.exceptions.SSLError: hostname 'kennethreitz.com' doesn't match either of '*.herokuapp.com', 'herokuapp.com'

.. I don't have SSL setup on this domain, so it fails. Excellent. Github does though::

このドメインに設定するSSLを持っていないので失敗します。
けっこう。Githubでは可能です。 ::

    >>> requests.get('https://github.com', verify=True)
    <Response [200]>

.. You can also pass ``verify`` the path to a CA_BUNDLE file for private certs. You can also set the ``REQUESTS_CA_BUNDLE`` environment variable.

プライベート証明書用のCA_BUNDLEファイルのパスを ``verify`` に渡すこともできます。
``REQUESTS_CA_BUNDLE`` 環境変数を設定することもできます。

.. Requests can also ignore verifying the SSL certficate if you set ``verify`` to False. ::

``verify`` をFalseにした場合、RequestsはがSSL証明書の検証を無視するようにすることもできます。 ::

    >>> requests.get('https://kennethreitz.com', verify=False)
    <Response [200]>

.. By default, ``verify`` is set to True. Option ``verify`` only applies to host certs.

デフォルトで、 ``verify`` はTrueに設定されています。
``verify`` は、証明書をホスト提供するためだけのオプションです。

.. You can also specify the local cert file either as a path or key value pair::

ローカルのパスやキーとバリューのペアのどちらかを証明書として指定することもできます。 ::

    >>> requests.get('https://kennethreitz.com', cert=('/path/server.crt', '/path/key'))
    <Response [200]>

.. If you specify a wrong path or an invalid cert::

もし間違ったパスや不正な証明書を指定した場合 ::

    >>> requests.get('https://kennethreitz.com', cert='/wrong_path/server.pem')
    SSLError: [Errno 336265225] _ssl.c:347: error:140B0009:SSL routines:SSL_CTX_use_PrivateKey_file:PEM lib


.. Body Content Workflow
   ---------------------

本文のワークフロー
---------------------

.. By default, when you make a request, the body of the response isn't downloaded immediately. The response headers are downloaded when you make a request, but the content isn't downloaded until you access the :class:`Response.content` attribute.

リクエストを作成する時にデフォルトで、レスポンスボディをすぐにダウンロードしません。
リクエストを作成する時にレスポンスヘッダーがダウンロードされますが、本文は :class:`Response.content`
アトリビュートにアクセスするまでダウンロードされません。

.. Let's walk through it::

ではやってみましょう ::

    tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
    r = requests.get(tarball_url)

.. The request has been made, but the connection is still open. The response body has not been downloaded yet. ::

リクエストが作成されましたがまだ接続されたままです。
レスポンスボディはまだダウンロードされていません。 ::

    r.content

.. The content has been downloaded and cached.

コンテンツがダウンロードされ、キャッシュされました。

.. You can override this default behavior with the ``prefetch`` parameter::

``prefetch`` パラメーターでデフォルトのこの振る舞いを上書きすることができます。 ::

    r = requests.get(tarball_url, prefetch=True)
    # Blocks until all of request body has been downloaded.


.. Configuring Requests
   --------------------

Requestsの設定
--------------------

.. Sometimes you may want to configure a request to customize its behavior. To do
   this, you can pass in a ``config`` dictionary to a request or session. See the :ref:`Configuration API Docs <configurations>` to learn more.

時々、振る舞いをカスタマイズするためにリクエストの設定をしたいかもしれません。
これをするには、リクエストかセッションに ``config`` 辞書を渡すことができます。
さらに知りたい場合は、 :ref:`Configuration API Docs <configurations>` を見て下さい。

Keep-Alive
----------

.. Excellent news — thanks to urllib3, keep-alive is 100% automatic within a session! Any requests that you make within a session will automatically reuse the appropriate connection!

素晴らしいお知らせです。
キープアライブはセッション内で100%自動的に行われるので、urllib3に感謝しています。
セッション内で生成した任意のリクエストは自動的に接続が継続します。

.. Note that connections are only released back to the pool for reuse once all body data has been read; be sure to either set ``prefetch`` to ``True`` にするかして下さい。or read the ``content`` property of the ``Response`` object.

すべての本文のデータが読み込まれた後に接続が一度再利用のためにプールに戻されることに注意してください。
``Response`` オブジェクトの ``content`` プロパティを見るか ``prefetch`` を ``True`` にするかして下さい。

.. If you'd like to disable keep-alive, you can simply set the ``keep_alive`` configuration to ``False``::

Keep-Aliveを無効にしたい場合は、単純に ``keep_alive`` の設定を ``False`` にするだけです。 ::

    s = requests.session()
    s.config['keep_alive'] = False


.. Asynchronous Requests
   ----------------------

非同期のリクエスト
----------------------

.. ``requests.async`` has been removed from requests and is now its own repository named `GRequests <https://github.com/kennethreitz/grequests>`_.

``requests.async`` はRequestsから削除しました。
そして現在は、それ単体で `GRequests <https://github.com/kennethreitz/grequests>`_ にレポジトリがあります。


.. Event Hooks
   -----------

イベントフック
------------------

.. Requests has a hook system that you can use to manipulate portions of
   the request process, or signal event handling.

Requestsにはリクエストの処理やシグナルイベントの処理の一部を操作することができるフックシステムがあります。

.. Available hooks:

フックを有効にするには :

``args``:
    .. A dictionary of the arguments being sent to Request().

    Request()に送られる引数の辞書

``pre_request``:
    .. The Request object, directly before being sent.

    リクエストオブジェクト、

``post_request``:
    .. The Request object, directly after being sent.

    リクエストオブジェクト、

``response``:
    .. The response generated from a Request.

    リクエストから生成されたレスポンス

.. You can assign a hook function on a per-request basis by passing a
   ``{hook_name: callback_function}`` dictionary to the ``hooks`` request
   parameter::

``hooks`` リクエストのパラメーターに ``{hook_name: callback_function}``
の辞書を渡すことで、リクエスト毎にフック関数を割り当てることができます。

    hooks=dict(args=print_url)

.. That ``callback_function`` will receive a chunk of data as its first
   argument.

その ``callback_function`` は最初の引数としてデータのチャンクを受け取ります。

::

    def print_url(args):
        print args['url']

.. If an error occurs while executing your callback, a warning is given.

コールバックの最中にエラーが発生したら、警告を発します。

.. If the callback function returns a value, it is assumed that it is to
   replace the data that was passed in. If the function doesn't return
   anything, nothing else is effected.

コールバック関数が値を返す場合、コールバック関数は渡されたデータを置き換えることが想定されます。
関数が何も返さなかった場合、他のものに影響を与えません。

.. Let's print some request method arguments at runtime::

ランタイムにリクエストメソッドの引数を表示させてみましょう ::

    >>> requests.get('http://httpbin.org', hooks=dict(args=print_url))
    http://httpbin.org
    <Response [200]>

.. Let's hijack some arguments this time with a new callback::

新しいコールバックを使って、いくつかの引数をハックしてみましょう ::

    def hack_headers(args):
        if args.get('headers') is None:
            args['headers'] = dict()

        args['headers'].update({'X-Testing': 'True'})

        return args

    hooks = dict(args=hack_headers)
    headers = dict(yo=dawg)

.. And give it a try::

試してみて下さい ::

    >>> requests.get('http://httpbin.org/headers', hooks=hooks, headers=headers)
    {
        "headers": {
            "Content-Length": "",
            "Accept-Encoding": "gzip",
            "Yo": "dawg",
            "X-Forwarded-For": "::ffff:24.127.96.129",
            "Connection": "close",
            "User-Agent": "python-requests.org",
            "Host": "httpbin.org",
            "X-Testing": "True",
            "X-Forwarded-Protocol": "",
            "Content-Type": ""
        }
    }


.. Custom Authentication
   ---------------------

カスタム認証
-----------------

.. Requests allows you to use specify your own authentication mechanism.

Requestsは認証システムを好きなものを使うことができます。

.. Any callable which is passed as the ``auth`` argument to a request method will
   have the opportunity to modify the request before it is dispatched.

リクエストメソッドの ``auth`` 引数に渡された任意の呼び出し可能なオブジェクトは、
リクエストが処理される前に修正されるタイミングがあります。

.. Authentication implementations are subclasses of ``requests.auth.AuthBase``,
   and are easy to define. Requests provides two common authentication scheme
   implementations in ``requests.auth``: ``HTTPBasicAuth`` and ``HTTPDigestAuth``.

認証の実装は ``requests.auth.AuthBase`` のサブクラスで、定義は簡単です。
Requestsは ``requests.auth`` で ``HTTPBasicAuth`` と ``HTTPDigestAuth``
という2つの一般的な認証スキームの実装を備えています。

.. Let's pretend that we have a web service that will only respond if the
   ``X-Pizza`` header is set to a password value. Unlikely, but just go with it.

``X-Pizza`` ヘッダーにパスワードの値が設定されている場合にのみ応答するウェブサービスがあるので設定しているふりをしてみましょう。
以下のようにするだけです。

::

    from requests.auth import AuthBase
    class PizzaAuth(AuthBase):
        """Attaches HTTP Pizza Authentication to the given Request object."""
        def __init__(self, username):
            # setup any auth-related data here
            self.username = username

        def __call__(self, r):
            # modify and return the request
            r.headers['X-Pizza'] = self.username
            return r

.. Then, we can make a request using our Pizza Auth::

それから、Pizza Authを使って、リクエストを生成することができます。 ::

    >>> requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
    <Response [200]>

.. Streaming Requests
   ------------------

ストリーミングリクエスト
------------------------------

.. With ``requests.Response.iter_lines()`` you can easily iterate over streaming
   APIs such as the `Twitter Streaming API <https://dev.twitter.com/docs/streaming-api>`_.

``requests.Response.iter_lines()`` で、 `Twitter Streaming API <https://dev.twitter.com/docs/streaming-api>`_
のようなストリーミングAPIから簡単に反復処理をすることができます。

.. To use the Twitter Streaming API to track the keyword "requests":

"requests"というキーワードをトラッキングするためにTwitterのストリーミングAPIを使うには :

::

    import requests
    import json

    r = requests.post('https://stream.twitter.com/1/statuses/filter.json',
        data={'track': 'requests'}, auth=('username', 'password'))

    for line in r.iter_lines():
	    if line: # filter out keep-alive new lines
		    print json.loads(line)


.. Verbose Logging
   ---------------

Verboseロギング
------------------

.. If you want to get a good look at what HTTP requests are being sent
   by your application, you can turn on verbose logging.

アプリケーションで送られてたHTTPリクエストを見やすくしたいなら、
Verboseロギングをオンにすることができます。

.. To do so, just configure Requests with a stream to write to::

これを行うには、ストリームを以下のようにしてRequestsを設定するだけです。 ::

    >>> my_config = {'verbose': sys.stderr}
    >>> requests.get('http://httpbin.org/headers', config=my_config)
    2011-08-17T03:04:23.380175   GET   http://httpbin.org/headers
    <Response [200]>


.. Proxies
   -------

プロキシ
------------

.. If you need to use a proxy, you can configure individual requests with the
   ``proxies`` argument to any request method:

プロキシを使う必要があるなら、 ``proxies`` 引数に任意のリクエストメソッドを渡して個々のリクエストを
設定することができます。

::

    import requests

    proxies = {
      "http": "10.10.1.10:3128",
      "https": "10.10.1.10:1080",
    }

    requests.get("http://example.org", proxies=proxies)

.. You can also configure proxies by environment variables ``HTTP_PROXY`` and ``HTTPS_PROXY``.

``HTTP_PROXY`` や ``HTTPS_PROXY`` の環境変数によってプロキシを設定することもできます。

::

    $ export HTTP_PROXY="10.10.1.10:3128"
    $ export HTTPS_PROXY="10.10.1.10:1080"
    $ python
    >>> import requests
    >>> requests.get("http://example.org")

.. To use HTTP Basic Auth with your proxy, use the `http://user:password@host/` syntax:

プロキシでベーシック認証を使うためには、 `http://user:password@host/` シンタックスを使います。:

::

    proxies = {
        "http": "http://user:pass@10.10.1.10:3128/",
    }

.. Compliance
   ----------

コンプライアンス
-----------------------

.. Requests is intended to be compliant with all relevant specifications and
   RFCs where that compliance will not cause difficulties for users. This
   attention to the specification can lead to some behaviour that may seem
   unusual to those not familiar with the relevant specification.

Requestsは、コンプラインスがユーザーにとって難しくならないようにしながら、
関連する全ての仕様とRFCに準拠することを目的としています。
仕様に対して注意することは、関連する仕様と似ないようにすることで、使いにくく感じないように行動を促すことです。

.. Encodings
   ^^^^^^^^^

エンコーディング
^^^^^^^^^^^^^^^^^^^^^^^^

.. When you receive a response, Requests makes a guess at the encoding to use for
   decoding the response when you call the ``Response.text`` method. Requests
   will first check for an encoding in the HTTP header, and if none is present,
   will use `chardet <http://pypi.python.org/pypi/chardet>`_ to attempt to guess
   the encoding.

レスポンスを受け取った時、Requestsは
エンコーディングを推測するために `chardet <http://pypi.python.org/pypi/chardet>`_ を使って、
Requestsは最初にHTTPヘッダーのエンコーディングをチェックして、noneを表示します。

The only time Requests will not do this is if no explicit charset is present
in the HTTP headers **and** the ``Content-Type`` header contains ``text``. In
this situation,
`RFC 2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.7.1>`_
specifies that the default charset must be ``ISO-8859-1``. Requests follows
the specification in this case. If you require a different encoding, you can
manually set the ``Response.encoding`` property, or use the raw
``Request.content``.

.. HTTP Verbs
   ----------

HTTPメソッド
-------------

.. Requests provides access to almost the full range of HTTP verbs: GET, OPTIONS,
   HEAD, POST, PUT, PATCH and DELETE. The following provides detailed examples of
   using these various verbs in Requests, using the GitHub API.

Requestsは、GET、OPTIONS、HEAD、POST、PUT、PATCH、DELETEなどのHTTPメソッドのほとんど全てにアクセスすることができます。
以下に、GitHubのAPIを使ってRequestsのこれらの様々なメソッドを使う詳細サンプルを掲載します。

.. We will begin with the verb most commonly used: GET. HTTP GET is an idempotent
   method that returns a resource from a given URL. As a result, it is the verb
   you ought to use when attempting to retrieve data from a web location. An
   example usage would be attempting to get information about a specific commit
   from GitHub. Suppose we wanted commit ``a050faf`` on Requests. We would get it
   like so::

最初に一般的によく使われているメソッドから始めましょう。
HTTPのGETは、与えられたURLのリソースを返す冪等メソッドです。
結果としてそれらのメソッドは、ウェブ上の場所からデータを取得しようとする時に使うメソッドです。
GitHubから特定のコミットに関する情報を取得してみる参考例を紹介します。
Requestsで ``a050faf`` をコミットしたいと仮定して下さい。以下のようになります。 ::

    >>> import requests
    >>> r = requests.get('https://api.github.com/repos/kennethreitz/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')

.. We should confirm that GitHub responded correctly. If it has, we want to work
   out what type of content it is. Do this like so::

GitHubが正しく応答したか確認する必要があります。
応答した場合は、それがどのようなコンテンツタイプかを検証していきます。
では、やってみます。 ::

    >>> if (r.status_code == requests.codes.ok):
    ...     print r.headers['content-type']
    ...
    application/json; charset=utf-8

.. So, GitHub returns JSON. That's great, we can use the JSON module to turn it
   into Python objects. Because GitHub returned UTF-8, we should use the
   ``r.text`` method, not the ``r.content`` method. ``r.content`` returns a
   bytestring, while ``r.text`` returns a Unicode-encoded string. I have no plans
   to perform byte-manipulation on this response, so I want any Unicode code
   points encoded.::

そして、GitHubはJSONを返してきました。
素晴らしい、JSONモジュールを使えるので、Pythonオブジェクトに変換することができます。
GitHubはUTF-8で返してくるので、 ``r.content`` メソッドではなく、 ``r.text`` メソッドを使って下さい。
``r.content`` はバイト文字列を返し、 ``r.text`` はユニコードにエンコーディングされた文字列を返します。
このレスポンスにおいて、バイト操作をするつもりはないので、任意のユニコードのコードはエンコードを示して欲しい。 ::

    >>> import json
    >>> commit_data = json.loads(r.text)
    >>> print commit_data.keys()
    [u'committer', u'author', u'url', u'tree', u'sha', u'parents', u'message']
    >>> print commit_data[u'committer']
    {u'date': u'2012-05-10T11:10:50-07:00', u'email': u'me@kennethreitz.com', u'name': u'Kenneth Reitz'}
    >>> print commit_data[u'message']
    makin' history

.. So far, so simple. Well, let's investigate the GitHub API a little bit. Now,
   we could look at the documentation, but we might have a little more fun if we
   use Requests instead. We can take advantage of the Requests OPTIONS verb to
   see what kinds of HTTP methods are supported on the url we just used.::

これまでのところ、非常にシンプルです。
ではGitHubのAPIを少し調べてみましょう。
ドキュメントで確認することができますが、Requestsを使ってもう少し面白いことができるかもしれません。
どのようなHTTPメソッド
RequestsのOPTIONSメソッドを活用することができます。 ::
我々は、HTTPメソッドの種類は、我々が単に使用されたURLに対してサポートされているかを確認する要求OPTIONS動詞を活用することができます。

    >>> verbs = requests.options(r.url)
    >>> verbs.status_code
    500

.. Uh, what? That's unhelpful! Turns out GitHub, like many API providers, don't
   actually implement the OPTIONS method. This is an annoying oversight, but it's
   OK, we can just use the boring documentation. If GitHub had correctly
   implemented OPTIONS, however, they should return the allowed methods in the
   headers, e.g.::

ええと、何があったのでしょう? 役立たず!
ほとんどのAPIプロバイダーと同様に、GitHubはOPTIONSメソッドが実装されていないということが判明しました。

    >>> verbs = requests.options('http://a-good-website.com/api/cats')
    >>> print verbs.headers['allow']
    GET,HEAD,POST,OPTIONS

.. Turning to the documentation, we see that the only other method allowed for
   commits is POST, which creates a new commit. As we're using the Requests repo,
   we should probably avoid making ham-handed POSTS to it. Instead, let's play
   with the Issues feature of GitHub.

ドキュメントを見てみると、
新しいコミットを作成するためのコミットするための許されている他のメソッドはPOSTしかないということがわかります。


.. This documentation was added in response to Issue #482. Given that this issue
   already exists, we will use it as an example. Let's start by getting it.::

このドキュメントでは、レスポンスにIssue　#482を追加しました。
このGithubのissueは存在していて、サンプルのように使うことができます。
それを取得してみましょう。 ::

    >>> r = requests.get('https://api.github.com/repos/kennethreitz/requests/issues/482')
    >>> r.status_code
    200
    >>> issue = json.loads(r.text)
    >>> print issue[u'title']
    Feature any http verb in docs
    >>> print issue[u'comments']
    3

.. Cool, we have three comments. Let's take a look at the last of them.::

クール、コメントが3つあります。
最後のコメントを見てみましょう。 ::

    >>> r = requests.get(r.url + u'/comments')
    >>> r.status_code
    200
    >>> comments = json.loads(r.text)
    >>> print comments[0].keys()
    [u'body', u'url', u'created_at', u'updated_at', u'user', u'id']
    >>> print comments[2][u'body']
    Probably in the "advanced" section

.. Well, that seems like a silly place. Let's post a comment telling the poster
   that he's silly. Who is the poster, anyway?::

まあ、それは愚かな場所のように思える。
投稿者を伝えるコメントを投稿してみましょう。
だれが投稿者か見てみましょう?

    >>> print comments[2][u'user'][u'login']
    kennethreitz

.. OK, so let's tell this Kenneth guy that we think this example should go in the
   quickstart guide instead. According to the GitHub API doc, the way to do this
   is to POST to the thread. Let's do it.::

この例は、クリックスタートガイドの代わりになると思うので、このKennethという人と話をしてみましょう。
GitHubのAPIのドキュメントによると、この方法はスレッドにPOSTすればいいみたいです。やってみましょう。 ::

    >>> body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
    >>> url = u"https://api.github.com/repos/kennethreitz/requests/issues/482/comments"
    >>> r = requests.post(url=url, data=body)
    >>> r.status_code
    404

.. Huh, that's weird. We probably need to authenticate. That'll be a pain, right?
   Wrong. Requests makes it easy to use many forms of authentication, including
   the very common Basic Auth.::

うーん、奇妙ですね。
認証が必要なのかもしれません。面倒ではないですか?
Requestsは、一般的なベーシック認証などの認証のためたくさんのフォームデータを簡単に使うことができます。 ::

    >>> from requests.auth import HTTPBasicAuth
    >>> auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')
    >>> r = requests.post(url=url, data=body, auth=auth)
    >>> r.status_code
    201
    >>> content = json.loads(r.text)
    >>> print content[u'body']
    Sounds great! I'll get right on it.

.. Brilliant. Oh, wait, no! I meant to add that it would take me a while, because
   I had to go feed my cat. If only I could edit this comment! Happily, GitHub
   allows us to use another HTTP verb, PATCH, to edit this comment. Let's do
   that.::

素晴らしい。
でもちょっと待った!
追加するために、しばらく時間がかかるかもしれません。なぜなら、I had to go feed my catだからです。
GitHubは、このコメントを編集するために、PATCHという別のHTTPメソッドを使うことができます。
やってみましょう。 ::

    >>> print content[u"id"]
    5804413
    >>> body = json.dumps({u"body": u"Sounds great! I'll get right on it once I feed my cat."})
    >>> url = u"https://api.github.com/repos/kennethreitz/requests/issues/comments/5804413"
    >>> r = requests.patch(url=url, data=body, auth=auth)
    >>> r.status_code
    200

.. Excellent. Now, just to torture this Kenneth guy, I've decided to let him
   sweat and not tell him that I'm working on this. That means I want to delete
   this comment. GitHub lets us delete comments using the incredibly aptly named
   DELETE method. Let's get rid of it.::

いいですね。
今丁度このKennethという男を悩ませるために、彼に汗をかかせて、彼にこれを取り組んでいることを教えないようにしました。
このコメントを削除したいということです。
GitHubは、信じられないくらい適切な名前のDELETEというメソッドを使ってコメントを削除することができます。
では削除してみましょう。 ::

    >>> r = requests.delete(url=url, auth=auth)
    >>> r.status_code
    204
    >>> r.headers['status']
    '204 No Content'

.. Excellent. All gone. The last thing I want to know is how much of my ratelimit
   I've used. Let's find out. GitHub sends that information in the headers, so
   rather than download the whole page I'll send a HEAD request to get the
   headers.::

いいですね。
全て完了しました。ratelimitがどのくらいあるかということことを最後に知っておきたいので、調べてみましょう。
GitHubはヘッダーを取得するためにHEADリクエストを送るとページ全体をダウンロードせずに、ヘッダーの情報を送信してくれます。

    >>> r = requests.head(url=url, auth=auth)
    >>> print r.headers
    // ...snip... //
    'x-ratelimit-remaining': '4995'
    'x-ratelimit-limit': '5000'
    // ...snip... //

.. Excellent. Time to write a Python program that abuses the GitHub API in all
   kinds of exciting ways, 4995 more times.

いいですね。
