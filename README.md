# 中州韻輸入法漢語方言拼音方案全集

**[中文](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#%E4%B8%AD%E5%B7%9E%E9%9F%BB%E8%BC%B8%E5%85%A5%E6%B3%95%E6%BC%A2%E8%AA%9E%E6%96%B9%E8%A8%80%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88%E5%85%A8%E9%9B%86)        [English](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#collection-of-rime-input-method-schemas-for-chinese-topolectsdialects)**

## 項目宗旨

本倉庫收集現代漢語各大方言及上古、中古漢語的[中州韻輸入法](https://rime.im/)拼音輸入方案和字庫。本項目的目標有三：

1. 爲漢語非普通話使用者提供實用的拼音輸入方案，解決被迫使用普通話輸入法的困難。
2. 爲現代漢語方言、古漢語學習者提供實用便利的學習工具，通過拼音打字來練習正音和正字。
3. 爲學術研究（語言學、漢學、人類學等）提供參考資料。

本項目同作爲推廣漢語方言拼音輸入的支持項目，關於推廣漢語方言拼音的理念和宗旨詳情請閱讀[本文](https://laubonghaudoi.github.io/dialects/blog/mission.html)。

本倉庫分爲三部分：
1. `sources/`路徑下爲各個輸入方案的來源倉庫，以submodule的形式保存，方便方案作者實時更新自己的方案。由於部分方案不存在於GitHub，故此路徑下方案收錄不完整，
2. `data/`路徑下爲已收錄所有方案文件，我會檢查`sources/`下各個方案的更新情況並將最新版本方案覆蓋至`data/`中。
3. `download/`路徑用於存放各個語言的唯一權威版拼音，即爲[發佈頁面](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases)的下載整合包，方便用戶直接部署使用。

## 使用教程（项目网站）

### [**漢語方言拼音輸入**](https://laubonghaudoi.github.io/dialects/)

## 已收錄方案

目前總共收錄46門語言/方言的80個方案（上古漢語和中古漢語各算一門語言）。**主要缺失閩北語、閩中語、邵將語、瓊雷話、平話、湘語、贛語、徽語、蘭銀官話、膠遼官話**的輸入方案，如有作者已編寫以上語言的輸入方案，請[聯系我](mailto:laubonghaudoi@qq.com)或新開一個issue以添加收錄。其他漢語或域外方音的方案亦強烈歡迎。

- 上古漢語
    - 上古全拼 - ℞ `dkzp`
- 中古漢語
    - 中古全拼 - ℞ `zyenpheng`
    - 中古三拼 - ℞ `triungkoxsampheng`
    - 中古四拼 - ℞ `deuqguv4`
    - 中古汉拼 - ℞ `dghp`
    - 廣韻羅馬字 - ℞ `kuankhiunn`
    - 爾切羅馬字 - ℞ `nieh_ched`
    - 廣韻查詢 - ℞ `middle_chinese_lookup`
    - 唐韻 - ℞ `Dangrvond`
    - 廣韻段毄攴字法 - ℞ `kmg`
- 粵語
    - 粤拼
        - 粵拼 - ℞ `jyutping`
        - 耶魯粵語拼音 - ℞ `yale`
        - 香港廣東話拼音 - ℞ `hkcantonese`
    - 粵拼⁺ - ℞ `jyutping+`
    - 粵語注音 - ℞ `zyujam`
    - 袖珍粵拼 - ℞ `jyutping_compact`
    - 耶鲁粤语拼音 - ℞ `yale`
    - 梧州白話 - ℞ `NgZjau_JyutPing`
    - 南寧白話輸入方案
        - 南寧白話 - ℞ `naamning_jyutping`
        - 南寧白話(IPA) - ℞ `naamning_jyutping_IPA`
    - 沟漏片藤县白话输入方案 - ℞ `jutjnyu_gaulaupin_dangjunbikwaa`
    - 貴州韻 - ℞ `gvaizauvan`
- 閩東語
    - 平話字表 (閩東語‣福州話)
        - 戚林八音 - ℞ `ciklinbekin`
        - 福州話字典 - ℞ `dfd`
- 莆仙語（興化語）
    - 興化語莆田城關話 - ℞ `Pouleng`
    - 興化語平話字 - ℞ `HinghuaBUC`
- 閩南語
    - 泉漳閩南語輸入方案
        - 廈腔閩南語 - ℞ `blg_ha`
        - 臺灣閩南語 - ℞ `blg_tai`
        - 漳腔閩南語 - ℞ `blg_tsiang`
        - 泉腔閩南語 - ℞ `blg_tsuan`
    - 閩南語廈台腔專用版 - ℞ `blg_etai`
    - 閩倂輸入灋 - ℞ `mp`
    - 潮语拼音输入法
        - 潮語拼音〔潮州〕 - ℞ `dieziu`
        - 潮語拼音〔潮阳〕 - ℞ `dioion`
        - 潮語拼音〔揭阳〕 - ℞ `gekion`
        - 潮語拼音〔汕头〕 - ℞ `suantau`
        - 潮語拼音〔澄海〕 - ℞ `tenghai`
        - 潮語拼音〔饒平〕 - ℞ `riaupeng`
    - 潮汕话輸入方案
        - 潮語 - ℞ `diege_j`
        - 潮語（帶潮語形聲鍵盤） - ℞ `diege`
        - 潮語（形聲鍵盤） - ℞ `diege_gb`
- 客家話
    - 客拼 - ℞ `hakka_pinyin`
- 吳語
    - 蘇州吳語 - ℞ `soutzoe`
    - 上海吳語輸入方案 
        - 上海吳語 - ℞ `wugniu_lopha`
        - 上海新派 - ℞ `wugniu`
    - 吳語注音輸入方案吳語學堂版
        - 吳語（桐鄉） - ℞ `wugniu_donshian`
        - 吳語（寧波） - ℞ `wugniu_gninpou`
        - 吳語（海寧） - ℞ `wugniu_haegnin`
        - 吳語（海鹽） - ℞ `wugniu_haeye`
        - 吳語（永嘉） - ℞ `wugniu_ionko`
        - 吳語（嘉善） - ℞ `wugniu_kazoe`
        - 吳語（嘉興） - ℞ `wugniu_kashin`
        - 吳語（松江） - ℞ `wugniu_sonkaon`
        - 吳語（蘇州） - ℞ `wugniu_soutseu`
        - 吳語（上海） - ℞ `wugniu_zaonhe`
    - 標準吳語 - ℞ `pcngng`
- 晉語
    - 晋拼解州片 - ℞ `haitrou`
- 官話
    - 中原官話洛陽方言
        - 洛陽羅馬字 - ℞ `lakyang`
        - 洛陽註音 - ℞ `lakyang_chuim`
    - 中原官話輸入方案
        - 中州羅馬字 - ℞ `zhung`
        - 中州打字速記法 - ℞ `zhung_stenotype`
        - 中州注音法（四十二鍵） - ℞ `zhung_42`
        - 中州羅馬字（並擊） - ℞ `zhung_combo`
        - 中州注音法（轉寫） - ℞ `zhung_transcript`
        - 中州注音法（並擊） - ℞ `zhung_combo_transcript`
    - 棗莊話羅馬字輸入方案
        - 嶧州話傳統羅馬字 - ℞ `yihdjoouhuah`
        - 嶧州話羅馬字 - ℞ `yihjoouhuah_romatzyh`
    - 南京官話拼音 - ℞ `langjin`
    - 蜀拼
        - 蜀拼通音 - ℞ `shupin_tongyin`
        - 蜀拼-成都 - ℞ `shupin_cendu`
        - 蜀拼-重慶 - ℞ `shupin_congqin`
        - 蜀拼-貴陽 - ℞ `shupin_guiyang`
        - 蜀拼-宜賓 - ℞ `shupin_libin`
        - 蜀拼-自貢 - ℞ `shupin_zigong`
- 域外方音
    - 옛한글・漢字 - ℞ `qyeyshanglr_hanja`
    - 한글・漢字 - ℞ `hangyl_hanja`
    - 한글 - ℞ `hangyl`
    - poly日文 - ℞ `jap_poly`
    - 古壮字拼音 - ℞ `sawndip`
    - 輸入法𡨸漢喃 - ℞ `hannomPS`

下載包內方案信息詳見[發佈](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases)頁面。

## 部分方案數據來源（非GitHub submodule）

- 中古漢語
    - [廣韻查詢](https://gist.github.com/lotem/e964a81c1ea457a6ae92)
    - [廣韻羅馬字](https://gist.github.com/lotem/3950485)
    - [廣韻段毄攴字法](https://bintray.com/rime-aca/Schemata/KMG)
- 粵語
    - [貴州韻](https://zhuanlan.zhihu.com/p/31464937)
- 閩語
    - （均來自GitHub）
- 客家話
    - （均來自GitHub）
- 吳語
    - （均來自GitHub）
- 官話
    - （均來自GitHub）
- 域外方音
    - [古壮字拼音](https://zhuanlan.zhihu.com/p/24138023)

## 資源

- 語言學習資源（方案白皮書、教程、字典）
    - 中古漢語
        - [中古漢語拼音](https://zh.wikipedia.org/wiki/User:Polyhedron/%E4%B8%AD%E5%8F%A4%E6%BC%A2%E8%AA%9E%E6%8B%BC%E9%9F%B3)
        - [中古漢語基礎教程](https://bkrs.info/taolun/attachment.php?aid=637)
        - [古音手鏡](http://www.guguolin.com/)
    - 官話
        - [南京話拼音教程](https://uliloewi.github.io/LangJinPinIn/SUMMARY)
    - 吳語
        - [吴语学堂](https://wugniu.com/)
        - [吴语协会 通用吴语拼音](http://wu-chinese.com/romanization/)
        - [吴语协会 吴音小字典](http://wu-chinese.com/minidict/)
        - [吳語注音法](http://input.foruto.com/wu/method.html)
        - [宁波话吴拼教程](https://shinzoqchiuq.github.io/gninpou-tutorial/)
    - 粵語
        - [南宁白话](https://leimaau.github.io/book/)
        - [貴州韻](https://github.com/tengtengteng/gvaizauvan/wiki)
    - 閩語
        - [平話字表 (閩東語‣福州話)](https://only3km.github.io/ciklinbekin/)
        - [臺語萌典](https://www.moedict.tw/'%E7%99%BC%E7%A9%8E)
        - [臺灣閩南語羅馬字拼音方案使用手冊](http://www.ntcu.edu.tw/tailo/educate.htm)
        - [潮语拼音教程](https://kahaani.github.io/gatian/index.html)
        - [潮州音字典](http://www.czyzd.com/)
        - [潮州·母语](https://www.mogher.com/)
    - 客家話
        - [薪典](http://syndict.com/)
        - [客語萌典](https://www.moedict.tw/:%E7%99%BC%E8%8A%BD)
- 語言學參考
    - [中国语言资源保护工程 汉语方言用字规范](http://www.moe.gov.cn/s78/A19/A19_gggs/A19_sjhj/201704/W020170405307025943395.pdf)
    - [中国语言资源保护工程采录展示平台](https://zhongguoyuyan.cn/)
    - [复旦大学东亚语言数据中心](http://ccdc.fudan.edu.cn)
    - [家乡话](http://jiaxianghua.org)
    - [鄉音苑](http://phonemica.net/)
    - [韻典網](https://ytenx.org/)
    - [古今文字集成](http://www.ccamc.co/index.php)
    - [篇韻データベース](http://suzukish.s252.xrea.com/search/)
- 輸入法軟件
    - [Rime官網](http://rime.im/)
    - [Pime輸入法](https://github.com/EasyIME/PIME/releases)
    - [iRime輸入法](https://itunes.apple.com/us/app/irime%E8%BE%93%E5%85%A5%E6%B3%95-%E4%BA%94%E7%AC%94%E5%B0%8F%E9%B9%A4%E5%8F%8C%E6%8B%BC%E8%BE%93%E5%85%A5%E6%B3%95/id1142623977?mt=8)
    - [同文輸入法](https://play.google.com/store/apps/details?id=com.osfans.trime&hl=zh)

## 致謝（按筆畫-字母順序排列）

- [佛振](https://github.com/lotem)
- [芽油](https://github.com/Yaryou)
- [滕謄](https://github.com/tengtengteng)
- [a-thok](https://github.com/a-thok)
- [biopolyhedron](https://github.com/biopolyhedron)
- [cryptogun](https://github.com/cryptogun)
- [Electric Sheep](https://github.com/shinzoqchiuq)
- [Hector Sioh](https://github.com/only3km)
- [inzoi](https://github.com/inzoi)
- [LeiMaau](https://github.com/leimaau)
- [lois.左](https://github.com/xunux)
- [osfans](https://github.com/osfans)
- [Papnas](https://github.com/Papnas)
- [Patrick T.](https://github.com/Patricivs)
- [Tenda Huang](https://github.com/Kahaani)
- [tsauibusato](https://github.com/tsauibusato)
- [uliloewi](https://github.com/uliloewi)

# Collection of Rime Input Method Schemas for Chinese Topolects/Dialects

**[中文](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#%E4%B8%AD%E5%B7%9E%E9%9F%BB%E8%BC%B8%E5%85%A5%E6%B3%95%E6%BC%A2%E8%AA%9E%E6%96%B9%E8%A8%80%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88%E5%85%A8%E9%9B%86)        [English](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#collection-of-rime-input-method-schemas-for-chinese-topolectsdialects)**

## The Mission of this Project

This repo collects the phonetic spelling schemas and character sets of [Rime input method](https://rime.im/) for Old Chinese, Middle Chinese and modern Chinese topolects/dialects. This project aims to:

1. Provide useful phonetic spelling input schemas for all non-Mandarin Chinese topolects/dialects, preventing the predicament where non-Mandarin Chinese speakers are compelled to type in Mandarin. 
2. Serve as a useful tool for Chinese topolect/dialect learners, as one can use phonetic spelling input to practice the standard pronunciation and orthography.
3. Provide references for academic researches (Linguistics, Sinology, Anthropology, etc.).  

This project also supports the promotion project of non-Mandarin phonetic spelling input. For a complete statement of the mission and motivation of the promotion, please read [this page](https://laubonghaudoi.github.io/dialects/blog/mission.html) (Chinese only).

This repo works as three parts:

1. Folders under the `sources/` directory are the source repos of some schemas, which are preserved as submodules so that the schema designers can keep their schemas up to date. Since not all schemas are open-sourced on GitHub, the collection under this directory is incomplete. 
2. The `data/` directory is a complete collection, which contains schemas that I collected from all sources (including those on GitHub). I will check the version of schemas under `sources/` regularly and copy the newest version to `data/`. 
3. The `download/` directory serves as the folder for the [released](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases) packages. It contains only the selected schema for the prestige dialect of each language. Hence users can download, deploy and use these off-the-shelf schemas conveniently.

## Tutorial

### Detailed Introduction (Project Website)

For detailed steps and explanations, check out this website (Chinese only):

### [**漢語方言拼音輸入**](https://laubonghaudoi.github.io/dialects/)

### Short Introduction

To deploy a certain schema to your Rime input method, simply copy the `.dict.yaml` and `.schema.yaml` to the user folder, then append the schema id in `default.yaml` and re-deploy.

For example, if you are using PIME under Windows 10, and would like to add support for the Old Chinese schema `dkzp`, simply copy the two files `dkzp.dict.yaml` and `dkzp.schema.yaml` to `C:\Users\Username\AppData\Roaming\PIME\Rime`, then open `default.yaml` and append `- schema: dkzp` after `schema_list:`, like this:

```yaml
schema_list:
  - schema: XXX
  - schema: YYY
  - schema: dkzp
```

Then save and re-deploy, and press Ctrl+`. You will see the Archaic Chinese schema available in the menu.

Steps are the similar under Linux, OS X and other versions of Windows operating systems.

## Collected Schemas

At the moment there are 80 schemas for 46 languages/dialects collected (old Chinese and middle Chinese are counted as one language respectively), and still **missing the schemas for Northern Min, Central Min, Shao-Jiang Min, Qiongleihua, Pinghua, Xiang, Gan, Huizhou, Lan–Yin Mandarin, Southwestern Mandarin**. If you have composed a schema for any of the languages above, please [contact me](mailto:laubonghaudoi@qq.com) or open a new issue to include it to the collection. Schemas for other Chinese languages are also highly welcomed.

- Old Chinese
    - 上古全拼 - ℞ `dkzp`
- Middle Chinese
    - 中古全拼 - ℞ `zyenpheng`
    - 中古三拼 - ℞ `triungkoxsampheng`
    - 中古四拼 - ℞ `deuqguv4`
    - 中古汉拼 - ℞ `dghp`
    - 廣韻羅馬字 - ℞ `kuankhiunn`
    - 爾切羅馬字 - ℞ `nieh_ched`
    - 廣韻查詢 - ℞ `middle_chinese_lookup`
    - 唐韻 - ℞ `Dangrvond`
    - 廣韻段毄攴字法 - ℞ `kmg`
- Yue (Cantonese)
    - 粤拼
        - 粵拼 - ℞ `jyutping`
        - 耶魯粵語拼音 - ℞ `yale`
        - 香港廣東話拼音 - ℞ `hkcantonese`
    - 粵拼⁺ - ℞ `jyutping+`
    - 粵語注音 - ℞ `zyujam`
    - 袖珍粵拼 - ℞ `jyutping_compact`
    - 耶鲁粤语拼音 - ℞ `yale`
    - 梧州白話 - ℞ `NgZjau_JyutPing`
    - 南寧白話輸入方案
        - 南寧白話 - ℞ `naamning_jyutping`
        - 南寧白話(IPA) - ℞ `naamning_jyutping_IPA`
    - 沟漏片藤县白话输入方案 - ℞ `jutjnyu_gaulaupin_dangjunbikwaa`
    - 貴州韻 - ℞ `gvaizauvan`
- Eastern Min
    - 平話字表 (閩東語‣福州話)
        - 戚林八音 - ℞ `ciklinbekin`
        - 福州話字典 - ℞ `dfd`
- Puxian Min
    - 興化語莆田城關話 - ℞ `Pouleng`
    - 興化語平話字 - ℞ `HinghuaBUC`
- Southern Min (Hokkien)
    - 泉漳閩南語輸入方案
        - 廈腔閩南語 - ℞ `blg_ha`
        - 臺灣閩南語 - ℞ `blg_tai`
        - 漳腔閩南語 - ℞ `blg_tsiang`
        - 泉腔閩南語 - ℞ `blg_tsuan`
    - 閩南語廈台腔專用版 - ℞ `blg_etai`
    - 閩倂輸入灋 - ℞ `mp`
    - 潮语拼音输入法
        - 潮語拼音〔潮州〕 - ℞ `dieziu`
        - 潮語拼音〔潮阳〕 - ℞ `dioion`
        - 潮語拼音〔揭阳〕 - ℞ `gekion`
        - 潮語拼音〔汕头〕 - ℞ `suantau`
        - 潮語拼音〔澄海〕 - ℞ `tenghai`
        - 潮語拼音〔饒平〕 - ℞ `riaupeng`
    - 潮汕话輸入方案
        - 潮語 - ℞ `diege_j`
        - 潮語（帶潮語形聲鍵盤） - ℞ `diege`
        - 潮語（形聲鍵盤） - ℞ `diege_gb`
- Hakka
    - 客拼 - ℞ `hakka_pinyin`
- Wu (Goetian)
    - 蘇州吳語 - ℞`soutzoe`
    - 上海吳語輸入方案 
        - 上海吳語 - ℞ `wugniu_lopha`
        - 上海新派 - ℞ `wugniu`
    - 吳語注音輸入方案吳語學堂版
        - 吳語（桐鄉） - ℞ `wugniu_donshian`
        - 吳語（寧波） - ℞ `wugniu_gninpou`
        - 吳語（海寧） - ℞ `wugniu_haegnin`
        - 吳語（海鹽） - ℞ `wugniu_haeye`
        - 吳語（永嘉） - ℞ `wugniu_ionko`
        - 吳語（嘉善） - ℞ `wugniu_kazoe`
        - 吳語（嘉興） - ℞ `wugniu_kashin`
        - 吳語（松江） - ℞ `wugniu_sonkaon`
        - 吳語（蘇州） - ℞ `wugniu_soutseu`
        - 吳語（上海） - ℞ `wugniu_zaonhe`
    - 標準吳語 - ℞ `pcngng`
- Jin
    - 晋拼解州片 - ℞ `haitrou`
- Mandarin
    - 中原官話洛陽方言
        - 洛陽羅馬字 - ℞ `lakyang`
        - 洛陽註音 - ℞ `lakyang_chuim`
    - 中原官話輸入方案
        - 中州羅馬字 - ℞ `zhung`
        - 中州打字速記法 - ℞ `zhung_stenotype`
        - 中州注音法（四十二鍵） - ℞ `zhung_42`
        - 中州羅馬字（並擊） - ℞ `zhung_combo`
        - 中州注音法（轉寫） - ℞ `zhung_transcript`
        - 中州注音法（並擊） - ℞ `zhung_combo_transcript`
    - 棗莊話羅馬字輸入方案
        - 嶧州話傳統羅馬字 - ℞ `yihdjoouhuah`
        - 嶧州話羅馬字 - ℞ `yihjoouhuah_romatzyh`
    - 南京官話拼音 - ℞ `langjin`
    - 蜀拼
        - 蜀拼通音 - ℞ `shupin_tongyin`
        - 蜀拼-成都 - ℞ `shupin_cendu`
        - 蜀拼-重慶 - ℞ `shupin_congqin`
        - 蜀拼-貴陽 - ℞ `shupin_guiyang`
        - 蜀拼-宜賓 - ℞ `shupin_libin`
        - 蜀拼-自貢 - ℞ `shupin_zigong`
- Foreign Dialects
    - 옛한글・漢字 - ℞ `qyeyshanglr_hanja`
    - 한글・漢字 - ℞ `hangyl_hanja`
    - 한글 - ℞ `hangyl`
    - poly日文 - ℞ `jap_poly`
    - 古壮字拼音 - ℞ `sawndip`
    - 輸入法𡨸漢喃 - ℞ `hannomPS`

For detailed information of the collected schemas in the download packege, please see the [release](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases) page.

## Incomplete List of Data Sources (non-GitHub submodules)

- Middle Chinese
    - [廣韻查詢](https://gist.github.com/lotem/e964a81c1ea457a6ae92)
    - [廣韻羅馬字](https://gist.github.com/lotem/3950485)
    - [廣韻段毄攴字法](https://bintray.com/rime-aca/Schemata/KMG)
- Yue (Cantonese)
    - [貴州韻](https://zhuanlan.zhihu.com/p/31464937)
- Min (Hokkien)
    - (All from GitHub)
- Hakka
    - (All from GitHub)
- Wu (Goetian)
    - (All from GitHub)
- Mandarin
    - (All from GitHub)
- Foreign Dialects
    - [古壮字拼音](https://zhuanlan.zhihu.com/p/24138023)

## Resources

- Language learning resources (schema white papers, tutorials, dictionaries, etc.)
    - Middle Chinese
        - [中古漢語拼音](https://zh.wikipedia.org/wiki/User:Polyhedron/%E4%B8%AD%E5%8F%A4%E6%BC%A2%E8%AA%9E%E6%8B%BC%E9%9F%B3)
        - [中古漢語基礎教程](https://bkrs.info/taolun/attachment.php?aid=637)
        - [古音手鏡](http://www.guguolin.com/)
    - Yue (Cantonese)
        - [南宁白话](https://leimaau.github.io/book/)
        - [貴州韻](https://github.com/tengtengteng/gvaizauvan/wiki)
    - Min (Hokkien)
        - [平話字表 (閩東語‣福州話)](https://only3km.github.io/ciklinbekin/)
        - [臺語萌典](https://www.moedict.tw/'%E7%99%BC%E7%A9%8E)
        - [臺灣閩南語羅馬字拼音方案使用手冊](http://www.ntcu.edu.tw/tailo/educate.htm)
        - [潮语拼音教程](https://kahaani.github.io/gatian/index.html)
        - [潮州音字典](http://www.czyzd.com/)
        - [潮州·母语](https://www.mogher.com/)
    - Hakka
        - [薪典](http://syndict.com/)
        - [客語萌典](https://www.moedict.tw/:%E7%99%BC%E8%8A%BD)
    - Wu (Goetian)
        - [吴语学堂](https://wugniu.com/)
        - [吴语协会 通用吴语拼音](http://wu-chinese.com/romanization/)
        - [吴语协会 吴音小字典](http://wu-chinese.com/minidict/)
        - [吳語注音法](http://input.foruto.com/wu/method.html)
        - [宁波话吴拼教程](https://shinzoqchiuq.github.io/gninpou-tutorial/)
    - Mandarin
        - [南京話拼音教程](https://uliloewi.github.io/LangJinPinIn/SUMMARY)
- Linguistics references
    - [中国语言资源保护工程 汉语方言用字规范](http://www.moe.gov.cn/s78/A19/A19_gggs/A19_sjhj/201704/W020170405307025943395.pdf)
    - [中国语言资源保护工程采录展示平台](https://zhongguoyuyan.cn/)
    - [复旦大学东亚语言数据中心](http://ccdc.fudan.edu.cn)
    - [家乡话](http://jiaxianghua.org)
    - [Phonemica](http://phonemica.net/)
    - [韻典網](https://ytenx.org/)
    - [古今文字集成](http://www.ccamc.co/index.php)
    - [篇韻データベース](http://suzukish.s252.xrea.com/search/)
- Input method software
    - [Rime Official Website](http://rime.im/)
    - [Pime Input Method](https://github.com/EasyIME/PIME/releases)
    - [iRime Input Method](https://itunes.apple.com/us/app/irime%E8%BE%93%E5%85%A5%E6%B3%95-%E4%BA%94%E7%AC%94%E5%B0%8F%E9%B9%A4%E5%8F%8C%E6%8B%BC%E8%BE%93%E5%85%A5%E6%B3%95/id1142623977?mt=8)
    - [Trime Input Method](https://play.google.com/store/apps/details?id=com.osfans.trime&hl=zh)


## Acknowledgements (In strokes and alphabetical order)

- [佛振](https://github.com/lotem)
- [芽油](https://github.com/Yaryou)
- [滕謄](https://github.com/tengtengteng)
- [a-thok](https://github.com/a-thok)
- [biopolyhedron](https://github.com/biopolyhedron)
- [cryptogun](https://github.com/cryptogun)
- [Electric Sheep](https://github.com/shinzoqchiuq)
- [Hector Sioh](https://github.com/only3km)
- [inzoi](https://github.com/inzoi)
- [LeiMaau](https://github.com/leimaau)
- [lois.左](https://github.com/xunux)
- [osfans](https://github.com/osfans)
- [Papnas](https://github.com/Papnas)
- [Patrick T.](https://github.com/Patricivs)
- [Tenda Huang](https://github.com/Kahaani)
- [tsauibusato](https://github.com/tsauibusato)
- [uliloewi](https://github.com/uliloewi)
