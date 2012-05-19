.. Requests: HTTP for Humans
   =========================

Requests: 人間のためのHTTP
=====================================

.. warning:: このドキュメントは `Requests <http://docs.python-requests.org/>`_ のドキュメントを翻訳したものです。
   翻訳の間違いなどの指摘は、 `翻訳リポジトリのIssues <https://github.com/tokuda109/requests-docs-ja/issues>`_ に登録して頂けるとうれしいです。

.. Requests is an ISC Licensed HTTP library, written in Python, for human
   beings.

Requestsは、人が使いやすいように作られていて、Pythonで書かれたISCライセンスのHTTPライブラリです。

.. Most existing Python modules for sending HTTP requests are extremely
   verbose and cumbersome. Python's builtin urllib2 module provides most of
   the HTTP capabilities you should need, but the api is thoroughly broken.
   It requires an enormous amount of work (even method overrides) to
   perform the simplest of tasks.

助長で扱いが難しいHTTPリクエストを送るための既にあるPythonモジュールがたくさんあります。
Pythonの組み込みのurllib2モジュールは、必要なHTTP機能がほとんど提供されていますが、APIがまともに使えません。
簡単なことを行う(メソッドの上書きでさえ)ためにたくさんの作業量が必要になります。

.. Things shouldn't be this way. Not in Python.

それはPython的ではないので、そんなに複雑にするべきではありません。

::

    >>> r = requests.get('https://api.github.com', auth=('user', 'pass'))
    >>> r.status_code
    204
    >>> r.headers['content-type']
    'application/json'
    >>> r.text
    ...

.. See `the same code, without Requests <https://gist.github.com/973705>`_.

`Requestsを使わずに同じ事をするときのコード <https://gist.github.com/973705>`_ を見て下さい。

Requests allow you to send HTTP/1.1 requests. You can add headers, form data,
multipart files, and parameters with simple Python dictionaries, and access the
response data in the same way. It's powered by httplib and `urllib3
<https://github.com/shazow/urllib3>`_, but it does all the hard work and crazy
hacks for you.

.. Features
   --------

機能
-----------

- International Domains and URLs
- Keep-Alive & Connection Pooling
- Sessions with Cookie Persistence
- Browser-style SSL Verification
- Basic/Digest Authentication
- Elegant Key/Value Cookies
- Automatic Decompression
- Unicode Response Bodies
- Multipart File Uploads
- Connection Timeouts
- Thread-safety

- ドメインとURLの国際化
- Keep-Aliveとコネクションプーリング
- Cookieによるセッションの永続化
- ブラウザのようなSSL接続
- ベーシック/ダイジェスト認証
- キー/バリューが整理されたCookie
- 圧縮の自動的な展開
- レスポンスの本文のユニコード化
- 複数のファイルアップロード
- コネクションのタイムアウト
- スレッドセーフ

.. Installation
   ------------

インストール
---------------

.. To install requests, simply: ::

Requestsをインストールするのは簡単です。 ::

    $ pip install requests

.. Or, if you absolutely must: ::

もしくは、以下でも同じです。 ::

    $ easy_install requests

.. But, you really shouldn't do that.

しかし、そうすべきではない。

.. Contribute
   ----------

コントリビュート
---------------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
#. Fork `the repository`_ on Github to start making your changes to the **develop** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: http://github.com/kennethreitz/requests
.. _AUTHORS: https://github.com/kennethreitz/requests/blob/develop/AUTHORS.rst
