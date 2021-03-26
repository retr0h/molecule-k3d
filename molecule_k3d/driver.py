# Copyright (c) 2021 John Dewey <john@dewey.ws>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

"""K3D Driver Module."""

from __future__ import absolute_import

import os

from molecule.api import Driver

from molecule import logger

log = logger.get_logger(__name__)


class K3d(Driver):
    """
    K3D Driver Class.

    The class responsible for managing `K3D`_.

    Molecule leverages Ansible's `command`_ module, by mapping
    variables from ``molecule.yml`` into ``create.yml`` and ``destroy.yml``.

    .. code-block:: yaml

        driver:
          name: k3d
        platforms:
          - name: molecule-cluster

    .. code-block:: bash

        $ python3 -m pip install molecule[k3d]

    .. _`K3D`: https://k3d.io/
    """  # noqa

    def __init__(self, config=None):
        """Construct K3d."""
        super(K3d, self).__init__(config)
        self._name = "k3d"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login_cmd_template(self):
        return (
            "docker exec "
            "-e COLUMNS={columns} "
            "-e LINES={lines} "
            "-e TERM=bash "
            "-e TERM=xterm "
            "-ti k3d-{instance}-server-0 sh"
        )

    @property
    def default_safe_files(self):
        return []

    @property
    def default_ssh_connection_options(self):
        return []

    def login_options(self, instance_name):
        return {"instance": instance_name}

    def ansible_connection_options(self, instance_name):
        x = {"ansible_connection": "docker"}
        if "DOCKER_HOST" in os.environ:
            x["ansible_docker_extra_args"] = "-H={}".format(
                os.environ["DOCKER_HOST"]
            )
        return x

    def sanity_checks(self):
        pass

    def reset(self):
        pass
