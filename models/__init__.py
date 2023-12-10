#!/usr/bin/python3
""" Initialize Module Package and reload object from Storage Engine """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
