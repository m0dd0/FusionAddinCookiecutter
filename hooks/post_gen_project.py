# pylint:disable=subprocess-run-check

import subprocess

subprocess.run(["git", "init"])
subprocess.run(["git", "checkout", "-b", "main"])
subprocess.run(
    [
        "git",
        "submodule",
        "add",
        "-b",
        "develop",
        "https://github.com/m0dd0/fusion_addin_framework.git",
    ],
    cwd="./{{cookiecutter.addin_name}}/libs",
)
# git submodule update --init --recursive
subprocess.run(["git", "add", "*"])
subprocess.run(
    [
        "git",
        "commit",
        "-a",
        "-m",
        "Created ready to use template with https://github.com/m0dd0/FusionAddinBase",
    ]
)
