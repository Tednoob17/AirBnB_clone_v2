#!/usr/bin/python3
"""Packs web_static into a .tgz archive"""

import os
from fabric.api import local
from datetime import datetime


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
