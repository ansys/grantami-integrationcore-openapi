# Copyright (C) 2026 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0

# flake8: noqa

# import API ABC
from ansys.openapi.common import ApiBase

# import apis into api package
from .default_api import DefaultApi

__all__ = [
    "ApiBase",
    "DefaultApi",
]
