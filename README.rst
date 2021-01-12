================
LD Feature Patch
================


.. image:: https://img.shields.io/pypi/v/ld_patch.svg
        :target: https://pypi.python.org/pypi/ld_patch

.. image:: https://img.shields.io/travis/pymetrics/ld-feature-patch.svg
        :target: https://travis-ci.com/pymetrics/ld-feature-patch

.. image:: https://readthedocs.org/projects/ld-feature-patch/badge/?version=latest
        :target: https://ld-feature-patch.readthedocs.io/en/latest/
        :alt: Documentation Status



Patch `Launch Darkly`_ feature flags for unit testing


* Free software: Apache Software License 2.0
* Documentation: https://ld-feature-patch.readthedocs.io/en/latest/.


Usage
--------

.. code:: python

    from ld_patch import patch_feature

    @patch_feature("my.flag.key", True)
    def test_my_code():

        # Feature defaults to False
        show_feature = ldclient.variation(
            "my.flag.key",
            "test@example.com",
            False
        )

        # But patch_feature set it to True
        assert show_feature == True


Installation
------------

.. code:: bash

    python -m pip install ld-feature-patch

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Launch Darkly`: https://launchdarkly.com/
