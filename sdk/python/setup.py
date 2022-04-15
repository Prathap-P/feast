# Copyright 2019 The Feast Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import glob
import os
import pathlib
import re
import shutil
import subprocess
from distutils.cmd import Command
from pathlib import Path
from subprocess import CalledProcessError

from setuptools import find_packages

try:
    from setuptools import setup
    from setuptools.command.build_py import build_py
    from setuptools.command.develop import develop
    from setuptools.command.install import install
    from setuptools.dist import Distribution
except ImportError:
    from distutils.command.build_py import build_py
    from distutils.core import setup
    from distutils.dist import Distribution

NAME = "feast"
DESCRIPTION = "Python SDK for Feast"
URL = "https://github.com/feast-dev/feast"
AUTHOR = "Feast"
REQUIRES_PYTHON = ">=3.7.0"

REQUIRED = [
    "click>=7.0.0",
    "colorama>=0.3.9",
    "dill==0.3.*",
    "fastavro>=1.1.0",
    "google-api-core>=1.23.0",
    "googleapis-common-protos==1.52.*",
    "grpcio>=1.34.0",
    "grpcio-reflection>=1.34.0",
    "Jinja2>=2.0.0",
    "jsonschema",
    "mmh3",
    "pandas>=1.0.0",
    "pandavro==1.5.*",
    "protobuf>=3.10,<3.20",
    "proto-plus<1.19.7",
    "pyarrow>=4.0.0",
    "pydantic>=1.0.0",
    "PyYAML>=5.4.*",
    "tabulate==0.8.*",
    "tenacity>=7.*",
    "toml==0.10.*",
    "tqdm==4.*",
    "fastapi>=0.68.0",
    "uvicorn[standard]>=0.14.0",
    "proto-plus<1.19.7",
    "tensorflow-metadata>=1.0.0,<2.0.0",
    "dask>=2021.*,<2022.02.0",
]

GCP_REQUIRED = [
    "google-cloud-bigquery>=2,<3",
    "google-cloud-bigquery-storage >= 2.0.0",
    "google-cloud-datastore>=2.1.*",
    "google-cloud-storage>=1.34.*,<1.41",
    "google-cloud-core>=1.4.0,<2.0.0",
]

REDIS_REQUIRED = [
    "redis==4.2.2",
    "hiredis>=2.0.0",
]

AWS_REQUIRED = [
    "boto3>=1.17.0",
    "docker>=5.0.2",
]

SNOWFLAKE_REQUIRED = [
    "snowflake-connector-python[pandas]>=2.7.3",
]

SPARK_REQUIRED = [
    "pyspark>=3.0.0",
]

TRINO_REQUIRED = [
    "trino>=0.305.0,<0.400.0",
]

GE_REQUIRED = [
    "great_expectations>=0.14.0,<0.15.0"
]

CI_REQUIRED = (
    [
        "cryptography==3.4.8",
        "flake8",
        "black==19.10b0",
        "isort>=5",
        "grpcio-tools==1.44.0",
        "grpcio-testing==1.44.0",
        "minio==7.1.0",
        "mock==2.0.0",
        "moto",
        "mypy==0.931",
        "mypy-protobuf==3.1",
        "avro==1.10.0",
        "gcsfs",
        "urllib3>=1.25.4",
        "psutil==5.9.0",
        "pytest>=6.0.0",
        "pytest-cov",
        "pytest-xdist",
        "pytest-benchmark>=3.4.1",
        "pytest-lazy-fixture==0.6.3",
        "pytest-timeout==1.4.2",
        "pytest-ordering==0.6.*",
        "pytest-mock==1.10.4",
        "Sphinx!=4.0.0,<4.4.0",
        "sphinx-rtd-theme",
        "testcontainers>=3.5",
        "adlfs==0.5.9",
        "firebase-admin==4.5.2",
        "pre-commit",
        "assertpy==1.1",
        "pip-tools",
        "pybindgen",
        "types-protobuf",
        "types-python-dateutil",
        "types-pytz",
        "types-PyYAML",
        "types-redis",
        "types-requests",
        "types-setuptools",
        "types-tabulate",
    ]
        + GCP_REQUIRED
        + REDIS_REQUIRED
        + AWS_REQUIRED
        + SNOWFLAKE_REQUIRED
        + SPARK_REQUIRED
        + TRINO_REQUIRED
        + GE_REQUIRED
)

DEV_REQUIRED = ["mypy-protobuf==3.1", "grpcio-testing==1.*"] + CI_REQUIRED

# Get git repo root directory
repo_root = str(pathlib.Path(__file__).resolve().parent.parent.parent)

