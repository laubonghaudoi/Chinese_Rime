#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
讀取`source_info.yaml`中的信息，
將`sources`文件夾中的文件複製到對應的`download`文件夾。
配合`update_submodules.sh`可更新`download`文件夾中的碼表。
"""

import os

import shutil

import yaml

info = yaml.load(open("source_info.yaml", "r",
                      encoding="utf-8"), Loader=yaml.SafeLoader)

for download in info.keys():
    for file in os.listdir(f"../download/{download}"):
        os.remove(f"../download/{download}/" + file)
    for file in info[download]["files"]:
        shutil.copy("../sources/"+info[download]
                    ["source"]+file, "../download/"+download)
