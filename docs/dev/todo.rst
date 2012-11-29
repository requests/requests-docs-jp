.. How to Help
   ===========

サポート方法
=================

.. Requests is under active development, and contributions are more than welcome!

Requestsは活発に開発中で、プロジェクトへの貢献はどしどし受け付けています!

.. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
   There is a Contributor Friendly tag for issues that should be ideal for people who are not very
   familiar with the codebase yet.
.. Fork `the repository <https://github.com/kennethreitz/requests>`_ on Github to start making your
   changes to the **develop** branch (or branch off of it).
.. Write a test which shows that the bug was fixed or that the feature works as expected.
.. Send a pull request and bug the maintainer until it gets merged and published. :)
   Make sure to add yourself to `AUTHORS <https://github.com/kennethreitz/requests/blob/develop/AUTHORS.rst>`_.

#. 公開されているissueの一覧をチェックするか、機能のアイデアやバグに関するディスカッションをするための新しいissueを作成して下さい。
   まだコードに精通していない人にとって持って来いのContributor Friendlyタグがあります。
#. **develop** ブランチ(もしくはそれから派生したブランチ)に修正を加えるために、
   Githubの `リポジトリ <https://github.com/kennethreitz/requests>`_ をフォークして下さい。
#. 期待している通りに動くか修正したバグが分かるようなテストを書く。
#. プルリクエストを送るとバグのメンテナーがマージして公開します。
   `AUTHORS <https://github.com/kennethreitz/requests/blob/develop/AUTHORS.rst>`_ に追加されるでしょう。

.. Development dependencies
   ------------------------

開発の際の依存関係
---------------------------

.. You'll need to install ``gunicorn`` and ``httpbin`` and various other dependencies in
   order to run requests' test suite::

requestsのテストスイートを実行するために、
``gunicorn`` や ``httpbin`` や他の依存するものをインストールする必要があります。 ::

    $ virtualenv env
    $ . env/bin/activate
    $ make
    $ make test

.. The ``Makefile`` has various useful targets for testing. For example, if you
   want to see how your pull request will behave with Travis-CI you would run
   ``make travis``.

``Makefile`` は、様々なテスト用の便利なツールがあります。
例として、Travis-CIでのプルリクエストの振る舞いを確認する場合は、 ``make travis`` を実行して下さい。

.. Versions of Python to Test On
   -----------------------------

テストするPythonのバージョン
---------------------------------------------------

.. Officially (as of 26-Nov-2012), requests supports python 2.6-3.3. In the
   future, support for 3.1 and 3.2 may be dropped. In general you will need to
   test on at least one python 2 and one python 3 version. You can also set up
   Travis CI for your own fork before you submit a pull request so that you are
   assured your fork works. To use Travis CI for your fork and other projects see
   their `documentation <http://about.travis-ci.org/docs/user/getting-started/>`_.

公式に(2012.11.26)、RequestsはPython 2.6から3.3をサポートします。
将来的には、バージョン3.1と3.2はサポート対象から外すかもしれません。
一般的に、Pythonのバージョン2から一つ、Pythonのバージョン3から一つを少なくともテストしなければいけません。
フォークしたものが動作しているかを確認したい場合、プルリクエストを送る前にフォークしたものにTravis CIを設定することもできます。
フォークしたものや他のプロジェクトのもので、Travis CIを使うためにはそれらの `ドキュメント <http://about.travis-ci.org/docs/user/getting-started/>`_ を見て下さい。

.. What Needs to be Done
   ---------------------

やらなければいけないこと
-------------------------------

.. Documentation needs a roadmap.

- ドキュメントにロードマップが必要です。
