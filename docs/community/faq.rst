.. _faq:

よくある質問
=============================

.. Frequently Asked Questions
   ==========================

.. This part of the documentation answers common questions about Requests.

ドキュメントのこの章は、Requestsに関する一般的な質問に答えます。

.. Encoded Data?
   -------------

データはエンコードされますか?
---------------------------------------

.. Requests automatically decompresses gzip-encoded responses, and does
   its best to decode response content to unicode when possible.

Requestsは自動的にgzipエンコードされたレスポンスを解凍します。
そして、可能ならユニコード化するためにレスポンスの本文をデコードします。

.. You can get direct access to the raw response (and even the socket),
   if needed as well.

必要なら、生のレスポンス(とソケット)に直接アクセスすることができます。


.. Custom User-Agents?
   -------------------

ユーザーエージェントをカスタマイズできますか?
--------------------------------------------------

.. Requests allows you to easily override User-Agent strings, along with
   any other HTTP Header.

Requestsは他のHTTPヘッダーと同様に、ユーザーエージェントの文字列を簡単に上書きすることができます。


.. Why not Httplib2?
   -----------------

なぜHttplib2ではないのですか?
----------------------------------

.. Chris Adams gave an excellent summary on
   `Hacker News <http://news.ycombinator.com/item?id=2884406>`_:

Chris Adamsさんは、 `Hacker News <http://news.ycombinator.com/item?id=2884406>`_ で、すばらしい見解を述べています。

    .. httplib2 is part of why you should use requests: it's far more respectable
       as a client but not as well documented and it still takes way too much code
       for basic operations. I appreciate what httplib2 is trying to do, that
       there's a ton of hard low-level annoyances in building a modern HTTP
       client, but really, just use requests instead. Kenneth Reitz is very
       motivated and he gets the degree to which simple things should be simple
       whereas httplib2 feels more like an academic exercise than something
       people should use to build production systems[1].

    httplib2はRequestsをなぜ使うべきかという理由の一部でしかありません。
    クライアントとしてはとても立派ですがドキュメント化があまりされていません。
    そして、基本的な操作をするためにたくさんのコードを書く必要があります。
    httplib2がやろうとしていることに感謝していますが、モダンなHTTPクライアントを作成するために低レベルの部分で不満がたくさんあるので、
    実際はhttplib2の代わりにRequestsを使っています。
    Kenneth Reitzはモチベーションが高く、本番環境のシステム[1]を作るために使うものよりはhttplib2は学校の勉強のような感じがするので、
    簡単なことは簡単にできるようにしようとしています。

    .. Disclosure: I'm listed in the requests AUTHORS file but can claim credit
       for, oh, about 0.0001% of the awesomeness.

    ディスクロージャー: RequestsのAUTHORSファイルにリストされていますが、クレジットにクレームを付けることができます。

    .. http://code.google.com/p/httplib2/issues/detail?id=96 is a good example:
       an annoying bug which affect many people, there was a fix available for
       months, which worked great when I applied it in a fork and pounded a couple
       TB of data through it, but it took over a year to make it into trunk and
       even longer to make it onto PyPI where any other project which required "
       httplib2" would get the working version.

    1. http://code.google.com/p/httplib2/issues/detail?id=96は良い例です。:
    たくさんの人に影響のある迷惑なバグは、そのバグによって数テラバイトものデータを解析してフォークしてそれを適用した時に数ヶ月も解決するために作業しなければいけなくなりますが、
    キチンと動くバージョンの"httplib2"が必要となる他のプロジェクトでtrunkにそれを作るために一年かけて引き継いで、PyPIでそれをつくるために長い期間がかかります。


.. Python 3 Support?
   -----------------

Python 3をサポートしていますか?
----------------------------------

.. Yes! Here's a list of Python platforms that are officially
   supported:

はい! 公式にサポートしているPythonプラットフォームのリストは以下のとおりです。

* Python 2.6
* Python 2.7
* Python 3.1
* Python 3.2
* Python 3.3
* PyPy 1.9