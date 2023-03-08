# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-unsafe

class Manager:
    def aggregate(self, *args, **kwargs): ...
    def all(self): ...
    def create(self, **kwargs): ...
    def filter(self, *args, **kwargs): ...
    def get(self, *args, **kwargs): ...
    def get_or_create(self, defaults=None, **kwargs): ...
    def raw(self, raw_query, params=None, translations=None, using=None): ...
    def bulk_create(self, *args): ...
    def using(self, *args): ...
    def defer(self, *args, **kwargs): ...