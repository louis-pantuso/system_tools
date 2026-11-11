#!/bin/python
from pathlib import Path
import sys 
from datetime import datetime,date 
import subprocess
today = date.today()

Notebook = Path('/home/louis/Notebook')


if not len(sys.argv) == 2:
    print("Please provide a filename") 
    sys.exit(1) 

filename= sys.argv[1]
mfile = filename + ".md" 

with open(mfile,'w') as file: 
    file.write(f"# {filename.title()}\n\n\n")
    file.write(f"## Date: {today}\n\n\n\n\n") 
    
subprocess.run(["nvim", "+", mfile]) 

Path(mfile).rename(Notebook/mfile)

subprocess.run(["notify-send",f"{mfile} moved successfully"])
