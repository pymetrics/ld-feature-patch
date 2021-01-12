=====
Usage
=====

To use LD Feature Patch in a project, decorate
your test methods with ``patch_feature``.


.. code:: python

    from ld_patch import patch_feature

    @patch_feature("my-feature-flag", True)
    def test_something():
        ...


``patch_feature`` takes two arguments:

  - The feature flag ket to override
  - The value the feature flag should assume.

Test Frameworks
---------------

Pytest
******

.. code:: python

    from ld_patch import patch_feature

    @patch_feature("my-feature-flag", True)
    def test_something():
        assert ld_client.variation(
            "my-feature-flag",
            "test-user@example.com",
            False,
        ) is True


Unittest
********

``patch_feature`` works with unittest test methods:


.. code:: python

    from ld_patch import patch_feature

    class MyTestCase(TestCase):
        @patch_feature("my-feature", True)
        def test_something(self):
            assert ld_client.variation(
                "my-feature",
                "testuser@example.com",
                False
            ) is True


Additionally, you can decorate an entire test case:

.. code:: python

    from ld_patch import patch_feature

    @patch_feature("my-feature", True)
    class MyTestCase(TestCase):

        def test_something(self):
            assert ld_client.variation(
                "my-feature",
                "testuser@example.com",
                False
            ) is True

        def test_something_else(self):
            assert ld_client.variation(
                "my-feature",
                "testuser@example.com",
                False
            ) is True


Advanced Usage
--------------

For codebases with complex LD client initialization schemes, ``patch_feature``
accepts the LD client to patch as an optional third argument.
