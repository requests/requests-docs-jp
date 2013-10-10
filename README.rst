.. Requests: HTTP for Humans
   =========================

Requests: 人間のためのHTTP
=====================================

.. image:: https://badge.fury.io/py/requests.png
    :target: http://badge.fury.io/py/requests

.. image:: https://travis-ci.org/kennethreitz/requests.png?branch=master
        :target: https://travis-ci.org/kennethreitz/requests

.. image:: https://pypip.in/d/requests/badge.png
        :target: https://crate.io/packages/requests/

.. Requests is an Apache2 Licensed HTTP library, written in Python, for human
   beings.

Requestsは、人が使いやすいように設計されているPythonで書かれたApache2ライセンスのHTTPライブラリです。

.. Most existing Python modules for sending HTTP requests are extremely
   verbose and cumbersome. Python's builtin urllib2 module provides most of
   the HTTP capabilities you should need, but the api is thoroughly broken.
   It requires an enormous amount of work (even method overrides) to
   perform the simplest of tasks.

冗長で扱うのが難しいHTTPリクエストを送信するためのPythonモジュールが既にたくさんあります。
Pythonの組み込みのurllib2モジュールは、必要なHTTP機能がほとんど提供されていますが、APIがまともに使えません。
簡単なことを行う(メソッドの上書きでさえ)のに、たくさんの作業量が必要になります。

.. Things shouldn't be this way. Not in Python.

それはPython的ではないので、そんなに複雑にするべきではありません。

.. code-block:: pycon

    >>> r = requests.get('https://api.github.com', auth=('user', 'pass'))
    >>> r.status_code
    204
    >>> r.headers['content-type']
    'application/json'
    >>> r.text
    ...

.. See `the same code, without Requests <https://gist.github.com/973705>`_.

`Requestsを使わずに同じ事をするときのコード <https://gist.github.com/973705>`_ を見て下さい。

.. Requests allow you to send HTTP/1.1 requests. You can add headers, form data,
   multipart files, and parameters with simple Python dictionaries, and access the
   response data in the same way. It's powered by httplib and `urllib3
   <https://github.com/shazow/urllib3>`_, but it does all the hard work and crazy
   hacks for you.

Requestsは、HTTP/1.1のリクエストを送信することができます。
ヘッダー、フォームデータ、マルチパートファイル、簡単なPythonの辞書形式でパラメータを添付することができ、
同じ方法でレスポンスデータにアクセスすることができます。
httplibや `urllib3 <https://github.com/shazow/urllib3>`_ が一緒に組み込まれていますが、
面倒な作業などは全てRequestsでやってくれます。


.. Features
   --------

機能
-----------

.. International Domains and URLs
.. Keep-Alive & Connection Pooling
.. Sessions with Cookie Persistence
.. Browser-style SSL Verification
.. Basic/Digest Authentication
.. Elegant Key/Value Cookies
.. Automatic Decompression
.. Unicode Response Bodies
.. Multipart File Uploads
.. Connection Timeouts
.. Thread-safety
.. HTTP(S) proxy support

- ドメインとURLの国際化
- Keep-Aliveとコネクションプーリング
- Cookieによるセッションの永続化
- ブラウザのようなSSLによる接続
- ベーシック/ダイジェスト認証
- エレガントなキー/バリューによるCookie
- 圧縮の自動的な展開
- レスポンスの本文のユニコード化
- マルチパートファイルのアップロード
- コネクションのタイムアウト
- スレッドセーフ
- HTTP(S)プロキシのサポート


.. Installation
   ------------

インストール
---------------

.. To install Requests, simply:

Requestsをインストールするのは簡単です。

.. code-block:: bash

    $ pip install requests

.. Or, if you absolutely must:

もしくは、以下でも同じです。

.. code-block:: bash

    $ easy_install requests

.. But, you really shouldn't do that.

しかし、easy_installを使うべきではない。


.. Documentation
   -------------

ドキュメント
----------------

.. Documentation is available at http://docs.python-requests.org/.

ドキュメントは、http://docs.python-requests.org/ で確認することができます。


.. Contribute
   ----------

コントリビュート
---------------------

.. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a `Contributor Friendly`_ tag for issues that should be ideal for people who are not very familiar with the codebase yet.
.. If you feel uncomfortable or uncertain about an issue or your changes, feel free to email @sigmavirus24 and he will happily help you via email, Skype, remote pairing or whatever you are comfortable with.
.. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
.. Write a test which shows that the bug was fixed or that the feature works as expected.
.. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

#. 公開されているissueの一覧をチェックするか、機能のアイデアやバグに関するディスカッションをするための新しいissueを作成して下さい。
   まだコードに精通していない人にとって持って来いの `Contributor Friendly`_ タグがあります。
#. If you feel uncomfortable or uncertain about an issue or your changes, feel free to email @sigmavirus24 and he will happily help you via email, Skype, remote pairing or whatever you are comfortable with.
#. **master** ブランチ(もしくはそれから派生したブランチ)に修正を加えるために、
   Githubの `リポジトリ <https://github.com/kennethreitz/requests>`_ をフォークして下さい。
#. 期待している通りに動くか修正したバグが分かるようなテストを書く。
#. プルリクエストを送るとバグのメンテナーがマージして公開します。
   `AUTHORS <https://github.com/kennethreitz/requests/blob/develop/AUTHORS.rst>`_ に追加されるでしょう。

.. _`the repository`: http://github.com/kennethreitz/requests
.. _AUTHORS: https://github.com/kennethreitz/requests/blob/master/AUTHORS.rst
.. _Contributor Friendly: https://github.com/kennethreitz/requests/issues?direction=desc&labels=Contributor+Friendly&page=1&sort=updated&state=open