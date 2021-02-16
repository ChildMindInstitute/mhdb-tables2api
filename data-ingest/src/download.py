import os
import sys
import numpy as np
import pandas as pd
import urllib.request as urllibrequest

mhdb_path = os.path.abspath(os.getcwd())

class Config():
    """convenience class for holding variables"""

    googlesheet_uids = { 
    'states':"11OkIWLwZYi9xkpuFODAKXQZHEFeMvYCQ8BTfIBKm0Z8", 
    'disorders':"13a0w3ouXq5sFCa0fBsg9xhWx67RGJJJqLjD_Oy1c3b0", 
    'resources':"1LeLlrsvBWMYTTIXTVtkynmBzzb0Uzi1OwpRLfyRAwzM", 
    'assessments':"1VUf3XnieYThY8OA6JWtpNP4zI2xa9xak9LXuyH_PaoE", 
    'sensors':"1ELaw79zmtmjmrg3J7slyoP-HXdfQRWa1Aqnbp50cmj8"
    }


def download_google_sheet(filepath, docid):
    """
    Download latest version of a Google Sheet
    Parameters
    ----------
    filepath : string
    docid : string
    Returns
    -------
    filepath : string
    """
    if not os.path.exists(os.path.abspath(os.path.dirname(filepath))):
        os.makedirs(os.path.abspath(os.path.dirname(filepath)))
    
    url = f"https://docs.google.com/spreadsheets/d/{docid}/export?format=xlsx"
    urllibrequest.urlretrieve(url, filepath)

    return filepath

def main():
  
    config = Config()

    for sheet_name, doc_id in config.googlesheet_uids.items():
        try:
            fpath  = f'../data/raw/{sheet_name}.xlsx'
            download_google_sheet(fpath, doc_id)
            print(f'downloaded {sheet_name} sheet with uid: {doc_id}')

        except:
            print(f'could not download: {sheet_name} with uid: {doc_id}')


if __name__ == '__main__':

    main()