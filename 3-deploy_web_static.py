#!/usr/bin/python3
"""Deploy archive to web servers"""
import os
from fabric.api import local, env, run, put
from datetime import datetime

# env.hosts = ['35.231.156.161', '34.73.64.44']
env.user = 'ubuntu'


def do_pack():
    """Packs web_static into a .tgz archive
    Returns:
        The archive path if the archive has been correctly generated
        None if the archive has not been generated
    """
    if not os.path.exists("versions"):
        local("mkdir versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_name = "versions/web_static_{}.tgz".format(date)
    command = "tar -cvzf {} {}".format(tgz_name, "web_static")
    output = local(command)
    if not output.failed:
        return tgz_name
    return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers
    Args:
        archive_path (str): Path to the archive
    Returns:
        False if the file at the path archive_path doesn’t exist
        True if all operations have been done correctly, otherwise False
    """
    if not archive_path or not os.path.exists(archive_path):
        return False
    put(archive_path, '/tmp')
    tgz_name = archive_path[archive_path.find("/") + 1: -4]
    try:
        run('mkdir -p /data/web_static/releases/{}/'.format(tgz_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
                tgz_name, tgz_name
        ))
        run('rm /tmp/{}.tgz'.format(tgz_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(
                tgz_name, tgz_name
        ))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            tgz_name
        ))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(
            tgz_name
        ))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to your web servers
    Returns:
        False if the file at the path archive_path doesn’t exist
        True if all operations have been done correctly, otherwise False
    """
    pack = do_pack()
    if pack:
        return do_deploy(pack)
    return False
