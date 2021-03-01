import os, zipfile
import json

from datetime import date
from dateutil.relativedelta import relativedelta

def getFilelist(foldername):
    filelist = []

    for dirname, _, filenames in os.walk(foldername):
        for filename in filenames:
            filelist.append(os.path.join(dirname, filename))

    return filelist

def createfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)    

def unzipfolder(folder, req_ext='.csv'):
    zipfilelist = [filename for filename in getFilelist(folder) if filename.endswith('.zip')]

    for filename in zipfilelist: # loop through items in dir
        zip_ref = zipfile.ZipFile(filename) # create zipfile object
        zip_ref.extractall(folder) # extract file to dir
        zip_ref.close() # close file

    removeList = [filename for filename in getFilelist(folder) if not filename.endswith(req_ext)]
    for filename in removeList:
        os.remove(filename) # delete zipped file    


def read_json(filepath):
    with open(filepath) as f:
        data = json.load(f)

    return data