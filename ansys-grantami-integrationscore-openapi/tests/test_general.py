# Copyright (C) 2026 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import py_compile

import pytest

src_folder = Path(__file__) / "../../src"
files = list(src_folder.rglob("*.py"))


@pytest.mark.parametrize("file", files, ids=[f.relative_to(src_folder).as_posix() for f in files])
def test_all_code_valid(file):
    py_compile.compile(file=file, doraise=True)
