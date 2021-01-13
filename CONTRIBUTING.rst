.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/pymetrics/ld-feature-patch/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

LD Feature Patch could always use more documentation, whether as part of the
official LD Feature Patch docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/pymetrics/ld-feature-patch/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `ld-feature-patch` for local development.

1. Fork the `ld-feature-patch` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/ld-feature-patch.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv ld-feature-patch
    $ cd ld-feature-patch/
    $ python -m pip install -e .

4. Install dev dependencies::

    $ python -m pip install -r requirements_dev.txt

5. Set up pre-commit_::

    $ python -m pip install pre-commit
    $ pre-commit install

6. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

7. As you're making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ flake8 ld_patch tests
    $ make test

   If ``make test`` fails, make sure you've run ``python -m pip install -e .``
   (don't forget the ``.`` at the end!), and try again.

8. Before committing, format your code with Black_. Optionally, configure
   your editor to format on save.

9. Commit your changes and push your branch to GitHub. The pre-commit tool
   will run the test suite, and check for formatting and linter errors::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

10. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.6, 3.7 and 3.8, and for PyPy. Check
   https://travis-ci.com/pymetrics/ld-feature-patch/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ pytest tests.test_ld_patch


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass.


.. _pre-commit: https://pre-commit.com/
.. _Black: https://github.com/psf/black#installation-and-usage
