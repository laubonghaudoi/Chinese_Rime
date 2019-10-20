<h1>中州韻輸入法漢語方言拼音方案全集
<br/>Collection of Rime Input Method Phonetic Spelling Schemas for Chinese Languages & Dialects</h1>

![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
![licence](https://img.shields.io/badge/licence-Apache--2.0-blue.svg?style=flat)

<h2>項目宗旨
<br/>The mission of this project</h2>

本倉庫收集現代漢語各大方言及上古、中古漢語的 [中州韻輸入法](https://rime.im/) 拼音輸入方案和字庫。本項目的目標有三：

1. 爲漢語非普通話使用者提供實用的拼音輸入方案，解決被迫使用普通話輸入法的困難。
2. 爲現代漢語方言、古漢語學習者提供實用便利的學習工具，通過拼音打字來練習正音和正字。
3. 爲學術研究（語言學、漢學、人類學等）提供參考資料。

本項目同作爲推廣漢語方言拼音輸入的支持項目，關於推廣漢語方言拼音的理念和宗旨詳情請閱讀 [本文](https://laubonghaudoi.github.io/hanhngiox/blog/mission.html)。

This repository collects the phonetic spelling schemas and character sets of [Rime input method](https://rime.im/) for Old Chinese, Middle Chinese and modern Chinese languages & dialects. This project aims to:

1. Provide useful phonetic spelling input schemas for all non-Mandarin Chinese languages & dialects, solving the predicament where non-Mandarin Chinese speakers are compelled to type in Mandarin.
2. Serve as a useful tool for Chinese language & dialect learners, as one can use phonetic spelling input to practice the standard pronunciation and orthography.
3. Provide references for academic researches (Linguistics, Sinology, Anthropology, etc.).

This project also supports the promotion project of non-Mandarin phonetic spelling input. For a complete statement of the mission and motivation of the promotion, please read [this page](https://laubonghaudoi.github.io/hanhngiox/blog/mission.html) (Chinese only).

本倉庫分为四个子文件夹：

1. `sources/` 路徑下爲各個輸入方案的來源倉庫，以子模塊 submodule 的形式保存。其中大部分爲配方（配方的介紹請參見 [Rime 輸入方案又是啥](https://github.com/rime/home/wiki/RimeWithSchemata#rime-%E8%BC%B8%E5%85%A5%E6%96%B9%E6%A1%88%E5%8F%88%E6%98%AF%E5%95%A5)），由方案作者更新維護，可直接通過 [plum](https://github.com/rime/plum) 安裝部署（關於如何安裝配方，請參照 HanhNgiox.net 上教程）。由於部分方案不存在於 GitHub，故此路徑下方案收錄不完整，
2. `unmaintained/` 路徑下爲从其他渠道收集得的方案文件，此类方案未配方化，无人更新维护，不保证可用性。
3. `download/` 用於存放各個語言的唯一權威版拼音，即爲 [發佈頁面](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases) 的下載整合包，方便用戶直接部署使用。
4. `script/` 內包含更新收錄碼表所需的代碼。使用方法請見 [使用教程](https://github.com/laubonghaudoi/Chinese_Rime#%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B%E9%A0%85%E7%9B%AE%E7%B6%B2%E7%AB%99-tutorial-project-website)。

有關已收集方案的资源，如方案白皮书、教程等，請參見 [方案相關文件（騰訊微雲）](https://github.com/laubonghaudoi/Chinese_Rime#%E8%B3%87%E6%BA%90resources)。

This repository has four sub-directories:

1. Folders under `sources/` are the source repositories of some schemas, preserved as submodules. Most of them are recipes (for an introduction to schema recipes, please see [Rime 輸入方案又是啥](https://github.com/rime/home/wiki/RimeWithSchemata#rime-%E8%BC%B8%E5%85%A5%E6%96%B9%E6%A1%88%E5%8F%88%E6%98%AF%E5%95%A5)) maintained by their authors, and can be installed and deployed by [plum](https://github.com/rime/plum) directly (please check out HanhNgiox.net on how to install recipes). Since not all schemas are maintained on GitHub, the collection in this directory is incomplete.
2. The `unmaintained/` directory preserves schemas from other sources which are not recipes. They are not maintained by anybody so the usabilities are not guaranteed.
3. `download/` serves as the folder for the [released](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases) packages. It contains only the selected schema for the prestige dialect of each language. Hence users can download, deploy and use these off-the-shelf schemas conveniently.
4. The `script/` folder contains scripts for automatically updating the schema files. Please see [Tutorial](https://github.com/laubonghaudoi/Chinese_Rime#%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B%E9%A0%85%E7%9B%AE%E7%B6%B2%E7%AB%99-tutorial-project-website) for instructions on how to use.

For related materials of the collected schemas, such as tutorials, schema white papers, etc., please see [Schema-related files (Tencent cloud)](https://github.com/laubonghaudoi/Chinese_Rime#%E8%B3%87%E6%BA%90resources)

<h2>使用教程
<br/>Tutorial</h2>

<h3>項目網站
<br/>Project website</h3>

關於如何使用方言拼音打字，請參考此網站：

For detailed steps with explanations on how to type Chinese characters with these schemas, please visit this website (simplified Chinese only):

<center><a href="http://www.hanhngiox.net"><font size="30"><b>漢語方言拼音輸入 HanhNgiox.net</b></font></a></center>

<h3>克隆此倉庫
<br/>Clone this repository</h3>

由於本倉庫體積過大，推薦運行以下命令來略過所有歷史記錄，僅克隆最新版的內容：

Considering the huge size of this repository, it is recommended to run the following command to skip all historical versions, cloning only the latest version of this repository:

```bash
git clone --depth=1 https://github.com/laubonghaudoi/Chinese_Rime.git
```

然後運行以下命令將全部子模塊內容克隆到本地：

Then run the following command to clone all submodules into the repository:

```bash
git submodule update --init --recursive
```

<h3>更新碼表
<br/>Update schemas</h3>

首先確保子模塊中內容已經克隆到本地，然後 `cd` 到 `script/` 下，運行以下命令來更新子模塊及下載包內方案文件：

First make sure you have cloned all submodules to local, then `cd` to `script/` and run the following commands to update all submodules and schema files in the download package:

```bash
# Update all submodules
chmod +x update_submodules.sh
./update_submodules.sh
# Update schema files in /download
python update_download.py
```

<h2>已收錄方案
<br/>Collected schemas</h2>

目前學界對漢語方言分類歸類問題仍存較大分歧。常見的分類方式有傳統的七分法、《中國語言地圖集》的十
分法和 ISO 國際標準的十三分法等。若使用傳統分法，則現代漢語族下分七大語支，官吳贛湘粵客閩。若採用《中國語言地圖集》之十分法，則晉語獨立於官話成一支，徽語獨立於吳語成一支，平話獨立於粵語成一支。若採用 ISO 693-3 標準的十三分法，則平話從屬於粵語，而閩語則細分爲閩北、閩南、閩東、閩中、莆仙五支，另外中古漢語和上古漢語各計作一門語言。

The taxonomy for Chinese languages and dialects has been an unsettled issue in academia. The traditional way (Jerry Norman 1988) puts Chinese languages into seven groups: Mandarin, Wu, Gan, Xiang, Cantonese, Hakka, Min, while the *Language Atlas of China* classifies them into 10 groups, separating Jin, Huizhou and Pinghua from Mandarin, Wu and Cantonese as independent languages. And the ISO 693-3 standard keeps Pinghua within Cantonese while further divides Min into Northern, Southern, Eastern, Central and Pu-Xian branches.

爲提高本項目可讀性和後續可維護性，本項目採用 ISO 標準的十三分法。此標準僅作參考，非最佳標準。若對此分類方式有任何疑問或意見，歡迎新開一個 issue 發起討論。下表爲此標準下各語言所對應的 ISO 639-3 代碼：

Considering the readability and maintainability of this project, here we adopt the ISO 693-3 system. This is for reference only and by no means the gold standard. If you have any questions or suggestions about this, feel free to open a new issue for discussion. The following table shows the ISO 639-3 codes for these languages.

| 上古漢語 Old Chinese | 中古漢語 Middle Chinese | 官話 Mandarin | 晉語 Jin | 吳語 Wu | 徽語 Huizhou | 贛語 Gan | 湘語 Xiang | 閩北語 Northern Min | 閩南語 Southern Min | 閩東語 Eastern Min| 閩中語 Central Min| 莆仙語 Pu-Xian Min | 客家話 Hakka | 粵語 Yue|
|----------|----------|------|------|------|------|------|------|--------|--------|--------|--------|--------|--------|------|
| och      | ltc      | cmn  | cjy  | wuu  | czh  | gan  | hsn  | mnp    | nan    | cdo    | czo    | cpx    | hak    | yue  |

目前 **暫缺閩北語、閩中語、徽語、贛語、湘語** 的輸入方案。如有作者已編寫以上語言的輸入方案，請 [聯系我](mailto:laubonghaudoi@icloud.com) 或新開一個 issue 以添加收錄。其他漢語或域外方音的方案亦強烈歡迎。

Right now we are still **missing the schemas for Northern Min, Central Min,  Huizhou, Gan, Xiang**. If you have composed a schema for any of the languages above, please [contact me](mailto:laubonghaudoi@icloud.com) or open a new issue to add it to the collection. Schemas for other Chinese languages are also highly welcomed.

以下爲方案總表和配方列表。其中配方以符號 ℞ 標識。

Below are the lists of all collected schemas and recipes, where recipes are marked with the symbol ℞.

---

<h3>方案列表（共 96 個方案）
<br/>Full list of collected schemas (96 schemas in total)</h3>

<ul>
  <li>
    <details>
      <summary>上古漢語 Old Chinese</summary>
      <ul>
        <li>上古全拼 - <code>dkzp</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>中古漢語 Middle Chinese</summary>
      <ul>
        <li>
          中古漢語（切韻音系）全拼及三拼 ℞
          <code>biopolyhedron/rime-middle-chinese</code>
          <ul>
            <li>中古全拼 - <code>zyenpheng</code></li>
            <li>中古三拼 - <code>triungkoxsampheng</code></li>
          </ul>
        </li>
        <li>
          爾切羅馬字 ℞ <code>rime-aca/rime-nieh-ched</code>
          <ul>
            <li>爾切羅馬字 - <code>nieh_ched</code></li>
          </ul>
        </li>
        <li>
          廣韻段毄攴字灋 ℞ <code>rime-aca/rime-kmg</code>
          <ul>
            <li>廣韻段毄攴字法 - <code>kmg</code></li>
          </ul>
        </li>
        <li>
          中古四拼 ℞ <code>inzoi/inzoi.github.io</code>
          <ul>
            <li>中古四拼 - <code>deuqguv4</code></li>
          </ul>
        </li>
        <li>
          唐韻（中古漢語）拼音方案 ℞ <code>rime-aca/rime-dangrvond</code>
          <ul>
            <li>唐韻 - <code>Dangrvond</code></li>
          </ul>
        </li>
        <li>中古汉拼 - <code>dghp</code></li>
        <li>廣韻羅馬字 - <code>kuankhiunn</code></li>
        <li>廣韻查詢 - <code>middle_chinese_lookup</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>官話 Mandarin</summary>
        <ul>
        <li>
          <details>
            <summary>中原官話 Central Plains Mandarin</summary>
            <ul>
              <li>
                中原官話洛陽方言 ℞ <code>Patricivs/lakyang</code>
                <ul>
                  <li>洛陽羅馬字 - <code>lakyang</code></li>
                  <li>洛陽註音 - <code>lakyang_chuim</code></li>
                </ul>
              </li>
              <li>
                中原官話輸入方案 ℞ <code>lotem/rime-zhung</code>
                <ul>
                  <li>中州羅馬字 - <code>zhung</code></li>
                  <li>中州打字速記法 - <code>zhung_stenotype</code></li>
                  <li>中州注音法（四十二鍵） - <code>zhung_42</code></li>
                  <li>中州羅馬字（並擊） - <code>zhung_combo</code></li>
                  <li>中州注音法（轉寫） - <code>zhung_transcript</code></li>
                  <li>中州注音法（並擊） - <code>zhung_combo_transcript</code></li>
                </ul>
              </li>
              <li>
                棗莊話羅馬字輸入方案 ℞ <code>tsauibusato/yihdjoouhuah </code>
                <ul>
                  <li>嶧州話傳統羅馬字 - <code>yihdjoouhuah</code></li>
                  <li>嶧州話羅馬字 - <code>yihjoouhuah_romatzyh</code></li>
                </ul>
              </li>
            </ul>
          </details>
        </li>
        <li>
          <details>
            <summary>膠遼官話 Jiaoliao Mandarin</summary>
            <b>暫缺 Not available</b>
          </details>
        </li>
        <li>
          <details>
            <summary>冀魯官話 Jiaoliao Mandarin</summary>
            <b>暫缺 Not available</b>
          </details>
        </li>
        <li>
          <details>
            <summary>蘭銀官話 Lan-Yin Mandarin</summary>
            <b>暫缺 Not available</b>
          </details>
        </li>
        <li>
          <details>
            <summary>江淮官話 Lower Yangtze Mandarin</summary>
            <ul>
              <li>
                南京話拼音输入法 ℞ <code>uliloewi/lang2jin1</code>
                <ul>
                  <li>南京官話拼音 - <code>langjin</code></li>
                </ul>
              </li>
              <li>泰如拼音 - <code>taerv</code></li>
              <li>南通方言 - <code>ntw</code></li>
            </ul>
          </details>
        </li>
        <li>
          <details>
            <summary>西南官話 Southwestern Mandarin</summary>
            <ul>
              <li>
                蜀拼 ℞ <code>Papnas/shupin</code>
                <ul>
                  <li>蜀拼通音 - <code>shupin_tongyin</code></li>
                  <li>蜀拼-成都 - <code>shupin_cendu</code></li>
                  <li>蜀拼-重慶 - <code>shupin_congqin</code></li>
                  <li>蜀拼-貴陽 - <code>shupin_guiyang</code></li>
                  <li>蜀拼-宜賓 - <code>shupin_libin</code></li>
                  <li>蜀拼-自貢 - <code>shupin_zigong</code></li>
                </ul>
              </li>
              <li>
                咵一咵湖北话 ℞ <code>yuxifongfei/hubehua</code>
                <ul>
                  <li>黃岡 - <code>huanggang</code></li>
                  <li>黃岡（混胡符版） - <code>huanggangxiangzhen</code></li>
                  <li>鄂城 - <code>ngocen</code></li>
                  <li>武漢 - <code>wuhan</code></li>
                </ul>
              </li>
            </ul>
          </details>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>晉語 Jin</summary>
      <ul>
        <li>嘉樂泉話 - <code>jieny</code></li>
        <li>晋拼解州片 - <code>haitrou</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>吳語 Wu</summary>
      <ul>
        <li>
          吳語協會式上海話輸入法 ℞ <code>edward-martyr/rime-yahwe_zaonhe</code>
          <ul>
            <li>吳協式上海言話 - <code>yahwe_zaonhe</code></li>
          </ul>
        </li>
        <li>
          吳語注音輸入方案吳語學堂版
          <ul>
            <li>
              上海吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_zaonhe</code>
              <ul>
                <li>吳語（上海） - <code>wugniu_zaonhe</code></li>
                <li>
                  吳語（上海老派） - <code>wugniu_zaonhe_laupha</code>
                </li>
                <li>吳語（松江） - <code>wugniu_sonkaon</code></li>
              </ul>
            </li>
            <li>
              蘇州吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_soutseu</code>
              <ul>
                <li>吳語（蘇州） - <code>wugniu_soutseu</code></li>
              </ul>
            </li>
            <li>
              寧波吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_gninpou</code>
              <ul>
                <li>吳語（寧波） - <code>wugniu_gninpou</code></li>
                <li>
                  吳語（鄞縣鍾公廟） - <code>wugniu_gninyu_tsonkonmiau</code>
                </li>
              </ul>
            </li>
            <li>
              嘉興（五縣兩區）吳語拼音輸入方案 ℞
              <code>NGLI/rime-wugniu_kashin</code>
              <ul>
                <li>吳語（桐鄉） - <code>wugniu_donshian</code></li>
                <li>吳語（海寧） - <code>wugniu_haegnin</code></li>
                <li>吳語（海鹽） - <code>wugniu_haeye</code></li>
                <li>吳語（嘉興） - <code>wugniu_kashin</code></li>
                <li>吳語（嘉善） - <code>wugniu_kazoe</code></li>
              </ul>
            </li>
            <li>吳語（永嘉） - <code>wugniu_ionko</code></li>
          </ul>
        </li>
        <li>
          吳語·上海話 ℞ <code>rime/rime-wugniu</code>
          <ul>
            <li>上海吳語 - <code>wugniu_lopha</code></li>
            <li>上海新派 - <code>wugniu</code></li>
          </ul>
        </li>
        <li>
          蘇州吳語 ℞ <code>rime/rime-soutzoe</code>
          <ul>
            <li>蘇州吳語 - <code>soutzoe</code></li>
          </ul>
        </li>
        <li>
          樂清話拼音輸入法 ℞ <code>lotem/rime-aoyu</code>
          <ul>
            <li>樂清柳東口音 - <code>ay_ncld</code></li>
            <li>樂清柳西口音 - <code>ay_ncls</code></li>
          </ul>
        </li>
        <li>標準吳語 - <code>pcngng</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>徽語 Huizhou</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>贛語 Gan</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>湘語 Xiang</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>閩北語 Northern Min</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>閩南語 Southern Min (Hokkien, Amoy, Taiwanese, Teochew)</summary>
      <ul>
        <li>
          閩南語輸入方案 ℞ <code>a-thok/rime-hokkien</code>
          <ul>
            <li>廈腔閩南語 - <code>blg_ha</code></li>
            <li>臺灣閩南語 - <code>blg_tai</code></li>
            <li>漳腔閩南語 - <code>blg_tsiang</code></li>
            <li>泉腔閩南語 - <code>blg_tsuan</code></li>
          </ul>
        </li>
        <li>
          閩南語拼音輸入方案 ℞ <code>LimTo/etaiBLG</code>
          <ul>
            <li>閩南語廈台腔專用版 - <code>blg_etai</code></li>
          </ul>
        </li>
        <li>閩倂輸入灋 - <code>mp</code></li>
        <li>
          潮语拼音输入法 ℞ <code>kahaani/dieghv</code>
          <ul>
            <li>潮語拼音〔潮州〕 - <code>dieziu</code></li>
            <li>潮語拼音〔潮阳〕 - <code>dioion</code></li>
            <li>潮語拼音〔揭阳〕 - <code>gekion</code></li>
            <li>潮語拼音〔汕头〕 - <code>suantau</code></li>
            <li>潮語拼音〔澄海〕 - <code>tenghai</code></li>
            <li>潮語拼音〔饒平〕 - <code>riaupeng</code></li>
          </ul>
        </li>
        <li>
          潮汕话輸入方案 ℞ <code>femkerr/dieghe</code>
          <ul>
            <li>潮語 - <code>diege_j</code></li>
            <li>潮語（帶潮語形聲鍵盤） - <code>diege</code></li>
            <li>潮語（形聲鍵盤） - <code>diege_gb</code></li>
          </ul>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>閩東語 Eastern Min</summary>
      <ul>
        <li>
          平話字表 (閩東語‣福州話) ℞ <code>only3km/ciklinbekin</code>
          <ul>
            <li>戚林八音 - <code>ciklinbekin</code></li>
            <li>福州話字典 - <code>dfd</code></li>
          </ul>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>閩中語 Central Min</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>莆仙語 Pu-Xian Min</summary>
      <ul>
        <li>
          兴化韵莆仙话输入方案 ℞ <code>Yaryou/HinghuaFactory</code>
          <ul>
            <li>興化韻莆音 - <code>Pouleng</code></li>
            <li>興化語平話字 - <code>HinghuaBUC</code></li>
          </ul>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>客家話 Hakka</summary>
      <ul>
        <li>
          崇正客語輸入法 ℞ <code>syndict/hakka</code>
          <ul>
            <li>客語 - <code>hakka</code></li>
            <li>客語-梅縣 - <code>hakka_meixian</code></li>
          </ul>
        </li>
        <li>客拼 - <code>hakka_pinyin</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>粵語 Yue (Cantonese)</summary>
      <ul>
        <li>
          粵拼 ℞ <code>rime/rime-jyutping</code>
          <ul>
            <li>粵拼 - <code>jyutping</code></li>
            <li>耶魯粵語拼音 - <code>yale</code></li>
            <li>香港廣東話拼音 - <code>hkcantonese</code></li>
          </ul>
        </li>
        <li>
          粵拼⁺ ℞ <code>rime-aca/rime-jyutping-plus</code>
          <ul>
            <li>粵拼⁺ - <code>jyutping+</code></li>
          </ul>
        </li>
        <li>
          粵語注音 ℞ <code>rime-aca/rime-zyujam</code>
          <ul>
            <li>粵語注音 - <code>zyujam</code></li>
          </ul>
        </li>
        <li>
          袖珍粵拼 ℞ <code>rime-aca/rime-jyutping-compact</code>
          <ul>
            <li>袖珍粵拼 - <code>jyutping_compact</code></li>
          </ul>
        </li>
        <li>
          南寧話輸入方案 ℞ <code>leimaau/naamning_jyutping</code>
          <ul>
            <li>南寧白話 - <code>naamning_baakwaa</code></li>
            <li>南寧（亭子）平話 - <code>naamning_bingwaa</code></li>
          </ul>
        </li>
        <li>
          沟漏片藤县白话输入方案 ℞
          <code>cryptogun/gaulau_jyutping</code>
          <ul>
            <li>
              粤语沟漏片藤县白话 - <code>jutjnyu_gaulaupin_dangjunbikwaa</code>
            </li>
          </ul>
        </li>
        <li>粵語雙拼 - <code>jyutsoeng</code></li>
        <li>梧州白話 - <code>NgZjau_JyutPing</code></li>
        <li>貴州韻 - <code>gvaizauvan</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>域外方音 Non-Sinitic Languages</summary>
      <ul>
        <li>
          한글 ℞ <code>rime-aca/rime-hangyl</code>
          <ul>
            <li>한글 - <code>hangyl</code></li>
            <li>한글・漢字 - <code>hangyl_hanja</code></li>
          </ul>
        </li>
        <li>
          옛한글・漢字 ℞ <code>biopolyhedron/rime-qyeyshanglr-hanja</code>
          <ul>
            <li>옛한글・漢字 - <code>qyeyshanglr_hanja</code></li>
          </ul>
        </li>
        <li>
          rime-hanja ℞ <code>sgalal/rime-hanja</code>
          <ul>
            <li>ハングル - <code>hangeul</code></li>
            <li>韓語漢字音 - <code>hanja</code></li>
          </ul>
        </li>
        <li>
          poly日文 ℞ <code>biopolyhedron/rime-jap-poly</code>
          <ul>
            <li>poly日文 - <code>jap_poly</code></li>
          </ul>
        </li>
        <li>
          rime-kunyomi ℞ <code>sgalal/rime-kunyomi</code>
          <ul>
            <li>訓読み - <code>kunyomi</code></li>
          </ul>
        </li>
        <li>古壮字拼音 - <code>sawndip</code></li>
        <li>輸入法𡨸漢喃 - <code>hannomPS</code></li>
      </ul>
    </details>
  </li>
</ul>

<h3>配方列表（共 36 個配方）
<br/>List of recipes (36 recipes in total)</h3>

<ul>
  <li>
    <details>
      <summary>上古漢語 Old Chinese</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>中古漢語 Middle Chinese</summary>
      <ul>
        <li>
          中古漢語（切韻音系）全拼及三拼 ℞
          <code>biopolyhedron/rime-middle-chinese</code>
        </li>
        <li>爾切羅馬字 ℞ <code>rime-aca/rime-nieh-ched</code></li>
        <li>廣韻段毄攴字灋 ℞ <code>rime-aca/rime-kmg</code></li>
        <li>中古四拼 ℞ <code>inzoi/inzoi.github.io</code></li>
        <li>唐韻（中古漢語）拼音方案 ℞ <code>rime-aca/rime-dangrvond</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>官話 Mandarin</summary>
        <ul>
        <li>
          <details>
            <summary>中原官話 Central Plains Mandarin</summary>
            <ul>
              <li>
                中原官話洛陽方言 ℞ <code>Patricivs/lakyang</code>
              </li>
              <li>
                中原官話輸入方案 ℞ <code>lotem/rime-zhung</code>
              </li>
              <li>
                棗莊話羅馬字輸入方案 ℞ <code>tsauibusato/yihdjoouhuah </code>
              </li>
            </ul>
          </details>
        </li>
        <li>
          <details>
            <summary>膠遼官話 Jiaoliao Mandarin</summary>
            <b>暫缺 Not available</b>
          </details>
        </li>
        <li>
          <details>
            <summary>冀魯官話 Jiaoliao Mandarin</summary>
            <b>暫缺 Not available</b>
          </details>
        </li>
        <li>
          <details>
            <summary>蘭銀官話 Lan-Yin Mandarin</summary>
            <b>暫缺 Not available</b>
          </details>
        </li>
        <li>
          <details>
            <summary>江淮官話 Lower Yangtze Mandarin</summary>
            <ul>
              <li>
                南京話拼音输入法 ℞ <code>uliloewi/lang2jin1</code>
              </li>
            </ul>
          </details>
        </li>
        <li>
          <details>
            <summary>西南官話 Southwestern Mandarin</summary>
            <ul>
              <li>
                蜀拼 ℞ <code>Papnas/shupin</code>
              </li>
              <li>咵一咵湖北话 ℞ <code>yuxifongfei/hubehua</code></li>
            </ul>
          </details>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>晉語 Jin</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>吳語 Wu</summary>
      <ul>
        <li>吳語協會式上海話輸入法 ℞ <code>edward-martyr/rime-yahwe_zaonhe</code></li>
        <li>上海吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_zaonhe</code></li>
        <li>蘇州吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_soutseu</code></li>
        <li>寧波吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_gninpou</code></li>
        <li>嘉興（五縣兩區）吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_kashin</code></li>
        <li>吳語·上海話 ℞ <code>rime/rime-wugniu</code></li>
        <li>蘇州吳語 ℞ <code>rime/rime-soutzoe</code></li>
        <li>樂清話拼音輸入法 ℞ <code>lotem/rime-aoyu</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>徽語 Hui</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>贛語 Gan</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>湘語 Xiang</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>閩北語 Northern Min</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>閩南語 Southern Min (Hokkien)</summary>
      <ul>
        <li>閩南語輸入方案 ℞ <code>a-thok/rime-hokkien</code></li>
        <li>閩南語拼音輸入方案 ℞ <code>LimTo/etaiBLG</code></li>
        <li>潮语拼音输入法 ℞ <code>kahaani/dieghv</code></li>
        <li>潮汕话輸入方案 ℞ <code>femkerr/dieghe</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>閩東語 Eastern Min</summary>
      <ul>
        <li>平話字表 (閩東語‣福州話) ℞ <code>only3km/ciklinbekin</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>閩中語 Central Min</summary>
      <b>暫缺 Not available</b>
    </details>
  </li>
  <li>
    <details>
      <summary>莆仙語 Pu-Xian Min</summary>
      <ul>
        <li>兴化韵莆仙话输入方案 ℞ <code>Yaryou/HinghuaFactory</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>客家話 Hakka</summary>
      <ul>
        <li>崇正客語輸入法 ℞ <code>syndict/hakka</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>粵語 Yue (Cantonese)</summary>
      <ul>
        <li>粵拼 ℞ <code>rime/rime-jyutping</code></li>
        <li>粵拼⁺ ℞ <code>rime-aca/rime-jyutping-plus</code></li>
        <li>粵語注音 ℞ <code>rime-aca/rime-zyujam</code></li>
        <li>袖珍粵拼 ℞ <code>rime-aca/rime-jyutping-compact</code></li>
        <li>南寧話輸入方案 ℞ <code>leimaau/naamning_jyutping</code></li>
        <li>沟漏片藤县白话输入方案 ℞ <code>cryptogun/gaulau_jyutping</code>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>域外方音 Non-Sinitic Languages</summary>
      <ul>
        <li>한글 ℞ <code>rime-aca/rime-hangyl</code></li>
        <li>옛한글・漢字 ℞ <code>biopolyhedron/rime-qyeyshanglr-hanja</code></li>
        <li>rime-hanja ℞ <code>sgalal/rime-hanja</code></li>
        <li>poly日文 ℞ <code>biopolyhedron/rime-jap-poly</code></li>
        <li>rime-kunyomi ℞ <code>sgalal/rime-kunyomi</code></li>
      </ul>
    </details>
  </li>
</ul>

---

下載包內方案信息詳見 [發佈](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases) 頁面。

For detailed information of the collected schemas in the download package, please see the [release](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases) page.

<h2>部分方案數據來源（非配方）
<br/>Incomplete list of sources of unmaintained schemas (non-recipes)</h2>

- 中古漢語
    - [廣韻查詢](https://gist.github.com/lotem/e964a81c1ea457a6ae92)
    - [廣韻羅馬字](https://gist.github.com/lotem/3950485)
    - [廣韻段毄攴字法](https://bintray.com/rime-aca/Schemata/KMG)
- 江淮官話
    - [泰如拼音](https://github.com/osfans/rime-tool/tree/master/data/y)
    - [南通方言](http://nantonghua.net/archives/7770)
- 粵語
    - [貴州韻](https://zhuanlan.zhihu.com/p/31464937)
- 晉語
    - [嘉樂泉話](https://github.com/osfans/rime-tool/tree/master/data/y)
- 域外方音
    - [古壮字拼音](https://zhuanlan.zhihu.com/p/24138023)

<h2>資源
<br/>Resources</h2>

<ul>
  <li>方案相關文件 Schema-related files</li>
  <ul>
    <li><a href="https://share.weiyun.com/5BqauQb">騰訊微雲 Tencent cloud</a></li>
    <li><a href="https://www.dropbox.com/sh/l5vxgdd05gp9oz4/AADz7xWYfZ5bAYmO4pElsqQDa?dl=0">Dropbox</a></li>
  </ul>
  <li><a href="http://share.sinolect.com/">藏书阁</a></li>
  <li>語言學習資源（方案白皮書、教程、字典）<br/>Language learning resources (schema white papers, tutorials, dictionaries, etc.)</li>
  <ul>
    <li>
      <details>
        <summary>中古漢語 Middle Chinese</summary>
        <ul>
          <li><a href="https://zh.wikipedia.org/wiki/User:Polyhedron/%E4%B8%AD%E5%8F%A4%E6%BC%A2%E8%AA%9E%E6%8B%BC%E9%9F%B3">中古漢語拼音</a></li>
          <li><a href="https://bkrs.info/taolun/attachment.php?aid=637">中古漢語基礎教程</a></li>
          <li><a href="http://www.guguolin.com/">古音手鏡</a></li>
        </ul>
      </details>
    </li>
    <li>
      <details>
        <summary>官話 Mandarin</summary>
        <ul>
          <li><a href="https://github.com/HesperusArcher/zhung/blob/master/Introduction.md">《中州羅馬字》拼音方案簡介</a></li>
          <li><a href="https://uliloewi.github.io/LangJinPinIn/SUMMARY">南京話拼音教程</a></li>
          <li><a href="http://nantonghua.net/">南通方言网</a></li>
          <li><a href="http://taerv.nguyoeh.com/">泰如方言</a></li>
          <li><a href="https://zhuanlan.zhihu.com/p/34562639">四川话通用拼音</a></li>
          <li><a href="https://github.com/yuxifongfei/hubehua/wiki">湖北话百科</a></li>
        </ul>
      </details>
    </li>
    <li>
      <details>
        <summary>吳語 Wu</summary>
        <ul>
          <li><a href="https://wugniu.com/">吴语学堂</a></li>
          <li><a href="http://wu-chinese.com/romanization/">吴语协会 通用吴语拼音</a></li>
          <li><a href="http://wu-chinese.com/minidict/">吴语协会 吴音小字典</a></li>
          <li><a href="http://input.foruto.com/wu/method.html">吳語注音法</a></li>
          <li><a href="https://shinzoqchiuq.github.io/gninpou-tutorial/">宁波话吴拼教程</a></li>
        </ul>
      </details>
    </li>
    <li>
      <details>
        <summary>閩南語 Southern Min (Hokkien)</summary>
        <ul>
          <li><a href="https://www.moedict.tw/'%E7%99%BC%E7%A9%8E">臺語萌典</a></li>
          <li><a href="http://www.ntcu.edu.tw/tailo/educate.htm">臺灣閩南語羅馬字拼音方案使用手冊</a></li>
          <li><a href="https://www.ispeakmin.com/bbs/">海墘閩語論壇</a></li>
          <li><a href="https://limkianhui.wordpress.com/">鹭水芗南－閩南語部落</a></li>
          <li><a href="http://hiteo.pw/">潮州話正音正字促進會</a></li>
          <li><a href="http://alt.reasoning.cs.ucla.edu/jinbo/dzl/">當代泉州音字彙</a></li>
          <li><a href="https://kahaani.github.io/gatian/index.html">潮语拼音教程</a></li>
          <li><a href="http://www.czyzd.com/">潮州音字典</a></li>
          <li><a href="https://www.mogher.com/">潮州·母语</a></li>
        </ul>
      </details>
    </li>
    <li>
      <details>
        <summary>閩東語 Eastern Min</summary>
        <ul>
          <li><a href="https://only3km.github.io/ciklinbekin/">平話字表 (閩東語‣福州話)</a></li>
          <li><a href="http://idioms.mindong.asia">福州话熟语大全</a></li>
        </ul>
      </details>
    </li>
    <li>
      <details>
        <summary>客家話 Hakka</summary>
        <ul>
          <li><a href="http://syndict.com/">薪典</a></li>
          <li><a href="https://www.moedict.tw/:%E7%99%BC%E8%8A%BD">客語萌典</a></li>
          <li><a href="https://depart.moe.edu.tw/ED2400/News.aspx?n=5EB26D97D6A29617&sms=8C59E176B3E3F56E">終身教育司-客家語</a></li>
          <li><a href="https://hakka.dict.edu.tw/hakkadict/index.htm">臺灣客家語常用詞辭典</a></li>
          <li><a href="http://hakka.fhl.net/dict/index_hakka.html">客語字典查尋</a></li>
        </ul>
      </details>
    </li>
    <li>
      <details>
        <summary>粵語 Yue (Cantonese)</summary>
        <ul>
          <li><a href="https://words.hk/">粵典</a></li>
          <li><a href="http://ling.cuhk.edu.hk/jyutpingteaching/">Jyutping Teaching 粵拼教學</a></li>
          <li><a href="https://www.howtostudycantonese.com/">粤塾</a></li>
          <li><a href="https://www.jyutdict.org/">泛粵大典</a></li>
          <li><a href="http://cccanto.org/#">CC-Canto</li>
          <li><a href="http://www.cantonese.sheik.co.uk/">Learn Cantonese</a></li>
          <li><a href="http://www.cantonese.asia/">粵語協會</a></li>
          <li><a href="http://www.cantonese.asia/attachments/school/canchars.htm">粵語字打法大全（2007賀歲版）</a></li>
          <li><a href="http://www.cantonese.asia/portal.php?mod=view&aid=229">Jyutping（粵拼）詳細教程</a></li>
          <li><a href="https://cantonesenotes.home.blog/">零二中文教學筆記</a></li>
          <li><a href="http://www.yueyu114.com/">粤语学习网·学广东话</a></li>
          <li><a href="https://cantolounge.com/">Cantolounge</a></li>
          <li><a href="https://leimaau.github.io/book/">南宁白话</a></li>
          <li><a href="https://github.com/tengtengteng/gvaizauvan/wiki">貴州韻</a></li>
        </ul>
      </details>
    </li>
  </ul>
  <li>
    <details>
      <summary>語言學參考 Linguistics references</summary>
      <ul>
        <li><a href="http://www.moe.gov.cn/s78/A19/A19_gggs/A19_sjhj/201704/W020170405307025943395.pdf">中国语言资源保护工程 汉语方言用字规范</a></li>
        <li><a href="https://zhongguoyuyan.cn/">中国语言资源保护工程采录展示平台</a></li>
        <li><a href="http://ccdc.fudan.edu.cn">复旦大学东亚语言数据中心</a></li>
        <li><a href="http://jiaxianghua.org">家乡话</a></li>
        <li><a href="http://phonemica.net/">鄉音苑</a></li>
        <li><a href="https://ixy.chsi.com.cn/">i乡音</a></li>
        <li><a href="http://cn.voicedic.com/">汉语方言发音字典</a></li>
        <li><a href="http://xiaoxue.iis.sinica.edu.tw/">小學堂</a></li>
        <li><a href="https://ytenx.org/">韻典網</a></li>
        <li><a href="http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/">粵語審音配詞字庫</a></li>
        <li><a href="https://jyut.net/">粵音資料集叢</a></li>
        <li><a href="http://corpus.eduhk.hk/JPwordlist/index.php">香港語言學學會粵拼詞表</a></li>
        <li><a href="http://gisun.org/">Gisun</a></li>
        <li><a href="http://www.ccamc.co/index.php">古今文字集成</a></li>
        <li><a href="http://suzukish.s252.xrea.com/search/">篇韻データベース</a></li>
        <li><a href="https://github.com/lingpy/sinopy">SinoPy</a></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>技術相關 Tech-related</summary>
      <ul>
        <li><a href="http://rime.im/">中州韻官網</a></li>
        <li><a href="https://github.com/EasyIME/PIME/releases">Pime輸入法</a></li>
        <li><a href="https://itunes.apple.com/us/app/irime%E8%BE%93%E5%85%A5%E6%B3%95-%E4%BA%94%E7%AC%94%E5%B0%8F%E9%B9%A4%E5%8F%8C%E6%8B%BC%E8%BE%93%E5%85%A5%E6%B3%95/id1142623977?mt=8">iRime输入法</a></li>
        <li><a href="https://play.google.com/store/apps/details?id=com.osfans.trime&hl=zh">同文輸入法</a></li>
        <li><a href="https://ngli.github.io/rime-wugniu/">吴语学堂拼音输入方案合集</a></li>
        <li><a href="https://github.com/MindongLab">閩東語實驗室</a></li>
      </ul>
    </details>
  </li>
</ul>

<h2>致謝（按筆畫-字母順序排列）
<br/>Acknowledgements (In strokes and alphabetical order)</h2>

- [佛振](https://github.com/lotem)
- [芽油](https://github.com/Yaryou)
- [滕謄](https://github.com/tengtengteng)
- [羽随风飞](https://github.com/yuxifongfei)
- [a-thok](https://github.com/a-thok)
- [biopolyhedron](https://github.com/biopolyhedron)
- [cryptogun](https://github.com/cryptogun)
- [Electric Sheep](https://github.com/shinzoqchiuq)
- [Hector Sioh](https://github.com/only3km)
- [inzoi](https://github.com/inzoi)
- [jimmy54](https://github.com/jimmy54)
- [LeiMaau](https://github.com/leimaau)
- [LimTo](https://github.com/LimTo)
- [lois.左](https://github.com/xunux)
- [osfans](https://github.com/osfans)
- [Papnas](https://github.com/Papnas)
- [Patrick T.](https://github.com/Patricivs)
- [sgal](https://github.com/sgalal)
- [syndict](https://github.com/syndict)
- [Tenda Huang](https://github.com/Kahaani)
- [tsauibusato](https://github.com/tsauibusato)
- [uliloewi](https://github.com/uliloewi)

<h2>參考資料
<br/>References</h2>

Eberhard, David M., Gary F. Simons, and Charles D. Fennig (eds.). 2019. Ethnologue: Languages of the World. Twenty-second edition. Dallas, Texas: SIL International. Online version: http://www.ethnologue.com.

Norman, J.L. (1988) Chinese. Cambridge University Press.

中国社会科学院语言研究所, 中国社会科学院民族学与人类学研究所. 2012. 中国语言地图集（第2版）：汉语方言卷. 商务印书馆.
