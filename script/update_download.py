#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
讀取`source_info.yaml`中的信息，
將`sources`文件夾中的文件複製到對應的`download`文件夾。
配合`update_submodules.sh`可更新`download`文件夾中的碼表。
"""
import yaml, shutil
info = yaml.load(open("source_info.yaml", "r", encoding="utf-8"), Loader=yaml.SafeLoader)
for dowload in info.keys():
    for file in info[dowload]["files"]:
        shutil.copy("../sources/"+info[dowload]["source"]+file, "../download/"+dowload)
