#!/usr/bin/env python

"""Tests for `ld_patch` package."""

from __future__ import absolute_import

from unittest import TestCase
from unittest.mock import patch

import ldclient
from ldclient.config import Config

from ld_patch import patch_feature


ldclient.set_config(Config("YOUR_SDK_KEY", offline=True))
client = ldclient.get()


def get_feature_status(
    feature_key: str, user_key: str = "test@example.com", default=False
):
    return client.variation(feature_key, user_key, default)


class TestPatchFeatureSimple(TestCase):
    def test_with_statement(self):
        with patch_feature("test-with-statement", "PASSED"):
            value = get_feature_status("test-with-statement")
            self.assertEqual(value, "PASSED")

    @patch_feature("method-decorator", "PASSED")
    def test_single_method_decorator(self):
        value = get_feature_status("method-decorator")
        self.assertEqual(value, "PASSED")

    @patch_feature("method-decorator-1", "PASSED-1")
    @patch_feature("method-decorator-2", "PASSED-2")
    def test_stacked_method_decorator(self):
        value_1 = get_feature_status("method-decorator-1")
        value_2 = get_feature_status("method-decorator-2")
        self.assertEqual(value_1, "PASSED-1")
        self.assertEqual(value_2, "PASSED-2")

    @patch_feature("a-feature", "PASSED")
    def test_overrides_feature_default(self):
        value = get_feature_status("a-feature", default="FAILED")
        self.assertEqual(value, "PASSED")

    @patch_feature("a-feature", "FAILED")
    def test_does_not_override_unpatched(self):
        value = get_feature_status("another-feature", default="PASSED")
        self.assertEqual(value, "PASSED")


@patch_feature("class-decorator", "class")
class TestPatchFeatureClassDecorator(TestCase):
    def test_class_decorator(self):
        value = get_feature_status("class-decorator")
        self.assertEqual(value, "class")

    @patch_feature("method-decorator", "method")
    def test_with_method_decorator(self):
        value_1 = get_feature_status("class-decorator")
        value_2 = get_feature_status("method-decorator")
        self.assertEqual(value_1, "class")
        self.assertEqual(value_2, "method")

    @patch_feature("method-decorator-1", "method-1")
    @patch_feature("method-decorator-2", "method-2")
    def test_with_stacked_method_decorators(self):
        value_1 = get_feature_status("class-decorator")
        value_2 = get_feature_status("method-decorator-1")
        value_3 = get_feature_status("method-decorator-2")
        self.assertEqual(value_1, "class")
        self.assertEqual(value_2, "method-1")
        self.assertEqual(value_3, "method-2")


@patch_feature("pytest-decorator", True)
def test_pytest_style():
    assert get_feature_status("pytest-decorator")


@patch_feature("pytest-1", True)
@patch_feature("pytest-2", True)
def test_assert_stacked_pytest():
    assert get_feature_status("pytest-1")
    assert get_feature_status("pytest-2")


def test_patch_feature_lazy_client_init():
    """Don't init the LD client at decoration time"""
    with patch.object(ldclient, "get", autospec=True):
        patch_feature("test", True)
        assert ldclient.get.call_count == 0
