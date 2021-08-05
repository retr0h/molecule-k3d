# molecule-k3d

[![Unit Test](https://github.com/retr0h/molecule-k3d/actions/workflows/unit.yml/badge.svg)](https://github.com/retr0h/molecule-k3d/actions/workflows/unit.yml)
[![Lint](https://github.com/retr0h/molecule-k3d/actions/workflows/lint.yml/badge.svg)](https://github.com/retr0h/molecule-k3d/actions/workflows/lint.yml)

molecule-k3d - Molecule k3d Driver allows Molecule users to test Ansible code using k3d.

## Dependencies

* [k3d][]

## Installing

    $ pip install molecule-k3d

## Usage

    $ molecule init scenario -d k3d
    $ molecule test

Be sure to set the following env vars, where `$instance`, is the name
of the platform specified in `molecule.yml`.

    platforms:
      - name: instance
    provisioner:
      name: ansible
      env:
        K8S_AUTH_KUBECONFIG: ~/.k3d/kubeconfig-$instance.yaml
        KUBECONFIG: ~/.k3d/kubeconfig-$instance.yaml

## Testing

To execute unit tests.

    $ make dep
    $ make test

## License

The [MIT] License.

[k3d]: https://k3d.io/
[MIT]: LICENSE
