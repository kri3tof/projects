import os
import fnmatch
import zipfile
import subprocess
import shutil
import requests
import re

url = 'http://whdownload.com/games.php?name=%&sort=0&dir=0'
home_url = "http://whdownload.com/"
pattern = re.compile(r'<td><a\shref="(.+?)">', re.S)
r = requests.get(url)
links = re.findall(pattern, r.text)

for link in links:
    print "Downloading: %s" % link
    r = requests.get("%s%s" % (home_url, link))
    f = open(link.split('/')[-1], 'wb')
    f.write(r.content)

patterns_to_delete = [
    "*_CD32*.*",
    "*_CDTV*.*",
    "*_NTSC*.*",
    "*_De*.*",
    "*_Fr*.*",
    "*_It*.*"
]

for root, dirs, files in os.walk("."):
    for pattern in patterns_to_delete:
        for filename in fnmatch.filter(files, pattern):
            filepath = os.path.join(root, filename)
            print(f"Usuwam plik: {filepath}")
            os.remove(filepath)

if os.path.isfile("EmeraldMines_v1.zip"):
    print("Usuwam EmeraldMines_v1.zip")
    os.remove("EmeraldMines_v1.zip")

for filename in os.listdir("."):
    if filename.endswith(".zip"):
        zip_dir = os.path.splitext(filename)[0]
        os.makedirs(zip_dir, exist_ok=True)
        try:
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(zip_dir)
            print(f"Rozpakowano {filename} do {zip_dir}, usuwam archiwum...")
            os.remove(filename)
        except zipfile.BadZipFile:
            print(f"Nieprawidlowe archiwum ZIP: {filename}")

for filename in os.listdir("."):
    if filename.endswith(".lha"):
        lha_dir = os.path.splitext(filename)[0]
        os.makedirs(lha_dir, exist_ok=True)
        try:
            result = subprocess.run(["lha", f"-xw={lha_dir}", filename], check=True)
            print(f"Rozpakowano {filename} do {lha_dir}, usuwam archiwum...")
            os.remove(filename)
        except subprocess.CalledProcessError:
            print(f"Blad podczas rozpakowywania pliku LHA: {filename}")

