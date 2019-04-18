# 中州韻輸入法漢語方言拼音方案全集

![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
![licence](https://img.shields.io/badge/licence-Apache--2.0-blue.svg?style=flat)

**[中文](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#%E4%B8%AD%E5%B7%9E%E9%9F%BB%E8%BC%B8%E5%85%A5%E6%B3%95%E6%BC%A2%E8%AA%9E%E6%96%B9%E8%A8%80%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88%E5%85%A8%E9%9B%86)        [English](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#collection-of-rime-input-method-schemas-for-chinese-topolectsdialects)**

## 項目宗旨

本倉庫收集現代漢語各大方言及上古、中古漢語的[中州韻輸入法](https://rime.im/)拼音輸入方案和字庫。本項目的目標有三：

1. 爲漢語非普通話使用者提供實用的拼音輸入方案，解決被迫使用普通話輸入法的困難。
2. 爲現代漢語方言、古漢語學習者提供實用便利的學習工具，通過拼音打字來練習正音和正字。
3. 爲學術研究（語言學、漢學、人類學等）提供參考資料。

本項目同作爲推廣漢語方言拼音輸入的支持項目，關於推廣漢語方言拼音的理念和宗旨詳情請閱讀[本文](https://laubonghaudoi.github.io/dialects/blog/mission.html)。

本倉庫分为四个子文件夹：

1. `sources/`路徑下爲各個輸入方案的來源倉庫，以子模块submodule的形式保存，方便方案作者實時更新自己的方案。由於部分方案不存在於GitHub，故此路徑下方案收錄不完整，
2. `unmaintained/`路徑下爲从其他渠道收集得的方案文件，此类文件不存在于GitHub上，无人更新维护，不保证可用性。
3. `download/`用於存放各個語言的唯一權威版拼音，即爲[發佈頁面](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases)的下載整合包，方便用戶直接部署使用。
4. `resources/`下为关于各个方案的其他资源，如方案白皮书、教程等，方便使用者学习参考。

## 使用教程（项目网站）

### [**漢語方言拼音輸入**](https://laubonghaudoi.github.io/dialects/)

## 已收錄方案

目前主要**缺失閩北語、閩中語、邵將語、瓊雷話、平話、湘語、贛語、徽語、蘭銀官話、膠遼官話**的輸入方案，如有作者已編寫以上語言的輸入方案，請[聯系我](mailto:laubonghaudoi@icloud.com)或新開一個issue以添加收錄。其他漢語或域外方音的方案亦強烈歡迎。

以下爲方案總表和配方列表。目前總共收錄32個配方的81個方案，其中配方以符號℞標識。

---

### 方案列表（共81個方案）

<ul>
  <li>
    <details>
      <summary>上古漢語</summary>
      <ul>
        <li>上古全拼 - <code>dkzp</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>中古漢語</summary>
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
      <summary>中原官話</summary>
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
      <summary>江淮官話</summary>
      <ul>
        <li>
          南京話拼音输入法 ℞ <code>uliloewi/lang2jin1</code>
          <ul>
            <li>南京官話拼音 - <code>langjin</code></li>
          </ul>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>西南官話</summary>
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
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>吳語</summary>
      <ul>
        <li>
          吳語注音輸入方案吳語學堂版
          <ul>
            <li>
              上海吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_zaonhe</code>
              <ul>
                <li>吳語（上海） - <code>wugniu_zaonhe</code></li>
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
              寧波吳語注音輸入方案吳語學堂版 ℞
              <code>NGLI/rime-wugniu_gninpou</code>
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
        <li>標準吳語 - <code>pcngng</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>粵語</summary>
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
          南寧白話輸入方案 ℞ <code>leimaau/naamning_jyutping</code>
          <ul>
            <li>南寧白話 - <code>naamning_jyutping</code></li>
          </ul>
        </li>
        <li>
          沟漏片藤县白话输入方案 ℞
          <code>cryptogun/rime-jutjnyu_gaulaupin_dangjunbikwaa</code>
          <ul>
            <li>
              粤语沟漏片藤县白话 - <code>jutjnyu_gaulaupin_dangjunbikwaa</code>
            </li>
          </ul>
        </li>
        <li>梧州白話 - <code>NgZjau_JyutPing</code></li>
        <li>貴州韻 - <code>gvaizauvan</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>閩東語</summary>
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
      <summary>閩南語</summary>
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
      <summary>莆仙語</summary>
      <ul>
        <li>
          興化工廠 ℞ <code>Yaryou/HinghuaFactory</code>
          <ul>
            <li>興化語莆田城關話 - <code>Pouleng</code></li>
            <li>興化語平話字 - <code>HinghuaBUC</code></li>
          </ul>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>客家話</summary>
      <ul>
        <li>
          崇正客語輸入法 ℞ <code>xunux/hakka-culture</code>
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
      <summary>晉語</summary>
      <ul>
        <li>晋拼解州片 - <code>haitrou</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>域外方音</summary>
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
          poly日文 ℞ <code>biopolyhedron/rime-jap-poly </code>
          <ul>
            <li>poly日文 - <code>jap_poly</code></li>
          </ul>
        </li>
        <li>古壮字拼音 - <code>sawndip</code></li>
        <li>輸入法𡨸漢喃 - <code>hannomPS</code></li>
      </ul>
    </details>
  </li>
</ul>

### 配方列表（共32個配方）

<ul>
  <li>
    <details>
      <summary>中古漢語</summary>
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
      <summary>中原官話</summary>
      <ul>
        <li>中原官話洛陽方言 ℞ <code>Patricivs/lakyang</code></li>
        <li>中原官話輸入方案 ℞ <code>lotem/rime-zhung</code></li>
        <li>棗莊話羅馬字輸入方案 ℞ <code>tsauibusato/yihdjoouhuah </code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>江淮官話</summary>
      <ul>
        <li>南京話拼音输入法 ℞ <code>uliloewi/lang2jin1</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>西南官話</summary>
      <ul>
        <li>蜀拼 ℞ <code>Papnas/shupin</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>吳語</summary>
      <ul>
        <li>上海吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_zaonhe</code></li>
        <li>蘇州吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_soutseu</code></li>
        <li>
          寧波吳語注音輸入方案吳語學堂版 ℞
          <code>NGLI/rime-wugniu_gninpou</code>
        </li>
        <li>
          嘉興（五縣兩區）吳語拼音輸入方案 ℞
          <code>NGLI/rime-wugniu_kashin</code>
        </li>
        <li>吳語·上海話 ℞ <code>rime/rime-wugniu</code></li>
        <li>蘇州吳語 ℞ <code>rime/rime-soutzoe</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>粵語</summary>
      <ul>
        <li>粵拼 ℞ <code>rime/rime-jyutping</code></li>
        <li>粵拼⁺ ℞ <code>rime-aca/rime-jyutping-plus</code></li>
        <li>粵語注音 ℞ <code>rime-aca/rime-zyujam</code></li>
        <li>袖珍粵拼 ℞ <code>rime-aca/rime-jyutping-compact</code></li>
        <li>南寧白話輸入方案 ℞ <code>leimaau/naamning_jyutping</code></li>
        <li>
          沟漏片藤县白话输入方案 ℞
          <code>cryptogun/rime-jutjnyu_gaulaupin_dangjunbikwaa</code>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>閩東語</summary>
      <ul>
        <li>平話字表 (閩東語‣福州話) ℞ <code>only3km/ciklinbekin</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>閩南語</summary>
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
      <summary>莆仙語</summary>
      <ul>
        <li>興化工廠 ℞ <code>Yaryou/HinghuaFactory</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>客家話</summary>
      <ul>
        <li>崇正客語輸入法 ℞ <code>xunux/hakka-culture</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>域外方音</summary>
      <ul>
        <li>한글 ℞ <code>rime-aca/rime-hangyl</code></li>
        <li>
          옛한글・漢字 ℞ <code>biopolyhedron/rime-qyeyshanglr-hanja</code>
        </li>
        <li>poly日文 ℞ <code>biopolyhedron/rime-jap-poly </code></li>
      </ul>
    </details>
  </li>
</ul>

---

下載包內方案信息詳見[發佈](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases)頁面。

## 部分方案數據來源（非GitHub子模塊）

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

<ul>
  <li>
    <details>
      <summary>語言學習資源（方案白皮書、教程、字典）</summary>
      <ul>
        <li>
          中古漢語
          <ul>
            <li><a href="https://zh.wikipedia.org/wiki/User:Polyhedron/%E4%B8%AD%E5%8F%A4%E6%BC%A2%E8%AA%9E%E6%8B%BC%E9%9F%B3">中古漢語拼音</a></li>
            <li><a href="https://bkrs.info/taolun/attachment.php?aid=637">中古漢語基礎教程</a></li>
            <li><a href="http://www.guguolin.com/">古音手鏡</a></li>
          </ul>
        </li>
        <li>
          官話
          <ul>
            <li><a href="https://uliloewi.github.io/LangJinPinIn/SUMMARY">南京話拼音教程</a></li>
            <li><a href="https://zhuanlan.zhihu.com/p/34562639">四川话通用拼音</a></li>
          </ul>
        </li>
        <li>
          吳語
          <ul>
            <li><a href="https://wugniu.com/">吴语学堂</a></li>
            <li><a href="http://wu-chinese.com/romanization/">吴语协会 通用吴语拼音</a></li>
            <li><a href="http://wu-chinese.com/minidict/">吴语协会 吴音小字典</a></li>
            <li><a href="http://input.foruto.com/wu/method.html">吳語注音法</a></li>
            <li><a href="https://shinzoqchiuq.github.io/gninpou-tutorial/">宁波话吴拼教程</a></li>
          </ul>
        </li>
        <li>
          粵語
          <ul>
            <li><a href="https://leimaau.github.io/book/">南宁白话</a></li>
            <li><a href="https://github.com/tengtengteng/gvaizauvan/wiki">貴州韻</a></li>
          </ul>
        </li>
        <li>
          閩語
          <ul>
            <li><a href="https://only3km.github.io/ciklinbekin/">平話字表 (閩東語‣福州話)</a></li>
            <li><a href="http://idioms.mindong.asia">福州话熟语大全</a></li>
            <li><a href="https://www.moedict.tw/'%E7%99%BC%E7%A9%8E">臺語萌典</a></li>
            <li><a href="http://www.ntcu.edu.tw/tailo/educate.htm">臺灣閩南語羅馬字拼音方案使用手冊</a></li>
            <li><a href="https://kahaani.github.io/gatian/index.html">潮语拼音教程</a></li>
            <li><a href="http://www.czyzd.com/">潮州音字典</a></li>
            <li><a href="https://www.mogher.com/">潮州·母语</a></li>
          </ul>
        </li>
        <li>
          客家話
          <ul>
            <li><a href="http://syndict.com/">薪典</a></li>
            <li><a href="https://www.moedict.tw/:%E7%99%BC%E8%8A%BD">客語萌典</a></li>
            <li><a href="http://hakka.fhl.net/dict/index_hakka.html">客語字典查尋</a></li>
          </ul>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>語言學參考</summary>
      <ul>
        <li><a href="http://www.moe.gov.cn/s78/A19/A19_gggs/A19_sjhj/201704/W020170405307025943395.pdf">中国语言资源保护工程 汉语方言用字规范</a></li>
        <li><a href="https://zhongguoyuyan.cn/">中国语言资源保护工程采录展示平台</a></li>
        <li><a href="http://ccdc.fudan.edu.cn">复旦大学东亚语言数据中心</a></li>
        <li><a href="http://jiaxianghua.org">家乡话</a></li>
        <li><a href="http://phonemica.net/">鄉音苑</a></li>
        <li><a href="http://xiaoxue.iis.sinica.edu.tw/">小學堂</a></li>
        <li><a href="https://ytenx.org/">韻典網</a></li>
        <li><a href="http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/">粵語審音配詞字庫</a></li>
        <li><a href="http://www.ccamc.co/index.php">古今文字集成</a></li>
        <li><a href="http://suzukish.s252.xrea.com/search/">篇韻データベース</a></li>
        <li><a href="https://github.com/lingpy/sinopy">SinoPy</a></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>技術相關</summary>
      <ul>
        <li><a href="http://rime.im/">中州韻官網</a></li>
        <li><a href="https://github.com/EasyIME/PIME/releases">Pime輸入法</a></li>
        <li><a href="https://itunes.apple.com/us/app/irime%E8%BE%93%E5%85%A5%E6%B3%95-%E4%BA%94%E7%AC%94%E5%B0%8F%E9%B9%A4%E5%8F%8C%E6%8B%BC%E8%BE%93%E5%85%A5%E6%B3%95/id1142623977?mt=8">iRime输入法</a></li>
        <li><a href="https://play.google.com/store/apps/details?id=com.osfans.trime&hl=zh">同文輸入法</a></li>
        <li><a href="https://github.com/MindongLab">閩東語實驗室</a></li>
      </ul>
    </details>
  </li>
</ul>

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
- [syndict](https://github.com/syndict)
- [Tenda Huang](https://github.com/Kahaani)
- [tsauibusato](https://github.com/tsauibusato)
- [uliloewi](https://github.com/uliloewi)

# Collection of Rime Input Method Schemas for Chinese Topolects/Dialects

**[中文](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#%E4%B8%AD%E5%B7%9E%E9%9F%BB%E8%BC%B8%E5%85%A5%E6%B3%95%E6%BC%A2%E8%AA%9E%E6%96%B9%E8%A8%80%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88%E5%85%A8%E9%9B%86)        [English](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema#collection-of-rime-input-method-schemas-for-chinese-topolectsdialects)**

## The Mission of this project

This repo collects the phonetic spelling schemas and character sets of [Rime input method](https://rime.im/) for Old Chinese, Middle Chinese and modern Chinese topolects/dialects. This project aims to:

1. Provide useful phonetic spelling input schemas for all non-Mandarin Chinese topolects/dialects, preventing the predicament where non-Mandarin Chinese speakers are compelled to type in Mandarin. 
2. Serve as a useful tool for Chinese topolect/dialect learners, as one can use phonetic spelling input to practice the standard pronunciation and orthography.
3. Provide references for academic researches (Linguistics, Sinology, Anthropology, etc.).  

This project also supports the promotion project of non-Mandarin phonetic spelling input. For a complete statement of the mission and motivation of the promotion, please read [this page](https://laubonghaudoi.github.io/dialects/blog/mission.html) (Chinese only).

This repo has four sub-directories:

1. Folders under the `sources/` directory are the source repos of some schemas, which are preserved as submodules so that the schema designers can maintain them. Since not all schemas are open-sourced on GitHub, the collection under this directory is incomplete. 
2. The `unmaintained/` directory preserves schemas from other sources (not from GitHub). They are not maintained by anybody so the usabilities are not guaranteed.  
3. The `download/` directory serves as the folder for the [released](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases) packages. It contains only the selected schema for the prestige dialect of each language. Hence users can download, deploy and use these off-the-shelf schemas conveniently.
4. The `resources/` directory stores materials about the collected schemas, such as tutorials, schema white papers, etc., as references and study materials for users.

## Tutorial

### Detailed introduction (Project Website)

For detailed steps and explanations, check out this website (Chinese only):

### [**漢語方言拼音輸入**](https://laubonghaudoi.github.io/dialects/)

### Short introduction

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

## Collected schemas

At the moment we are still **missing the schemas for Northern Min, Central Min, Shao-Jiang Min, Qiongleihua, Pinghua, Xiang, Gan, Huizhou, Lan–Yin Mandarin, Southwestern Mandarin**. If you have composed a schema for any of the languages above, please [contact me](mailto:laubonghaudoi@icloud.com) or open a new issue to include it to the collection. Schemas for other Chinese languages are also highly welcomed.

Up to now we have collected 32 recipes of 81 schemas. Below are the lists of all collected schemas and recipes, where recipes are marked with the symbol ℞.

---

### Full list of collected schemas (81 schemas in total)

<ul>
  <li>
    <details>
      <summary>Old Chinese</summary>
      <ul>
        <li>上古全拼 - <code>dkzp</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Middle Chinese</summary>
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
      <summary>Central Plains Mandarin</summary>
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
      <summary>Lower Yangtze Mandarin</summary>
      <ul>
        <li>
          南京話拼音输入法 ℞ <code>uliloewi/lang2jin1</code>
          <ul>
            <li>南京官話拼音 - <code>langjin</code></li>
          </ul>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Southwestern Mandarin</summary>
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
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Wu (Goetian)</summary>
      <ul>
        <li>
          吳語注音輸入方案吳語學堂版
          <ul>
            <li>
              上海吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_zaonhe</code>
              <ul>
                <li>吳語（上海） - <code>wugniu_zaonhe</code></li>
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
              寧波吳語注音輸入方案吳語學堂版 ℞
              <code>NGLI/rime-wugniu_gninpou</code>
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
        <li>標準吳語 - <code>pcngng</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Yue (Cantonese)</summary>
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
          南寧白話輸入方案 ℞ <code>leimaau/naamning_jyutping</code>
          <ul>
            <li>南寧白話 - <code>naamning_jyutping</code></li>
          </ul>
        </li>
        <li>
          沟漏片藤县白话输入方案 ℞
          <code>cryptogun/rime-jutjnyu_gaulaupin_dangjunbikwaa</code>
          <ul>
            <li>
              粤语沟漏片藤县白话 - <code>jutjnyu_gaulaupin_dangjunbikwaa</code>
            </li>
          </ul>
        </li>
        <li>梧州白話 - <code>NgZjau_JyutPing</code></li>
        <li>貴州韻 - <code>gvaizauvan</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Eastern Min</summary>
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
      <summary>Southern Min</summary>
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
      <summary>Pu-Xian Min</summary>
      <ul>
        <li>
          興化工廠 ℞ <code>Yaryou/HinghuaFactory</code>
          <ul>
            <li>興化語莆田城關話 - <code>Pouleng</code></li>
            <li>興化語平話字 - <code>HinghuaBUC</code></li>
          </ul>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Hakka</summary>
      <ul>
        <li>
          崇正客語輸入法 ℞ <code>xunux/hakka-culture</code>
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
      <summary>Jin</summary>
      <ul>
        <li>晋拼解州片 - <code>haitrou</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Foreign Dialects</summary>
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
          poly日文 ℞ <code>biopolyhedron/rime-jap-poly </code>
          <ul>
            <li>poly日文 - <code>jap_poly</code></li>
          </ul>
        </li>
        <li>古壮字拼音 - <code>sawndip</code></li>
        <li>輸入法𡨸漢喃 - <code>hannomPS</code></li>
      </ul>
    </details>
  </li>
</ul>

### List of recipes (32 recipes in total)

<ul>
  <li>
    <details>
      <summary>Middle Chinese</summary>
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
      <summary>Central Plains Mandarin</summary>
      <ul>
        <li>中原官話洛陽方言 ℞ <code>Patricivs/lakyang</code></li>
        <li>中原官話輸入方案 ℞ <code>lotem/rime-zhung</code></li>
        <li>棗莊話羅馬字輸入方案 ℞ <code>tsauibusato/yihdjoouhuah </code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Lower Yangtze Mandarin</summary>
      <ul>
        <li>南京話拼音输入法 ℞ <code>uliloewi/lang2jin1</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Southwestern Mandarin</summary>
      <ul>
        <li>蜀拼 ℞ <code>Papnas/shupin</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Wu (Goetian)</summary>
      <ul>
        <li>上海吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_zaonhe</code></li>
        <li>蘇州吳語拼音輸入方案 ℞ <code>NGLI/rime-wugniu_soutseu</code></li>
        <li>
          寧波吳語注音輸入方案吳語學堂版 ℞
          <code>NGLI/rime-wugniu_gninpou</code>
        </li>
        <li>
          嘉興（五縣兩區）吳語拼音輸入方案 ℞
          <code>NGLI/rime-wugniu_kashin</code>
        </li>
        <li>吳語·上海話 ℞ <code>rime/rime-wugniu</code></li>
        <li>蘇州吳語 ℞ <code>rime/rime-soutzoe</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Yue (Cantonese)</summary>
      <ul>
        <li>粵拼 ℞ <code>rime/rime-jyutping</code></li>
        <li>粵拼⁺ ℞ <code>rime-aca/rime-jyutping-plus</code></li>
        <li>粵語注音 ℞ <code>rime-aca/rime-zyujam</code></li>
        <li>袖珍粵拼 ℞ <code>rime-aca/rime-jyutping-compact</code></li>
        <li>南寧白話輸入方案 ℞ <code>leimaau/naamning_jyutping</code></li>
        <li>
          沟漏片藤县白话输入方案 ℞
          <code>cryptogun/rime-jutjnyu_gaulaupin_dangjunbikwaa</code>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Eastern Min</summary>
      <ul>
        <li>平話字表 (閩東語‣福州話) ℞ <code>only3km/ciklinbekin</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Southern Min</summary>
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
      <summary>Pu-Xian Min</summary>
      <ul>
        <li>興化工廠 ℞ <code>Yaryou/HinghuaFactory</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Hakka</summary>
      <ul>
        <li>崇正客語輸入法 ℞ <code>xunux/hakka-culture</code></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Foreign Dialects</summary>
      <ul>
        <li>한글 ℞ <code>rime-aca/rime-hangyl</code></li>
        <li>
          옛한글・漢字 ℞ <code>biopolyhedron/rime-qyeyshanglr-hanja</code>
        </li>
        <li>poly日文 ℞ <code>biopolyhedron/rime-jap-poly </code></li>
      </ul>
    </details>
  </li>
</ul>

---

For detailed information of the collected schemas in the download packege, please see the [release](https://github.com/laubonghaudoi/Chinese_dialect_Rime_schema/releases) page.

## Incomplete list of sources of unmaintained schemas

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

<ul>
  <li>
    <details>
      <summary>Language learning resources (schema white papers, tutorials, dictionaries, etc.)</summary>
      <ul>
        <li>
          中古漢語
          <ul>
            <li><a href="https://zh.wikipedia.org/wiki/User:Polyhedron/%E4%B8%AD%E5%8F%A4%E6%BC%A2%E8%AA%9E%E6%8B%BC%E9%9F%B3">中古漢語拼音</a></li>
            <li><a href="https://bkrs.info/taolun/attachment.php?aid=637">中古漢語基礎教程</a></li>
            <li><a href="http://www.guguolin.com/">古音手鏡</a></li>
          </ul>
        </li>
        <li>
          官話
          <ul>
            <li><a href="https://uliloewi.github.io/LangJinPinIn/SUMMARY">南京話拼音教程</a></li>
            <li><a href="https://zhuanlan.zhihu.com/p/34562639">四川话通用拼音</a></li>
          </ul>
        </li>
        <li>
          吳語
          <ul>
            <li><a href="https://wugniu.com/">吴语学堂</a></li>
            <li><a href="http://wu-chinese.com/romanization/">吴语协会 通用吴语拼音</a></li>
            <li><a href="http://wu-chinese.com/minidict/">吴语协会 吴音小字典</a></li>
            <li><a href="http://input.foruto.com/wu/method.html">吳語注音法</a></li>
            <li><a href="https://shinzoqchiuq.github.io/gninpou-tutorial/">宁波话吴拼教程</a></li>
          </ul>
        </li>
        <li>
          粵語
          <ul>
            <li><a href="https://leimaau.github.io/book/">南宁白话</a></li>
            <li><a href="https://github.com/tengtengteng/gvaizauvan/wiki">貴州韻</a></li>
          </ul>
        </li>
        <li>
          閩語
          <ul>
            <li><a href="https://only3km.github.io/ciklinbekin/">平話字表 (閩東語‣福州話)</a></li>
            <li><a href="http://idioms.mindong.asia">福州话熟语大全</a></li>
            <li><a href="https://www.moedict.tw/'%E7%99%BC%E7%A9%8E">臺語萌典</a></li>
            <li><a href="http://www.ntcu.edu.tw/tailo/educate.htm">臺灣閩南語羅馬字拼音方案使用手冊</a></li>
            <li><a href="https://kahaani.github.io/gatian/index.html">潮语拼音教程</a></li>
            <li><a href="http://www.czyzd.com/">潮州音字典</a></li>
            <li><a href="https://www.mogher.com/">潮州·母语</a></li>
          </ul>
        </li>
        <li>
          客家話
          <ul>
            <li><a href="http://syndict.com/">薪典</a></li>
            <li><a href="https://www.moedict.tw/:%E7%99%BC%E8%8A%BD">客語萌典</a></li>
            <li><a href="http://hakka.fhl.net/dict/index_hakka.html">客語字典查尋</a></li>
          </ul>
        </li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Linguistics references</summary>
      <ul>
        <li><a href="http://www.moe.gov.cn/s78/A19/A19_gggs/A19_sjhj/201704/W020170405307025943395.pdf">中国语言资源保护工程 汉语方言用字规范</a></li>
        <li><a href="https://zhongguoyuyan.cn/">中国语言资源保护工程采录展示平台</a></li>
        <li><a href="http://ccdc.fudan.edu.cn">复旦大学东亚语言数据中心</a></li>
        <li><a href="http://jiaxianghua.org">家乡话</a></li>
        <li><a href="http://phonemica.net/">鄉音苑</a></li>
        <li><a href="http://xiaoxue.iis.sinica.edu.tw/">小學堂</a></li>
        <li><a href="https://ytenx.org/">韻典網</a></li>
        <li><a href="http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/">粵語審音配詞字庫</a></li>
        <li><a href="http://www.ccamc.co/index.php">古今文字集成</a></li>
        <li><a href="http://suzukish.s252.xrea.com/search/">篇韻データベース</a></li>
        <li><a href="https://github.com/lingpy/sinopy">SinoPy</a></li>
      </ul>
    </details>
  </li>
  <li>
    <details>
      <summary>Tech related</summary>
      <ul>
        <li><a href="http://rime.im/">中州韻官網</a></li>
        <li><a href="https://github.com/EasyIME/PIME/releases">Pime輸入法</a></li>
        <li><a href="https://itunes.apple.com/us/app/irime%E8%BE%93%E5%85%A5%E6%B3%95-%E4%BA%94%E7%AC%94%E5%B0%8F%E9%B9%A4%E5%8F%8C%E6%8B%BC%E8%BE%93%E5%85%A5%E6%B3%95/id1142623977?mt=8">iRime输入法</a></li>
        <li><a href="https://play.google.com/store/apps/details?id=com.osfans.trime&hl=zh">同文輸入法</a></li>
        <li><a href="https://github.com/MindongLab">閩東語實驗室</a></li>
      </ul>
    </details>
  </li>
</ul>

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
- [syndict](https://github.com/syndict)
- [Tenda Huang](https://github.com/Kahaani)
- [tsauibusato](https://github.com/tsauibusato)
- [uliloewi](https://github.com/uliloewi)