# README file from Feast repo root directory
README_FILE = os.path.join(repo_root, "README.md")
with open(README_FILE, "r", encoding="utf8") as f:
    LONG_DESCRIPTION = f.read()

# Add Support for parsing tags that have a prefix containing '/' (ie 'sdk/go') to setuptools_scm.
# Regex modified from default tag regex in:
# https://github.com/pypa/setuptools_scm/blob/2a1b46d38fb2b8aeac09853e660bcd0d7c1bc7be/src/setuptools_scm/config.py#L9
TAG_REGEX = re.compile(
    r"^(?:[\/\w-]+)?(?P<version>[vV]?\d+(?:\.\d+){0,2}[^\+]*)(?:\+.*)?$"
)

# Only set use_scm_version if git executable exists (setting this variable causes pip to use git under the hood)
if shutil.which("git"):
    use_scm_version = {"root": "../..", "relative_to": __file__, "tag_regex": TAG_REGEX}
else:
    use_scm_version = None

PROTO_SUBDIRS = ["core", "serving", "types", "storage"]


class BuildPythonProtosCommand(Command):
    description = "Builds the proto files into Python files."
    user_options = []

    def initialize_options(self):
        self.python_protoc = [
            "python",
            "-m",
            "grpc_tools.protoc",
        ]  # find_executable("protoc")
        self.proto_folder = os.path.join(repo_root, "protos")
        self.python_folder = os.path.join(
            os.path.dirname(__file__) or os.getcwd(), "feast/protos"
        )
        self.sub_folders = PROTO_SUBDIRS

    def finalize_options(self):
        pass

    def _generate_python_protos(self, path: str):
        proto_files = glob.glob(os.path.join(self.proto_folder, path))
        Path(self.python_folder).mkdir(exist_ok=True)
        subprocess.check_call(
            self.python_protoc
            + [
                "-I",
                self.proto_folder,
                "--python_out",
                self.python_folder,
                "--grpc_python_out",
                self.python_folder,
                "--mypy_out",
                self.python_folder,
            ]
            + proto_files,
        )

    def run(self):
        for sub_folder in self.sub_folders:
            self._generate_python_protos(f"feast/{sub_folder}/*.proto")
            # We need the __init__ files for each of the generated subdirs
            # so that they are regular packages, and don't need the `--namespace-packages` flags
            # when being typechecked using mypy. BUT, we need to exclude `types` because that clashes
            # with an existing module in the python standard library.
            if sub_folder == "types":
                continue
            with open(f"{self.python_folder}/feast/{sub_folder}/__init__.py", 'w'):
                pass

        with open(f"{self.python_folder}/__init__.py", 'w'):
            pass
        with open(f"{self.python_folder}/feast/__init__.py", 'w'):
            pass

        for path in Path("feast/protos").rglob("*.py"):
            for folder in self.sub_folders:
                # Read in the file
                with open(path, "r") as file:
                    filedata = file.read()

                # Replace the target string
                filedata = filedata.replace(
                    f"from feast.{folder}", f"from feast.protos.feast.{folder}"
                )

                # Write the file out again
                with open(path, "w") as file:
                    file.write(filedata)


def _generate_path_with_gopath():
    go_path = subprocess.check_output(["go", "env", "GOPATH"]).decode("utf-8")
    go_path = go_path.strip()
    path_val = os.getenv("PATH")
    path_val = f"{path_val}:{go_path}/bin"

    return path_val


def _ensure_go_and_proto_toolchain():
    try:
        version = subprocess.check_output(["go", "version"])
    except Exception as e:
        raise RuntimeError("Unable to find go toolchain") from e

    semver_string = re.search(r"go[\S]+", str(version)).group().lstrip("go")
    parts = semver_string.split(".")
    if not (int(parts[0]) >= 1 and int(parts[1]) >= 16):
        raise RuntimeError(f"Go compiler too old; expected 1.16+ found {semver_string}")

    path_val = _generate_path_with_gopath()

    try:
        subprocess.check_call(["protoc-gen-go", "--version"], env={
            "PATH": path_val
        })
        subprocess.check_call(["protoc-gen-go-grpc", "--version"], env={
            "PATH": path_val
        })
    except Exception as e:
        raise RuntimeError("Unable to find go/grpc extensions for protoc") from e


