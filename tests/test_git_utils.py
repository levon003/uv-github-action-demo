import subprocess

import pytest

from demo_python_package import git_utils


def test_get_diff_files():
    added_files, changed_files, deleted_files = git_utils.get_diff_files(
        source_branch="main"
    )
    assert len(added_files) == 0
    assert len(changed_files) == 0
    assert len(deleted_files) == 0

    with pytest.raises(subprocess.CalledProcessError):
        added_files, changed_files, deleted_files = git_utils.get_diff_files(
            source_branch="nonexistent_branch"
        )
