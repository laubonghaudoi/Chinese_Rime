#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
讀取`source_info.yaml`中的信息，
將`sources`文件夾中的文件複製到對應的`download`文件夾。
配合`update_submodules.sh`可更新`download`文件夾中的碼表。
"""

import shutil

from pathlib import Path
import sys

import yaml

info = yaml.load(open("source_info.yaml", "r",
                      encoding="utf-8"), Loader=yaml.SafeLoader)

downloads = sys.argv[1:] or info.keys()
for download in downloads:
    if download not in info:
        raise KeyError(f"unknown download package: {download}")
    output_dir = Path("../download") / download
    output_dir.mkdir(parents=True, exist_ok=True)
    for file in output_dir.iterdir():
        if file.is_dir():
            shutil.rmtree(file)
        else:
            file.unlink()
    for file in info[download]["files"]:
        output_file = output_dir / file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(Path("../sources") / info[download]["source"] / file, output_file)
