import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "assets" not in listdir("ArnavX"):
        LOGGER(__name__).warning(
            f"Assets Folder not Found. Please clone repository again."
        )
        sys.exit()
    for file in os.listdir(ArnavX):
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir(ArnavX):
        mkdir("downloads")
    if "cache" not in listdir(ArnavX):
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
