import ldclient
from unittest.mock import MagicMock
from functools import wraps
from typing import Any


TEST_PREFIX = "test_"


class patch_feature:
    def __init__(self, feature_flag: str, value: Any, client=None):
        self.feature_flag = feature_flag
        self.value = value
        self.client = client or ldclient.get()
        self.original_variation = self.client.variation

    def copy(self):
        return patch_feature(
            feature_flag=self.feature_flag, value=self.value, client=self.client
        )

    def decorate_class(self, klass):
        # based on unittest.mock._patch.decorate_class
        for attr in dir(klass):
            if not attr.startswith(TEST_PREFIX):
                continue

            attr_value = getattr(klass, attr)
            if not hasattr(attr_value, "__call__"):
                continue
            patcher = self.copy()
            setattr(klass, attr, patcher(attr_value))
        return klass

    def decorate_method(self, method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            with patch_feature(self.feature_flag, self.value):
                return method(*args, **kwargs)

        return wrapper

    def __enter__(self):
        def get_variation(flag, user, default):
            if flag == self.feature_flag:
                return self.value
            return self.original_variation(flag, user, default)

        variation = MagicMock(spec=self.original_variation)
        variation.side_effect = get_variation
        self.client.variation = variation

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.client.variation = self.original_variation

    def __call__(self, thing):

        if isinstance(thing, type):
            ret = self.decorate_class(thing)
        else:
            ret = self.decorate_method(thing)

        return ret
