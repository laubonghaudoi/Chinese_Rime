#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# 更新各個submodule
cd ../sources
for file in ./*/*
do
    cd "$file"
    if [ "$file" = "./中原官話/棗莊話羅馬字輸入方案" ];
    then
        git fetch --all
        git reset --hard origin/棗莊話羅馬字輸入方案
        git pull origin 棗莊話羅馬字輸入方案
    else
        git fetch --all
        git reset --hard origin/master
        git pull origin master
    fi
    cd ../../
done

echo "done"
