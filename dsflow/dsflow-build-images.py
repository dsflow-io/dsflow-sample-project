import sys
import os
import subprocess

from python_scripts.custom_libraries.cli_utils import validate_env

validate_env()

DSFLOW_ROOT = os.environ["DSFLOW_ROOT"]

# TODO: automatically find all images in dsflow/docker/

args = ["docker-compose",
        "-f", DSFLOW_ROOT + "/docker/adminer/docker-compose.yaml",
        "-f", DSFLOW_ROOT + "/docker/base/docker-compose.yaml",
        "-f", DSFLOW_ROOT + "/docker/dsflow-job-generator/docker-compose.yaml"
        ]

my_env = os.environ.copy()

# preview
subprocess.call(args + ["config"], env=my_env)

# build
subprocess.call(args + ["build"], env=my_env)
