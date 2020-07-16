import os
from datetime import datetime

with os.scandir() as dir_entries:
    os.mkdir(".\\Sorted")
    for entry in dir_entries:
        if str(entry.name).endswith(".jpg") or str(entry.name).endswith(".JPG") or str(entry.name).endswith(".mp4") or str(entry.name).endswith(".MP4"):
            casVytvorenia = entry.stat().st_mtime
            try:
                nazovPriecinku = ".\\Sorted\\" + datetime.utcfromtimestamp(casVytvorenia).strftime('%Y-%m-%d')
                os.mkdir(nazovPriecinku)
            except: pass
            finally:
                nazovSuboru = nazovPriecinku + "\\" + entry.name
                os.replace(entry.path, nazovSuboru)