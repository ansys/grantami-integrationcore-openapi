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

from pathlib import Path
import py_compile

import pytest

src_folder = Path(__file__) / "../../src"
files = list(src_folder.rglob("*.py"))


@pytest.mark.parametrize("file", files, ids=[f.relative_to(src_folder).as_posix() for f in files])
def test_all_code_valid(file):
    py_compile.compile(file=file, doraise=True)
