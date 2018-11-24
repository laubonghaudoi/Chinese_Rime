# Rime输入法汉语方言拼音方案全集

**[简体中文](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#rime%E8%BE%93%E5%85%A5%E6%B3%95%E6%B1%89%E8%AF%AD%E6%96%B9%E8%A8%80%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88%E5%85%A8%E9%9B%86)    [正體中文](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#rime%E8%BC%B8%E5%85%A5%E6%B3%95%E6%BC%A2%E8%AA%9E%E6%96%B9%E8%A8%80%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88%E5%85%A8%E9%9B%86)    [English](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#collection-of-rime-input-method-schemas-for-chinese-dialects)**

## 项目宗旨

本仓库收集现代汉语各大方言及上古、中古汉语的Rime字库和拼音输入方案。本项目的宗旨是为汉语非普通话使用者提供实用的拼音输入方案，解决被迫使用普通话输入法的困难，并为现代汉语方言、古汉语学习者提供实用便利的学习工具以及为语言学界学术研究提供参考资料。

本仓库分为两部分：`data/`路径下为各个输入方案的来源仓库，以submodule的形式保存，方便方案作者实时更新自己的方案。由于部分方案不存在于Github，故此路径下方案收录不完整，`download/`路径下为已收录所有方案的下载版，可直接部署使用。我会检查`data/`下各个方案的更新情况并将最新版本方案覆盖至`download/`中，确保直接下载的方案为最新版本。

## 使用教程

若要在自己的Rime输入法中添加某一输入方案，只需将该方案的`.dict.yaml`和`.schema.yaml`文件复制到用户文件夹下，然后在`default.yaml`中添加方案名称，再重新部署即可。

例如使用Win10系统下的PIME输入法，要添加上古全拼输入方案`dkzp`，则只需将`dkzp.dict.yaml`和`dkzp.schema.yaml`两个文件复制到路径`C:\Users\用户名\AppData\Roaming\PIME\Rime`下，然后打开该路径下的`default.yaml`，在`schema_list:`后加入`- schema: dkzp`，如下：

```yaml
schema_list:
  - schema: XXX
  - schema: YYY
  - schema: dkzp
```

保存后重新部署，再按Ctrl+`即可在菜单中选择上古全拼方案。

Linux、OS X与其他Windows版本系统下操作同理。

## 已收录方案

目前**主要缺失闽北语、蒲仙语、平语、湘语、赣语、徽语、西南官话、兰银官话、江淮官话、胶辽官话**的输入方案，如有作者已编写以上语言的输入方案，欢迎联系我添加收录。其他汉语或域外方音的方案亦强烈欢迎。

- 上古汉语
    - 上古全拼 - `dkzp`
- 中古汉语
    - 中古全拼 - `zyenpheng`
    - 中古三拼 - `triungkoxsampheng`
    - 中古四拼 - `deuqguv4`
    - 廣韻羅馬字 - `kuankhiunn`
    - 爾切羅馬字 - `nieh_ched`
    - 廣韻查詢 - `middle_chinese_lookup`
    - 唐韻 - `Dangrvond`
    - 廣韻段毄攴字法 - `kmg`
- 粤语
    - 粤拼
        - 粵拼 - `jyutping`
        - 耶魯粵語拼音 - `yale`
        - 香港廣東話拼音 - `hkcantonese`
    - 粵拼⁺ - `jyutping+`
    - 粵語注音 - `zyujam`
    - 袖珍粵拼 - `jyutping_compact`
    - 耶鲁粤语拼音 - `yale`
    - 梧州白話 - `NgZjau_JyutPing`
    - 沟漏片藤县白话输入方案 - `jutjnyu_gaulaupin_dangjunbikwaa`
    - 貴州韻 - `gvaizauvan`
- 闽语
    - 泉漳閩南語輸入方案
        - 廈腔閩南語 - `blg_ha`
        - 臺灣閩南語 - `blg_tai`
        - 漳腔閩南語 - `blg_tsiang`
        - 泉腔閩南語 - `blg_tsuan`
    - 閩南語廈台腔專用版 - `blg_etai`
    - 閩倂輸入灋 - `mp`
    - 潮语拼音输入法
        - 潮語拼音〔潮州〕 - `dieziu`
        - 潮語拼音〔潮阳〕 - `dioion`
        - 潮語拼音〔揭阳〕 - `gekion`
        - 潮語拼音〔汕头〕 - `suantau`
        - 潮語拼音〔澄海〕 - `tenghai`
        - 潮語拼音〔饒平〕 - `riaupeng`
    - 潮汕话輸入方案
        - 潮語 - `diege_j`
        - 潮語（帶潮語形聲鍵盤） - `diege`
        - 潮語（形聲鍵盤） - `diege_gb`
    - 平話字表 (閩東語‣福州話)
        - 戚林八音 - `ciklinbekin`
        - 福州話字典 - `dfd`
- 客家话
    - 客拼 - `hakka_pinyin`
- 吴语
    - 蘇州吳語 - `soutzoe`
    - 上海吳語 - `wugniu_lopha`
    - 上海新派 - `wugniu`
    - 吳語注音輸入方案吳語學堂版
        - 吳語（桐鄉） - `wugniu_donshian`
        - 吳語（寧波） - `wugniu_gninpou`
        - 吳語（海寧） - `wugniu_haegnin`
        - 吳語（海鹽） - `wugniu_haeye`
        - 吳語（永嘉） - `wugniu_ionko`
        - 吳語（嘉善） - `wugniu_kazoe`
        - 吳語（嘉興） - `wugniu_kashin`
        - 吳語（松江） - `wugniu_sonkaon`
        - 吳語（蘇州） - `wugniu_soutseu`
        - 吳語（上海） - `wugniu_zaonhe`
- 晋语
    - 晋拼解州片 - `haitrou`
- 官话
    - 中原官話洛陽方言
        - 洛陽羅馬字 - `lakyang`
        - 洛陽註音 - `lakyang_chuim`
    - 中原官話輸入方案
        - 中州羅馬字 - `zhung`
        - 中州打字速記法 - `zhung_stenotype`
        - 中州注音法（四十二鍵） - `zhung_42`
        - 中州羅馬字（並擊） - `zhung_combo`
        - 中州注音法（轉寫） - `zhung_transcript`
        - 中州注音法（並擊） - `zhung_combo_transcript`
    - 棗莊話羅馬字輸入方案
        - 嶧州話傳統羅馬字 - `yihdjoouhuah`
        - 嶧州話羅馬字 - `yihjoouhuah_romatzyh`
- 域外方音
    - 옛한글・漢字 - `qyeyshanglr_hanja`
    - 한글・漢字 - `hangyl_hanja`
    - 한글 - `hangyl`
    - poly日文 - `jap_poly`
    - 古壮字拼音 - `sawndip`
    - 輸入法𡨸漢喃 - `hannomPS`

## 部分方案数据来源（非Github submodule）

- 中古汉语
    - [廣韻查詢](https://gist.github.com/lotem/e964a81c1ea457a6ae92)
    - [廣韻羅馬字](https://gist.github.com/lotem/3950485)
    - [廣韻段毄攴字法](https://bintray.com/rime-aca/Schemata/KMG)
- 粤语
    - [貴州韻](https://zhuanlan.zhihu.com/p/31464937)
- 闽语
    - （均来自Github）
- 客家话
    - （均来自Github）
- 吴语
    - (已失效)[吳語注音輸入方案吳語學堂版](http://www.wugniu.com/main/index.php?s=/Home/Article/detail/id/10.html)
- 官话
    - （均来自Github）
- 域外方音
    - [古壮字拼音](https://zhuanlan.zhihu.com/p/24138023)

## 资源

- 输入法软件
    - [Rime官网](http://rime.im/)
    - [Pime输入法](https://github.com/EasyIME/PIME/releases)
    - [iRime输入法](https://itunes.apple.com/us/app/irime%E8%BE%93%E5%85%A5%E6%B3%95-%E4%BA%94%E7%AC%94%E5%B0%8F%E9%B9%A4%E5%8F%8C%E6%8B%BC%E8%BE%93%E5%85%A5%E6%B3%95/id1142623977?mt=8)
    - [同文输入法](https://play.google.com/store/apps/details?id=com.osfans.trime&hl=zh)
- 语言学参考
    - [中国语言资源保护工程 汉语方言用字规范](http://www.moe.gov.cn/s78/A19/A19_gggs/A19_sjhj/201704/W020170405307025943395.pdf)
    - [中国语言资源保护工程采录展示平台](https://zhongguoyuyan.cn/)
    - [复旦大学东亚语言数据中心](http://ccdc.fudan.edu.cn)
    - [家乡话](http://jiaxianghua.org)
    - [乡音苑](http://phonemica.net/)
- 语言学习资源
    - 中古汉语
        - [中古漢語基礎教程](https://bkrs.info/taolun/attachment.php?aid=637)
    - 粤语
        - [貴州韻](https://github.com/tengtengteng/gvaizauvan/wiki)
    - 闽语
        - [平話字表 (閩東語‣福州話)](https://only3km.github.io/ciklinbekin/)
        - [臺灣閩南語羅馬字拼音方案使用手冊](http://www.ntcu.edu.tw/tailo/educate.htm)
        - [潮语拼音教程](https://kahaani.github.io/gatian/index.html)
        - [潮州音字典](http://www.czyzd.com/)
        - [潮州·母语](https://www.mogher.com/)
    - 客家话
        - [薪典](http://syndict.com/)
    - 吴语
        - [吴语学堂](https://wugniu.com/)
        - [吴语协会 通用吴语拼音](http://wu-chinese.com/romanization/)
        - [吴语协会 吴音小字典](http://wu-chinese.com/minidict/)
        - [吳語注音法](http://input.foruto.com/wu/method.html)

## 致谢

- [a-thok](https://github.com/a-thok)
- [biopolyhedron](https://github.com/biopolyhedron)
- [cryptogun](https://github.com/cryptogun)
- [Hector Sioh](https://github.com/only3km)
- [inzoi](https://github.com/inzoi)
- [lois.左](https://github.com/xunux)
- [osfans](https://github.com/osfans)
- [Patrick T.](https://github.com/Patricivs)
- [Tenda Huang](https://github.com/Kahaani)
- [tsauibusato](https://github.com/tsauibusato)
- [佛振](https://github.com/lotem)
- [滕謄](https://github.com/tengtengteng)

# Rime輸入法漢語方言拼音方案全集

## 項目宗旨

本倉庫收集現代漢語各大方言及上古、中古漢語的Rime字庫和拼音輸入方案。本項目的宗旨是爲漢語非普通話使用者提供實用的拼音輸入方案，解決被迫使用普通話輸入法的困難，並爲現代漢語方言、古漢語學習者提供實用便利的學習工具以及爲語言學界學術研究提供參考資料。

本倉庫分爲兩部分：`data/`路徑下爲各個輸入方案的來源倉庫，而submodule的形式保存，方便方案作者實時更新自己的方案。由於部分方案不存在於Github，故此路徑下方案收錄不完整，`download/`路徑下爲已收錄所有方案的下載版，可直接部署使用。我會檢查`data/`下各個方案的更新情況並將最新版本方案覆蓋至`download/`中，確保直接下載的方案爲最新版本。

## 使用教程

若要在自己的Rime輸入法中添加某一輸入方案，只需將該方案的`.dict.yaml`和`.schema.yaml`文件復制到用戶文件夾下，然後在`default.yaml`中添加方案名稱，再重新部署即可。

例如使用Win10系統下的PIME輸入法，要添加上古全拼輸入方案`dkzp`，則只需將`dkzp.dict.yaml`和`dkzp.schema.yaml`兩個文件復制到路徑`C:\Users\用戶名\AppData\Roaming\PIME\Rime`下，然後打開該路徑下的`default.yaml`，在`schema_list:`後加入`- schema: dkzp`，如下：

```yaml
schema_list:
  - schema: XXX
  - schema: YYY
  - schema: dkzp
```

保存後重新部署，再按Ctrl+`即可在菜單中選擇上古全拼方案。

Linux、OS X與其他Windows版本系統下操作同理。

## 已收錄方案

目前**主要缺失閩北語、蒲仙語、平語、湘語、贛語、徽語、西南官話、蘭銀官話、江淮官話、膠遼官話**的輸入方案，如有作者已編寫以上語言的輸入方案，歡迎聯系我添加收錄。其他漢語或域外方音的方案亦強烈歡迎。

- 上古漢語
    - 上古全拼 - `dkzp`
- 中古漢語
    - 中古全拼 - `zyenpheng`
    - 中古三拼 - `triungkoxsampheng`
    - 中古四拼 - `deuqguv4`
    - 廣韻羅馬字 - `kuankhiunn`
    - 爾切羅馬字 - `nieh_ched`
    - 廣韻查詢 - `middle_chinese_lookup`
    - 唐韻 - `Dangrvond`
    - 廣韻段毄攴字法 - `kmg`
- 粵語
    - 粤拼
        - 粵拼 - `jyutping`
        - 耶魯粵語拼音 - `yale`
        - 香港廣東話拼音 - `hkcantonese`
    - 粵拼⁺ - `jyutping+`
    - 粵語注音 - `zyujam`
    - 袖珍粵拼 - `jyutping_compact`
    - 耶鲁粤语拼音 - `yale`
    - 梧州白話 - `NgZjau_JyutPing`
    - 沟漏片藤县白话输入方案 - `jutjnyu_gaulaupin_dangjunbikwaa`
    - 貴州韻 - `gvaizauvan`
- 閩語
    - 泉漳閩南語輸入方案
        - 廈腔閩南語 - `blg_ha`
        - 臺灣閩南語 - `blg_tai`
        - 漳腔閩南語 - `blg_tsiang`
        - 泉腔閩南語 - `blg_tsuan`
    - 閩南語廈台腔專用版 - `blg_etai`
    - 閩倂輸入灋 - `mp`
    - 潮语拼音输入法
        - 潮語拼音〔潮州〕 - `dieziu`
        - 潮語拼音〔潮阳〕 - `dioion`
        - 潮語拼音〔揭阳〕 - `gekion`
        - 潮語拼音〔汕头〕 - `suantau`
        - 潮語拼音〔澄海〕 - `tenghai`
        - 潮語拼音〔饒平〕 - `riaupeng`
    - 潮汕话輸入方案
        - 潮語 - `diege_j`
        - 潮語（帶潮語形聲鍵盤） - `diege`
        - 潮語（形聲鍵盤） - `diege_gb`
    - 平話字表 (閩東語‣福州話)
        - 戚林八音 - `ciklinbekin`
        - 福州話字典 - `dfd`
- 客家話
    - 客拼 - `hakka_pinyin`
- 吳語
    - 蘇州吳語 - `soutzoe`
    - 上海吳語 - `wugniu_lopha`
    - 上海新派 - `wugniu`
    - 吳語注音輸入方案吳語學堂版
        - 吳語（桐鄉） - `wugniu_donshian`
        - 吳語（寧波） - `wugniu_gninpou`
        - 吳語（海寧） - `wugniu_haegnin`
        - 吳語（海鹽） - `wugniu_haeye`
        - 吳語（永嘉） - `wugniu_ionko`
        - 吳語（嘉善） - `wugniu_kazoe`
        - 吳語（嘉興） - `wugniu_kashin`
        - 吳語（松江） - `wugniu_sonkaon`
        - 吳語（蘇州） - `wugniu_soutseu`
        - 吳語（上海） - `wugniu_zaonhe`
- 晉語
    - 晋拼解州片 - `haitrou`
- 官話
    - 中原官話洛陽方言
        - 洛陽羅馬字 - `lakyang`
        - 洛陽註音 - `lakyang_chuim`
    - 中原官話輸入方案
        - 中州羅馬字 - `zhung`
        - 中州打字速記法 - `zhung_stenotype`
        - 中州注音法（四十二鍵） - `zhung_42`
        - 中州羅馬字（並擊） - `zhung_combo`
        - 中州注音法（轉寫） - `zhung_transcript`
        - 中州注音法（並擊） - `zhung_combo_transcript`
    - 棗莊話羅馬字輸入方案
        - 嶧州話傳統羅馬字 - `yihdjoouhuah`
        - 嶧州話羅馬字 - `yihjoouhuah_romatzyh`
- 域外方音
    - 옛한글・漢字 - `qyeyshanglr_hanja`
    - 한글・漢字 - `hangyl_hanja`
    - 한글 - `hangyl`
    - poly日文 - `jap_poly`
    - 古壮字拼音 - `sawndip`
    - 輸入法𡨸漢喃 - `hannomPS`

## 部分方案數據來源（非Github submodule）

- 中古漢語
    - [廣韻查詢](https://gist.github.com/lotem/e964a81c1ea457a6ae92)
    - [廣韻羅馬字](https://gist.github.com/lotem/3950485)
    - [廣韻段毄攴字法](https://bintray.com/rime-aca/Schemata/KMG)
- 粵語
    - [貴州韻](https://zhuanlan.zhihu.com/p/31464937)
- 閩語
    - （均來自Github）
- 客家話
    - （均來自Github）
- 吳語
    - (已失效)[吳語注音輸入方案吳語學堂版](http://www.wugniu.com/main/index.php?s=/Home/Article/detail/id/10.html)
- 官話
    - （均來自Github）
- 域外方音
    - [古壮字拼音](https://zhuanlan.zhihu.com/p/24138023)

## 資源

- 輸入法軟件
    - [Rime官網](http://rime.im/)
    - [Pime輸入法](https://github.com/EasyIME/PIME/releases)
    - [iRime輸入法](https://itunes.apple.com/us/app/irime%E8%BE%93%E5%85%A5%E6%B3%95-%E4%BA%94%E7%AC%94%E5%B0%8F%E9%B9%A4%E5%8F%8C%E6%8B%BC%E8%BE%93%E5%85%A5%E6%B3%95/id1142623977?mt=8)
    - [同文輸入法](https://play.google.com/store/apps/details?id=com.osfans.trime&hl=zh)
- 語言學參考
    - [中国语言资源保护工程 汉语方言用字规范](http://www.moe.gov.cn/s78/A19/A19_gggs/A19_sjhj/201704/W020170405307025943395.pdf)
    - [中国语言资源保护工程采录展示平台](https://zhongguoyuyan.cn/)
    - [复旦大学东亚语言数据中心](http://ccdc.fudan.edu.cn)
    - [家乡话](http://jiaxianghua.org)
    - [鄉音苑](http://phonemica.net/)
- 語言學習資源
    - 中古漢語
        - [中古漢語基礎教程](https://bkrs.info/taolun/attachment.php?aid=637)
    - 粵語
        - [貴州韻](https://github.com/tengtengteng/gvaizauvan/wiki)
    - 閩語
        - [平話字表 (閩東語‣福州話)](https://only3km.github.io/ciklinbekin/)
        - [臺灣閩南語羅馬字拼音方案使用手冊](http://www.ntcu.edu.tw/tailo/educate.htm)
        - [潮语拼音教程](https://kahaani.github.io/gatian/index.html)
        - [潮州音字典](http://www.czyzd.com/)
        - [潮州·母语](https://www.mogher.com/)
    - 客家話
        - [薪典](http://syndict.com/)
    - 吳語
        - [吴语学堂](https://wugniu.com/)
        - [吴语协会 通用吴语拼音](http://wu-chinese.com/romanization/)
        - [吴语协会 吴音小字典](http://wu-chinese.com/minidict/)
        - [吳語注音法](http://input.foruto.com/wu/method.html)
  
## 致謝

- [a-thok](https://github.com/a-thok)
- [biopolyhedron](https://github.com/biopolyhedron)
- [cryptogun](https://github.com/cryptogun)
- [Hector Sioh](https://github.com/only3km)
- [inzoi](https://github.com/inzoi)
- [lois.左](https://github.com/xunux)
- [osfans](https://github.com/osfans)
- [Patrick T.](https://github.com/Patricivs)
- [Tenda Huang](https://github.com/Kahaani)
- [tsauibusato](https://github.com/tsauibusato)
- [佛振](https://github.com/lotem)
- [滕謄](https://github.com/tengtengteng)

# Collection of Rime Input Method Schemas for Chinese Dialects

## The Mission of this Project

This repo collects the Rime phonetic spelling input method schemas and vocabularies for Archaic Chinese, Middle Chinese and modern Chinese dialects. This project is dedicated to providing useful phonetic spelling input methods for all non-Mandarin Chinese dialects, preventing the stale where non-Mandarin Chinese speakers are compelled to use Mandarin input methods. In addition, this project also serves as a useful tool for Chinese dialect learners and a reference for linguistic research.

This repo works as two parts. Folders under the `data/` directory are the sources of some schemas, which are reserved as submodules so that authors of these repos can keep their schemas up to date. Since not all schemas are created on Github, the collection of schemas under this directory is incomplete. The folders under `download/` are off-the-shelf version of the all collected schemas, which you can download, deploy and use directly. I will check the version of schemas under `data/` and copy the newest version to `download/`, to make sure all off-the-shelf schemas are updated.

## Tutorial

To add support for a certain schema to your Rime input method, simply copy the `.dict.yaml` and `.schema.yaml` to the user folder, then append the schema id in `default.yaml` and re-deploy.

For example, if you are using PIME under Windows 10, and would like to add support for the Archaic Chinese schema `dkzp`, simiply copy the two files `dkzp.dict.yaml` and `dkzp.schema.yaml` to `C:\Users\Username\AppData\Roaming\PIME\Rime`, then open `default.yaml` and append `- schema: dkzp` after `schema_list:`, like this:

```yaml
schema_list:
  - schema: XXX
  - schema: YYY
  - schema: dkzp
```

Then save and re-deploy, and press Ctrl+`. You will see the Archaic Chinese schema available in the menu.

Steps are the similar under Linux, OS X and other versions of Windows operating systems.

## Collected Schemas

At the moment this is collection **is missing the schemas for Northern Min, Pu-Xian Min, Pinghua, Xiang, Gan, Huizhou, Lower Yangtze Mandarin, Lan–Yin Mandarin, Southwestern Mandarin**. If you have composed a schema for any of the languages above, please contact me to include it to the collection. Schemas for other Chinese languages are also highly welcomed.

- Archaic Chinese
    - 上古全拼 - `dkzp`
- Middle Chinese
    - 中古全拼 - `zyenpheng`
    - 中古三拼 - `triungkoxsampheng`
    - 中古四拼 - `deuqguv4`
    - 廣韻羅馬字 - `kuankhiunn`
    - 爾切羅馬字 - `nieh_ched`
    - 廣韻查詢 - `middle_chinese_lookup`
    - 唐韻 - `Dangrvond`
    - 廣韻段毄攴字法 - `kmg`
- Yue (Cantonese)
    - 粤拼
        - 粵拼 - `jyutping`
        - 耶魯粵語拼音 - `yale`
        - 香港廣東話拼音 - `hkcantonese`
    - 粵拼⁺ - `jyutping+`
    - 粵語注音 - `zyujam`
    - 袖珍粵拼 - `jyutping_compact`
    - 耶鲁粤语拼音 - `yale`
    - 梧州白話 - `NgZjau_JyutPing`
    - 沟漏片藤县白话输入方案 - `jutjnyu_gaulaupin_dangjunbikwaa`
    - 貴州韻 - `gvaizauvan`
- Min (Hokkien)
    - 泉漳閩南語輸入方案
        - 廈腔閩南語 - `blg_ha`
        - 臺灣閩南語 - `blg_tai`
        - 漳腔閩南語 - `blg_tsiang`
        - 泉腔閩南語 - `blg_tsuan`
    - 閩南語廈台腔專用版 - `blg_etai`
    - 閩倂輸入灋 - `mp`
    - 潮语拼音输入法
        - 潮語拼音〔潮州〕 - `dieziu`
        - 潮語拼音〔潮阳〕 - `dioion`
        - 潮語拼音〔揭阳〕 - `gekion`
        - 潮語拼音〔汕头〕 - `suantau`
        - 潮語拼音〔澄海〕 - `tenghai`
        - 潮語拼音〔饒平〕 - `riaupeng`
    - 潮汕话輸入方案
        - 潮語 - `diege_j`
        - 潮語（帶潮語形聲鍵盤） - `diege`
        - 潮語（形聲鍵盤） - `diege_gb`
    - 平話字表 (閩東語‣福州話)
        - 戚林八音 - `ciklinbekin`
        - 福州話字典 - `dfd`
- Hakka
    - 客拼 - `hakka_pinyin`
- Wu
    - 蘇州吳語 - `soutzoe`
    - 上海吳語 - `wugniu_lopha`
    - 上海新派 - `wugniu`
    - 吳語注音輸入方案吳語學堂版
        - 吳語（桐鄉） - `wugniu_donshian`
        - 吳語（寧波） - `wugniu_gninpou`
        - 吳語（海寧） - `wugniu_haegnin`
        - 吳語（海鹽） - `wugniu_haeye`
        - 吳語（永嘉） - `wugniu_ionko`
        - 吳語（嘉善） - `wugniu_kazoe`
        - 吳語（嘉興） - `wugniu_kashin`
        - 吳語（松江） - `wugniu_sonkaon`
        - 吳語（蘇州） - `wugniu_soutseu`
        - 吳語（上海） - `wugniu_zaonhe`
- Jin
    - 晋拼解州片 - `haitrou`
- Mandarin
    - 中原官話洛陽方言
        - 洛陽羅馬字 - `lakyang`
        - 洛陽註音 - `lakyang_chuim`
    - 中原官話輸入方案
        - 中州羅馬字 - `zhung`
        - 中州打字速記法 - `zhung_stenotype`
        - 中州注音法（四十二鍵） - `zhung_42`
        - 中州羅馬字（並擊） - `zhung_combo`
        - 中州注音法（轉寫） - `zhung_transcript`
        - 中州注音法（並擊） - `zhung_combo_transcript`
    - 棗莊話羅馬字輸入方案
        - 嶧州話傳統羅馬字 - `yihdjoouhuah`
        - 嶧州話羅馬字 - `yihjoouhuah_romatzyh`
- Foreign Dialects
    - 옛한글・漢字 - `qyeyshanglr_hanja`
    - 한글・漢字 - `hangyl_hanja`
    - 한글 - `hangyl`
    - poly日文 - `jap_poly`
    - 古壮字拼音 - `sawndip`
    - 輸入法𡨸漢喃 - `hannomPS`

## Incomplete List of Data Sources (non-Github submodules)

- Middle Chinese
    - [廣韻查詢](https://gist.github.com/lotem/e964a81c1ea457a6ae92)
    - [廣韻羅馬字](https://gist.github.com/lotem/3950485)
    - [廣韻段毄攴字法](https://bintray.com/rime-aca/Schemata/KMG)
- Yue (Cantonese)
    - [貴州韻](https://zhuanlan.zhihu.com/p/31464937)
- Min (Hokkien)
    - (All from Github)
- Hakka
    - (All from Github)
- Wu
    - (Obsolete)[吳語注音輸入方案吳語學堂版](http://www.wugniu.com/main/index.php?s=/Home/Article/detail/id/10.html)
- Mandarin
    - (All from Github)
- Foreign Dialects
    - [古壮字拼音](https://zhuanlan.zhihu.com/p/24138023)

## Resources

- Input Method Software
    - [Rime Official Website](http://rime.im/)
    - [Pime Input Method](https://github.com/EasyIME/PIME/releases)
    - [iRime Input Method](https://itunes.apple.com/us/app/irime%E8%BE%93%E5%85%A5%E6%B3%95-%E4%BA%94%E7%AC%94%E5%B0%8F%E9%B9%A4%E5%8F%8C%E6%8B%BC%E8%BE%93%E5%85%A5%E6%B3%95/id1142623977?mt=8)
    - [Trime Input Method](https://play.google.com/store/apps/details?id=com.osfans.trime&hl=zh)
- Linguistics References
    - [中国语言资源保护工程 汉语方言用字规范](http://www.moe.gov.cn/s78/A19/A19_gggs/A19_sjhj/201704/W020170405307025943395.pdf)
    - [中国语言资源保护工程采录展示平台](https://zhongguoyuyan.cn/)
    - [复旦大学东亚语言数据中心](http://ccdc.fudan.edu.cn)
    - [家乡话](http://jiaxianghua.org)
    - [Phonemica](http://phonemica.net/)
- Language Learning Resources
    - Middle Chinese
        - [中古漢語基礎教程](https://bkrs.info/taolun/attachment.php?aid=637)
    - Yue (Cantonese)
        - [貴州韻](https://github.com/tengtengteng/gvaizauvan/wiki)
    - Min (Hokkien)
        - [平話字表 (閩東語‣福州話)](https://only3km.github.io/ciklinbekin/)
        - [臺灣閩南語羅馬字拼音方案使用手冊](http://www.ntcu.edu.tw/tailo/educate.htm)
        - [潮语拼音教程](https://kahaani.github.io/gatian/index.html)
        - [潮州音字典](http://www.czyzd.com/)
        - [潮州·母语](https://www.mogher.com/)
    - Hakka
        - [薪典](http://syndict.com/)
    - Wu
        - [吴语学堂](https://wugniu.com/)
        - [吴语协会 通用吴语拼音](http://wu-chinese.com/romanization/)
        - [吴语协会 吴音小字典](http://wu-chinese.com/minidict/)
        - [吳語注音法](http://input.foruto.com/wu/method.html)
  
## Acknowledgements

- [a-thok](https://github.com/a-thok)
- [biopolyhedron](https://github.com/biopolyhedron)
- [cryptogun](https://github.com/cryptogun)
- [Hector Sioh](https://github.com/only3km)
- [inzoi](https://github.com/inzoi)
- [lois.左](https://github.com/xunux)
- [osfans](https://github.com/osfans)
- [Patrick T.](https://github.com/Patricivs)
- [Tenda Huang](https://github.com/Kahaani)
- [tsauibusato](https://github.com/tsauibusato)
- [佛振](https://github.com/lotem)
- [滕謄](https://github.com/tengtengteng)
