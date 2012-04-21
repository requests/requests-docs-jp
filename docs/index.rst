.. requests-docs-ja documentation master file, created by
   sphinx-quickstart on Sun Apr  1 15:13:59 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Requests: HTTP for Humans
   =========================

Requests: 人のためのHTTP
============================

.. Release v\ |version|. (:ref:`Installation <install>`)

リリース v\ |version|. (:ref:`Installation <install>`)

.. Requests is an :ref:`ISC Licensed <isc>` HTTP library, written in Python, for human beings.

Requestsは、人が使いやすいように作られていて、Pythonで書かれた :ref:`ISC Licensed <isc>` ベースのHTTPライブラリです。

.. Python's standard **urllib2** module provides most of
   the HTTP capabilities you need, but the API is thoroughly **broken**.
   It was built for a different time — and a different web. It requires an *enormous* amount of work (even method overrides) to perform the simplest of tasks.

Pythonの標準の **urllib2** モジュールは、必要とされるほとんどのHTTPの機能を備えていますが、APIがまともに **使えません** 。
様々なウェブ用に作られていて、何回も修正されてきました。
簡単なことをするため(メソッドの上書きでさえ)に、かなりの量の作業が必要になります。

.. Things shouldn’t be this way. Not in Python.

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

.. Requests takes all of the work out of Python HTTP/1.1 — making your integration with web services seamless.
   There's no need to manually add query strings to your URLs, or to form-encode your POST data.
   Keep-alive and HTTP connection pooling are 100%  automatic, powered by
   `urllib3 <https://github.com/shazow/urllib3>`_, which is embedded within Requests.

Requestsは、ウェブサーバーとシームレスに統合されたPythonのHTTP/1.1の処理の全てを受け持ちます。
URLに手動でクエリを入力したり、POSTデータをエンコードしたりする必要はありません。
Keep-aliveやHTTP接続は `urllib3 <https://github.com/shazow/urllib3>`_ によって100%自動で、Requestsに組み込まれています。

.. Testimonials
   ------------

推薦文
------------

.. `Heroku <http://heroku.com>`_,
   `PayPal <https://www.paypal.com/>`_,
   `Transifex <https://www.transifex.net/>`_,
   `Native Instruments <http://www.native-instruments.com/>`_, `The Washington Post <http://www.washingtonpost.com/>`_,
   `Twitter, Inc <http://twitter.com>`_,
   `Readability <http://readability.com>`_, and
   Federal US Institutions
   use Requests internally. It has been installed over 100,000 times from PyPI.

`Heroku <http://heroku.com>`_, 
`PayPal <https://www.paypal.com/>`_,
`Transifex <https://www.transifex.net/>`_,
`Native Instruments <http://www.native-instruments.com/>`_,
`The Washington Post <http://www.washingtonpost.com/>`_,
`Twitter, Inc <http://twitter.com>`_,
`Readability <http://readability.com>`_,
Federal US Institutions は内部でRequestsを使っています。
PyPIから100,000回以上インストールされています。

**Armin Ronacher**
    .. Requests is the perfect example how beautiful an API can be with the
       right level of abstraction.

    Requestsはどのように美しいAPIを正しく抽象化できるかの完璧な例です。

**Matt DeBoard**
    .. I'm going to get @kennethreitz's Python requests module tattooed
       on my body, somehow. The whole thing.

    私は@kennethreitzのPythonのRequestsモジュールのタトゥーを何とかして体に入れたい。以上。

**Daniel Greenfeld**
    .. Nuked a 1200 LOC spaghetti code library with 10 lines of code thanks to
       @kennethreitz's request library. Today has been AWESOME.

    @kennethreitzのリクエストライブラリに感謝して
    今日ではすばらしくなりました。

**Kenny Meyers**
    .. Python HTTP: When in doubt, or when not in doubt, use Requests. Beautiful,
       simple, Pythonic.

    PythonのHTTPにおいて、疑わしいときも、疑わしくない時も、Requestsを使います。美しくて、シンプルで、Pythonicだ。

.. Feature Support
   ---------------

サポートする機能
------------------

.. Requests is ready for today's web.

Requestsは現在のウェブに欠かせない機能を持っています。

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
.. ``.netrc`` support

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
- ``.netrc`` のサポート

.. User Guide
   ----------

ユーザーガイド
--------------------

.. This part of the documentation, which is mostly prose, begins with some
   background information about Requests, then focuses on step-by-step
   instructions for getting the most out of Requests.

ドキュメントのこの章は、Requestsに関するいくつかの背景を説明することから始めます。
それから、Requestsを有効に使うための説明をステップバイステップで紹介します。

.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/quickstart
   user/advanced


.. Community Guide
   -----------------

コミュニティガイド
--------------------

.. This part of the documentation, which is mostly prose, details the
   Requests ecosystem and community.

ドキュメントのこの章は、Requestsのエコシステムやコミュニティについて書いています。

.. toctree::
   :maxdepth: 1

   community/faq
   community/out-there.rst
   community/support
   community/updates

.. API Documentation
   -----------------

APIドキュメント
--------------------

.. If you are looking for information on a specific function, class or method,
   this part of the documentation is for you.

特定の関数やクラスやメソッドの情報を探している場合、ドキュメントのこの章を見て下さい。

.. toctree::
   :maxdepth: 2

   api


.. Developer Guide
   ---------------

開発者ガイド
------------------

.. If you want to contribute to the project, this part of the documentation is for
   you.

プロジェクトに貢献したい場合、ドキュメントのこの章を見て下さい。

.. toctree::
   :maxdepth: 1

   dev/internals
   dev/todo
   dev/authors
