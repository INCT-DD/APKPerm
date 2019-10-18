#!/usr/bin/env python3

__author__ = "Kocsen Chung"
# Setup Dependencies - PYTHON 3
# Downloads dependencies and gets them ready for the
# apk_decompiler.sh script

import shutil
import stat
import os
import sys
import zipfile
import urllib.request

if sys.version < '3':
    sys.exit("Please use Python3.")

# # Directory Variables ##
__DIR = os.path.dirname(os.path.realpath(__file__))
lib_dir = __DIR + "/lib"

# URLS for libraries
dex2jar_url = "https://github.com/pxb1988/dex2jar/releases/download/2.0/dex-tools-2.0.zip"
dex2jar_zip_destination = lib_dir + "/dex2jar.zip"
apktools_url = "https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.4.0.jar"
apktools_destination = lib_dir + "/apktool.jar"
jdcore_url = "https://clojars.org/repo/org/clojars/razum2um/jd-core-java/1.2/jd-core-java-1.2.jar"
jdcore_destination = lib_dir + "/jd-core-java.jar"


def main():
    """
    Main run.
    - Downloads, unzips and makes dex2jar executable
    - Downloads and renames apk-tools
    - Downloads and renames Procyon decompiler
    :return:
    """
    create_lib_dir()

    # ############
    # # Dex2Jar
    # ############
    print("Downloading dex2jar")
    urllib.request.urlretrieve(dex2jar_url, dex2jar_zip_destination)
    files_inzip = extract(dex2jar_zip_destination)
    # zip_name = os.path.basename(dex2jar_url).split(".zip")[0]
    # Rename dex2jar.#.#.# to dex2jar
    os.rename(lib_dir + "/" + files_inzip[0], lib_dir + "/dex2jar")
    # Remove the zip
    os.remove(dex2jar_zip_destination)
    make_dir_executable(lib_dir + "/dex2jar")

    # ############
    # # apktools
    # ############
    print("Downloading apktools")
    urllib.request.urlretrieve(apktools_url, apktools_destination)

    # ############
    # # jd-core-java
    # ############
    print("Downloading jd-core-java decompiler")
    urllib.request.urlretrieve(jdcore_url, jdcore_destination)

    print("Complete")


def extract(path_to_zip):
    """ Extract a zip """
    print("Extracting " + path_to_zip)
    with zipfile.ZipFile(path_to_zip, "r") as z:
        z.extractall(lib_dir)
        return z.namelist()


def create_lib_dir():
    """
    Creates a /lib directory in the working directory if it doesent already exist,
    if dir exists, deletes it and makes a new one.
    """
    if os.path.exists(lib_dir):
        print("Existing lib directory is being deleted...")
        shutil.rmtree(lib_dir)
    print("Creating new lib directory")
    os.makedirs(lib_dir)


def make_dir_executable(directory):
    """
    Makes .sh files in directory variable executable
    :param directory:
    :return: N/A
    """
    for file in os.listdir(directory):
        if ".sh" in file:
            full_path = "/".join([directory, file])
            st = os.stat(full_path)
            os.chmod(full_path, st.st_mode | stat.S_IEXEC)


if __name__ == "__main__":
    main()