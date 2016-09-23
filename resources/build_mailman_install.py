#!/usr/bin/python3

import os
import shutil
import subprocess

# Install mailman as far as possible without /var/ volume to speed up
# container startup later:

os.mkdir("/mailman-venv")
python3_version = "python3"
if "extra_mailman_python_version" in os.environ:
    python3_version = "python" + os.environ[
        "extra_mailman_python_version"]
subprocess.check_output(["bash",
    "-c", "source /root/.bashrc; virtualenv /mailman-venv"])

os.mkdir("/opt/mailman/")
subprocess.check_output(["git",
    "clone",
    "https://gitlab.com/mailman/mailman-bundler.git"])
os.chdir("/opt/mailman/mailman-bundler/")
subprocess.check_output(["buildout"])

shutil.copytree("/opt/mailman/mailman-bundler/var/",
    "/opt/mailman/mailman-bundler-var-default")

