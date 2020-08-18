#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
     from the contents of the web_static folder of
     your AirBnB Clone repo, using the function do_pack.
"""
from fabric import api
import os.path
from datetime import datetime


def do_pack():
     """ script that generates a .tgz archive
     from the contents of the web_static"""
     with api.settings(warn_only=True):
          isdir = os.path.isdir('versions')
          if not isdir:
               mkdir = api.local('mkdir versions')
               if mkdir.failed:
                    return None
          suffix = datetime.now().strftime('%Y%m%d%M%S')
          path = 'versions/web_static_{}.tgz'.format(suffix)
          tar = api.local('tar -cvzf {} web_static'.format(path))
          if tar.failed:
               return None
          size = os.stat(path).st_size
          print('web_static packed: {} -> {}Bytes'.format(path, size))
          return path
