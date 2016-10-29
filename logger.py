from time import strftime

"""logger.py: A simple logging module"""

__author__ = "Prajesh Ananthan"
__copyright__ = "Copyright 2016, Python"
__license__ = "GPL"


def DEBUG(text):
    print(strftime('%d/%b/%Y %H:%M:%S DEBUG | {}'.format(text)))


def INFO(text):
    print(strftime('%d/%b/%Y %H:%M:%S INFO | {}'.format(text)))


def WARNING(text):
    print(strftime('%d/%b/%Y %H:%M:%S WARNING | {}'.format(text)))


def ERROR(text):
    print(strftime('%d/%b/%Y %H:%M:%S ERROR | {}'.format(text)))
