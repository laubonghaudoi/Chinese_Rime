#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# 更新各個submodule
branch_mains=("./中古漢語/切韻拼音","./晉語/晋语汾阳话输入方案","./吳語/溫州話","./閩北語/建寧府羅馬字輸入法和閩北語輸入法","./閩南語/台語方音輸入法","./湘語/邵東話輸入方案","./上古漢語/上古漢語輸入方案集")
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
    elif [[ "${branch_mains[*]}"  =~ "${file}" ]];
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
