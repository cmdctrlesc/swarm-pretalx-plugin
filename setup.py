import os
from distutils.command.build import build

from django.core import management
from setuptools import find_packages, setup

try:
    with open(
        os.path.join(os.path.dirname(__file__), "README.rst"), encoding="utf-8"
    ) as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""


class CustomBuild(build):
    def run(self):
        management.call_command("compilemessages", verbosity=1)
        build.run(self)


cmdclass = {"build": CustomBuild}


setup(
    name="swarm-plugin",
    version="0.1.5",
    description="Pretalx plugin for exporting the agenda to Swarm",
    long_description=long_description,
    url="https://github.com/cmdctrlesc/swarm-pretalx-plugin",
    author="cmdctrlesc",
    author_email="alanxyz210@gmail.com",
    license="Apache Software License",
    install_requires=[],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretalx.plugin]
swarm_pretalx=swarm_pretalx:PretalxPluginMeta
""",
)
