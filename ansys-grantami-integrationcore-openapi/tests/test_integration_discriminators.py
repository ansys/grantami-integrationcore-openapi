# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum
import types

import ansys.grantami.integrationcore_openapi.integration.models as models
import pytest

ALL_MODELS = {
    k: v
    for k, v in models.__dict__.items()
    if isinstance(v, type) and k not in ("ModelBase", "Unset_Type") and not issubclass(v, Enum)
}
POLYMORPHIC_MODELS = {
    k: v for k, v in ALL_MODELS.items() if "discriminator_value_class_map" in v.__dict__
}
MONOMORPHIC_MODELS = {k: v for k, v in ALL_MODELS.items() if k not in POLYMORPHIC_MODELS.keys()}


@pytest.mark.parametrize("cls", ALL_MODELS.values())
def test_get_real_child_model_method_exists(cls):
    assert isinstance(cls.get_real_child_model, types.MethodType)


@pytest.mark.parametrize("cls", POLYMORPHIC_MODELS.values())
def test_get_real_child_model_returns_correct_class_name(cls):
    for value, sub_cls in cls.discriminator_value_class_map.items():
        discriminator_property = cls._get_discriminator_field_name()
        sub_cls_name = cls.get_real_child_model({discriminator_property: value})
        assert sub_cls_name == sub_cls.rsplit("/", 1)[-1]


@pytest.mark.parametrize("cls", POLYMORPHIC_MODELS.values())
def test_polymorphic_child_class_exists(cls):
    for sub_cls in cls.discriminator_value_class_map.values():
        sub_cls_name = sub_cls.rsplit("/", 1)[-1]
        assert sub_cls_name in ALL_MODELS.keys()


@pytest.mark.parametrize("cls", MONOMORPHIC_MODELS.values())
def test_monomorphic_model_raises_notimplemented(cls):
    with pytest.raises(NotImplementedError):
        cls.get_real_child_model({})
