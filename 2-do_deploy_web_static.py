#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents

from fabric import api
from datetime import datetime
from fabric.contrib import files
import os


api.env.hosts = ['34.74.130.170', '34.235.167.111']
api.env.key_filename = '~/.ssh/holberton'
api.env.user = 'ubuntu'


def do_deploy(archive_path):
    """do_deploy method"""
    if not os.path.isfile(archive_path):
        return False
    with api.cd('/tmp'):
        base = os.path.basename(archive_path)
        root, ext = os.path.splitext(base)
        outpath = '/data/web_static/releases/{}'.format(root)
        try:
            putpath = api.put(archive_path)
            if files.exists(outpath):
                api.run('rm -rdf {}'.format(outpath))
            api.run('sudo mkdir -p {}'.format(outpath))
            api.run('sudo tar -xzf {} -C {}'.format(putpath[0], outpath))
            api.run('sudo rm -f {}'.format(putpath[0]))
            api.run('sudo mv -u {}/web_static/* {}'.format(outpath, outpath))
            api.run('sudo rm -rf {}/web_static'.format(outpath))
            api.run('sudo rm -rf /data/web_static/current')
            api.run('sudo ln -sf {} /data/web_static/current'.format(outpath))
            print('New version deployed!')
        except:
            return False
        else:
            return True
