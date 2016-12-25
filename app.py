import os

from pytube import YouTube

import logger
from progress_bar import print_status
from readconfig import *
from ui import Gui

"""youtube-downloader.py: A Youtube video downloader that downloads multiple videos from various sources simulatenously"""

__author__ = "Prajesh Ananthan"
__copyright__ = 'Copyright 2016 Prajesh Ananthan'
__license__ = 'MIT License'


# TODO: Ability to download videos at all resolution
# TODO: Download at least 3 videos simultaneously
# TODO: Unit testing for fail scenarios

def main():
    logger.INFO("##### Starting Multituber #####")

    user_interface = Gui()

    # TODO: Port config to GUI
    config = ConfigFile("D:/side_projects/multituber/config/multituber.conf")
    config.loadconfig()

    _download_path = config.getvalue('DOWNLOAD_PATH')
    _format = config.getvalue('FORMAT')
    _quality = config.getvalue('QUALITY')

    _links = user_interface.getlinks()

    createdirectory(_download_path)

    downloadvideos(_links, _download_path, _quality, _format)

    logger.INFO("Done. Videos downloaded: {}".format(len(_links)))
    logger.INFO("##### Shuting down Multituber #####")


def createdirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.DEBUG('{} created!'.format(directory))


def downloadvideos(videos, directory, quality, format):
    video = None
    for vid in videos:
        yt = YouTube(vid)
        logger.DEBUG('Downloading => [ {} | {} ]'.format(yt.filename, quality))
        video = yt.get(format, quality)
        video.download(directory, on_progress=print_status)
        print()


if __name__ == '__main__':
    main()