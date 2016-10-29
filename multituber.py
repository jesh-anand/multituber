from pytube import YouTube
from ui import Gui
import logger
import os
import winsound
from readconfig import *
from progress_bar import print_status

"""youtube-downloader.py: A Youtube video downloader that downloads multiple videos from various sources simulatenously"""

__author__ = "Prajesh Ananthan"
__copyright__ = "Copyright 2016, Python"
__license__ = "GPL"


# TODO: To have flexible approach to download videos at all resolution
# TODO: To download multiple videos simultanously
# TODO: Style GUI with proper positioning
# TODO: Port dependencies to local without pip import

def main():
    logger.INFO("##### Starting Multituber #####")

    user_interface = Gui()
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

    winsound.Beep(440, 100)  # frequency, duration


if __name__ == '__main__':
    main()
