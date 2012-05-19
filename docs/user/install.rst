.. _install:

インストールする方法
========================

.. Installation
   ============

.. This part of the documentation covers the installation of Requests.
   The first step to using any software package is getting it properly installed.

ドキュメントのこの章はRequestsのインストール方法をカバーしています。
パッケージを使うための最初のステップは適切にインストールすることです。

Distribute & Pip
----------------

.. Installing requests is simple with `pip <http://www.pip-installer.org/>`_::

Requestsのインストールは、 `pip <http://www.pip-installer.org/>`_ を使うと簡単です。 ::

    $ pip install requests

.. or, with `easy_install <http://pypi.python.org/pypi/setuptools>`_::

もしくは、 `easy_install <http://pypi.python.org/pypi/setuptools>`_ を使います。 ::

    $ easy_install requests

.. But, you really `shouldn't do that <http://www.pip-installer.org/en/latest/other-tools.html#pip-compared-to-easy-install>`_.

しかし、 `そうすべきではない <http://www.pip-installer.org/en/latest/other-tools.html#pip-compared-to-easy-install>`_ 。

.. Cheeseshop Mirror
   -----------------

Cheeseshopミラー
--------------------

.. If the Cheeseshop is down, you can also install Requests from Kenneth Reitz's
   personal `Cheeseshop mirror <http://pip.kennethreitz.com/>`_::

Cheeseshopはダウンしている場合は、Kenneth Reitzの `Cheeseshopのミラー <http://pip.kennethreitz.com/>`_ から
インストールすることもできます。

    $ pip install -i http://pip.kennethreitz.com/simple requests


.. Get the Code
   ------------

コードを取得する
----------------------

.. Requests is actively developed on GitHub, where the code is
   `always available <https://github.com/kennethreitz/requests>`_.

Requestsは、GitHub上で活発に開発されていて、コードは `いつでも見ることができます <https://github.com/kennethreitz/requests>`_ 。

.. You can either clone the public repository::

公開レポジトリを複製するができます。 ::

    git clone git://github.com/kennethreitz/requests.git

.. Download the `tarball <https://github.com/kennethreitz/requests/tarball/master>`_::

`tarball <https://github.com/kennethreitz/requests/tarball/master>`_ をダウンロードして下さい。 ::

    $ curl -OL https://github.com/kennethreitz/requests/tarball/master

.. Or, download the `zipball <https://github.com/kennethreitz/requests/zipball/master>`_::

もしくは、 `zipball <https://github.com/kennethreitz/requests/zipball/master>`_ をダウンロードして下さい。 ::

    $ curl -OL https://github.com/kennethreitz/requests/zipball/master


.. Once you have a copy of the source, you can embed it in your Python package,
   or install it into your site-packages easily::

ソースのコピーを持っていないなら、Pythonパッケージに埋め込んだり、site-packagesに
簡単にインストールすることができます。

    $ python setup.py install

.. _gevent:

Geventをインストールする
--------------------------------

.. Installing Gevent
   -----------------

.. If you are using the ``requests.async`` module for making concurrent
   requests, you need to install gevent.

コンカレントリクエストを作成するための ``requests.async`` モジュールを使っているなら、
geventをインストールする必要があります。

.. To install gevent, you'll need ``libevent``.

geventをインストールするためには、 ``libevent`` が必要です。

OSX::

    $ brew install libevent

Ubuntu::

    $ apt-get install libevent-dev

.. Once you have ``libevent``, you can install ``gevent`` with ``pip``::

``libevent`` がインストールされたら、 ``pip`` で ``gevent`` をインストールできます。 ::

    $ pip install gevent
