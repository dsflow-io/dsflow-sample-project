import sys
import os
import subprocess

from python_scripts.custom_libraries.cli_utils import validate_env

validate_env()

DSFLOW_ROOT = os.environ["DSFLOW_ROOT"]
DSFLOW_WORKSPACE = os.environ["DSFLOW_WORKSPACE"]

docker_compose_base_file = DSFLOW_ROOT + "/docker/base/docker-compose.yaml"

my_env = os.environ.copy()

args = ["docker-compose",
        "-f", docker_compose_base_file
        ]

if len(sys.argv) > 1 and sys.argv[1] == "--verbose":
    print("Rendered docker compose file:")
    subprocess.call(args + ["config"], env=my_env)
    print("base args: ", " ".join(args))

print("=== calling docker-compose ===")
call_result = subprocess.call(args + ["up", "-d"], env=my_env)

if call_result == 0:
    print("\n=== dsflow instructions ===")
    print("Open jupyter notebooks in your browser at http://localhost:8888/")
    print("Password is green3")
    print("\nHINTS:")
    print("- Call `dsflow stop-all` to stop docker containers.")
    print("- Call `dsflow` to show list of available commands.")
else:
    print("\n=== something went wrong ===")
    print("Reach out to pm@dsflow.io")
