#!/bin/python

from requests import get
from subprocess import run
from glob import glob
from os import chdir, makedirs
from os.path import exists
from re import search
from shutil import rmtree

def downloadFile(url, path):
    rmtree(path)
    run(['wget','-P', path, url])

def getVersion():
    res = get('https://rufus.ie/it/#')
    x = search(r'rufus-(\d.\d).exe', res.text)
    return x.group(1)

print('---rufus.py---')
version = getVersion()
path='download/rufus/'
if not exists(path):
    makedirs(path)

try:
    with open('version/rufus-version.txt', 'r+') as file:
        if file.read() != version:
            file.truncate(0)
            file.write(version)
            downloadFile(f'https://github.com/pbatard/rufus/releases/download/v{version}/rufus-{version}.exe', path)
except FileNotFoundError:
    with open('version/rufus-version.txt', 'w') as file:
        file.write(version)
        downloadFile(f'https://github.com/pbatard/rufus/releases/download/v{version}/rufus-{version}.exe')