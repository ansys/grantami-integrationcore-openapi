# Copyright (C) 2026 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# flake8: noqa

# import API ABC
from ansys.openapi.common import ApiBase

# import apis into api package
from .databases_api import DatabasesApi
from .model_definitions_api import ModelDefinitionsApi
from .models_api import ModelsApi
from .ready_api import ReadyApi
from .record_search_criteria_api import RecordSearchCriteriaApi
from .settings_api import SettingsApi
from .tables_api import TablesApi
from .users_api import UsersApi

__all__ = [
    "ApiBase",
    "DatabasesApi",
    "ModelDefinitionsApi",
    "ModelsApi",
    "ReadyApi",
    "RecordSearchCriteriaApi",
    "SettingsApi",
    "TablesApi",
    "UsersApi",
]
