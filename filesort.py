#!/bin/python 

from pathlib import Path 
from datetime import datetime,date


Downloads = Path.home()/"Downloads" 
Pictures = Path.home()/"Pictures" 
Documents = Path.home()/"Documents"
Videos = Path.home()/"Videos"
Archives = Path.home()/"Archives"




now = datetime.now()


EXT_MAP = {
    # Pictures
    ".jpg":  Pictures,
    ".jpeg": Pictures,
    ".png":  Pictures,
    ".gif":  Pictures,
    ".webp": Pictures,
    ".bmp":  Pictures,

    # Documents
    ".pdf":  Documents,
    ".txt":  Documents,
    ".docx": Documents,
    ".doc":  Documents,

    # Video
    ".mp4":  Videos,
    ".mkv":  Videos,
    ".mov":  Videos,
 
    # Archives
    ".zip":  Archives,
    ".rar":  Archives,
    ".7z":   Archives
    }




with open(Downloads/"logfile.txt",'a') as file: 
    for item in Downloads.iterdir(): 
        if item.is_dir(): 
        # Move the directory to a folder in home called unsorted
            pass  
        elif item.is_file() and item.name != "logfile.txt":
            ext = item.suffix
        
            if ext in EXT_MAP:
                file.write(f"{item.name} moved to {EXT_MAP[ext]} at {now}\n")
                item.rename(EXT_MAP[ext]/item.name)