class BuildGoProtosCommand(Command):
    description = "Builds the proto files into Go files."
    user_options = []

    def initialize_options(self):
        self.go_protoc = [
            "python",
            "-m",
            "grpc_tools.protoc",
        ]  # find_executable("protoc")
        self.proto_folder = os.path.join(repo_root, "protos")
        self.go_folder = os.path.join(repo_root, "go/protos")
        self.sub_folders = PROTO_SUBDIRS
        self.path_val = _generate_path_with_gopath()

    def finalize_options(self):
        pass

    def _generate_go_protos(self, path: str):
        proto_files = glob.glob(os.path.join(self.proto_folder, path))

        try:
            subprocess.check_call(
                self.go_protoc
                + ["-I", self.proto_folder,
                   "--go_out", self.go_folder,
                   "--go_opt=module=github.com/feast-dev/feast/go/protos",
                   "--go-grpc_out", self.go_folder,
                   "--go-grpc_opt=module=github.com/feast-dev/feast/go/protos"]
                + proto_files,
                env={
                    "PATH": self.path_val
                }
            )
        except CalledProcessError as e:
            print(f"Stderr: {e.stderr}")
            print(f"Stdout: {e.stdout}")

    def run(self):
        go_dir = Path(repo_root) / "go" / "protos"
        go_dir.mkdir(exist_ok=True)
        for sub_folder in self.sub_folders:
            self._generate_go_protos(f"feast/{sub_folder}/*.proto")


class BuildGoEmbeddedCommand(Command):
    description = "Builds Go embedded library"
    user_options = []

    def initialize_options(self) -> None:
        self.path_val = _generate_path_with_gopath()

        self.go_env = {}
        for var in ("GOCACHE", "GOPATH"):
            self.go_env[var] = subprocess \
                .check_output(["go", "env", var]) \
                .decode("utf-8") \
                .strip()

    def finalize_options(self) -> None:
        pass

    def _compile_embedded_lib(self):
        print("Compile embedded go")
        subprocess.check_call([
            "gopy",
            "build",
            "-output",
            "feast/embedded_go/lib",
            "-vm",
            "python3",
            "-no-make",
            "github.com/feast-dev/feast/go/embedded"
        ], env={
            "PATH": self.path_val,
            "CGO_LDFLAGS_ALLOW": ".*",
            **self.go_env,
        })

    def run(self):
        self._compile_embedded_lib()


class BuildCommand(build_py):
    """Custom build command."""

    def run(self):
        self.run_command("build_python_protos")
        if os.getenv("COMPILE_GO", "false").lower() == "true":
            _ensure_go_and_proto_toolchain()
            self.run_command("build_go_protos")
            self.run_command("build_go_lib")
        build_py.run(self)


class DevelopCommand(develop):
    """Custom develop command."""

    def run(self):
        self.run_command("build_python_protos")
        if os.getenv("COMPILE_GO", "false").lower() == "true":
            _ensure_go_and_proto_toolchain()
            self.run_command("build_go_protos")
            self.run_command("build_go_lib")
        develop.run(self)


class BinaryDistribution(Distribution):
    """Distribution which forces a binary package with platform name
     when go compilation is enabled"""
    def has_ext_modules(self):
        return os.getenv("COMPILE_GO", "false").lower() == "true"


setup(
    name=NAME,
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    install_requires=REQUIRED,
    # https://stackoverflow.com/questions/28509965/setuptools-development-requirements
    # Install dev requirements with: pip install -e .[dev]
    extras_require={
        "dev": DEV_REQUIRED,
        "ci": CI_REQUIRED,
        "gcp": GCP_REQUIRED,
        "aws": AWS_REQUIRED,
        "redis": REDIS_REQUIRED,
        "snowflake": SNOWFLAKE_REQUIRED,
        "spark": SPARK_REQUIRED,
        "trino": TRINO_REQUIRED,
        "ge": GE_REQUIRED,
    },
    include_package_data=True,
    license="Apache",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ["feast=feast.cli:cli"]},
    use_scm_version=use_scm_version,
    setup_requires=[
        "setuptools_scm",
        "grpcio",
        "grpcio-tools==1.44.0",
        "mypy-protobuf==3.1",
        "sphinx!=4.0.0",
    ],
    package_data={
        "": [
            "protos/feast/**/*.proto",
            "protos/feast/third_party/grpc/health/v1/*.proto",
            "feast/protos/feast/**/*.py",
        ],
    },
    cmdclass={
        "build_python_protos": BuildPythonProtosCommand,
        "build_go_protos": BuildGoProtosCommand,
        "build_go_lib": BuildGoEmbeddedCommand,
        "build_py": BuildCommand,
        "develop": DevelopCommand,
    },
    distclass=BinaryDistribution,  # generate wheel with platform-specific name
)
