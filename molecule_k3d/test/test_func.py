"""Functional tests."""
import os
import subprocess

import molecule.logger
import molecule.util
import pytest
from molecule.test.conftest import change_dir_to
from molecule.test.conftest import random_string  # noqa
from molecule.test.conftest import temp_dir  # noqa

import molecule

LOG = molecule.logger.get_logger(__name__)


def format_result(result: subprocess.CompletedProcess):
    """Return friendly representation of completed process run."""
    return (
        f"RC: {result.returncode}\n"
        + f"STDOUT: {result.stdout}\n"
        + f"STDERR: {result.stderr}"
    )


def test_command_init_scenario(temp_dir, DRIVER):  # noqa
    """Verify that init scenario works."""
    role_directory = os.path.join(temp_dir.strpath, "test-init")
    cmd = [
        "molecule",
        "init",
        "role",
        "test-init",
    ]
    result = molecule.util.run_command(cmd)
    assert result.returncode == 0

    with change_dir_to(role_directory):
        molecule_directory = pytest.helpers.molecule_directory()
        scenario_directory = os.path.join(molecule_directory, "test-scenario")
        options = {"role_name": "test-init", "driver-name": DRIVER}
        cmd = [
            "molecule",
            "init",
            "scenario",
            "test-scenario",
            *molecule.util.dict2args(options),
        ]
        result = molecule.util.run_command(cmd)
        assert result.returncode == 0

        assert os.path.isdir(scenario_directory)

        # TODO(retr0h): Need to correct `verify.yml` upstream.
        # Attempts to always gather facts, which doesn't fit
        # the k3d paradigm.
        #  cmd = [
        #      "molecule",
        #      "--debug",
        #      "test",
        #      "-s",
        #      "test-scenario",
        #  ]
        #  result = molecule.util.run_command(cmd)
        #  assert result.returncode == 0
