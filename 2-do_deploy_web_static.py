#!/usr/bin/python3
"""
AirBnB clone - Deploy static, Deploy archive!
"""
from datetime import datetime
from fabric.api import *
import shlex
import os

env.hosts = ['18.214.88.235', '100.25.103.162']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Distributes archive to the web servers
    Retruns:
        (bool): `True` if all operations successful, `False` otherwise
    """
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        wname = name.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(name)

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(releases_path))
        run("sudo tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("sudo rm {}".format(tmp_path))
        run("sudo mv {}web_static/* {}".format(releases_path, releases_path))
        run("sudo rm -rf {}web_static".format(releases_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except Exception as ex:
        return False
