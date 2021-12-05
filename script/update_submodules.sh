#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# 更新各個submodule
cd ../sources
for file in ./*/*
do
    cd "$file"
    echo "$file"
    git fetch --all
    if [ "$file" = "./中原官話/棗莊話羅馬字輸入方案" ];
    then
        git reset --hard origin/棗莊話羅馬字輸入方案
        git pull origin 棗莊話羅馬字輸入方案
    elif [ "$file" = "./晉語/晋语汾阳话输入方案" ];
    then
        git reset --hard origin/main
        git pull origin main
    elif [ "$file" = "./吳語/溫州話" ];
    then
        git reset --hard origin/main
        git pull origin main
    elif [ "$file" = "./閩北語/建寧府羅馬字輸入法和閩北語輸入法" ];
    then
        git reset --hard origin/main
        git pull origin main
    elif [ "$file" = "./閩南語/台語方音輸入法" ];
    then
        git reset --hard origin/main
        git pull origin main
    else
        git reset --hard origin/master
        git pull origin master
    fi
    cd ../../
done

echo "done"
