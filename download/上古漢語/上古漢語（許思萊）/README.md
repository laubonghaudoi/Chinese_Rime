# 上古音輸入方案：許思萊擬音

鳴謝：<br>
[字統網](https://zi.tools/)

> 許思萊（Axel Schuessler）耕耘上古漢語的語義和語源。古音構擬……主要成果體現在《簡約上古音和東漢音》一書中。許思萊擬音是簡約的，原因可能是他主攻語義、語源，不希望被擬音中「激進的、不確定的」的成分影響。<br>
> [*古音小鏡 2022.5.20*](http://www.kaom.net/ny_box.php?name=xusilai)

---
許思萊擬音依照歷史分期，對應兩個輸入方案：一是上古漢語（Old Chinese），對應 `OC_schuesslerOC` 方案；二是東漢漢語（Later *Hàn* Chinese），對應 `OC_schuesslerLHC` 方案。兩套方案的輸入轉寫規則稍異。

[散復生（Geoffrey Sampson）](https://www.grsampson.net/)在其著作《[Voices from Early China](https://www.cambridgescholars.com/product/978-1-5275-5212-8)》中給出了詩經全文的許氏擬音，但對擬音細節有所修改。正字後合併到一起，用 `Ⓖ` 標記，以示區分。

[畢鶚（Wolfgang Behr）](https://www.aoi.uzh.ch/en/sinologie/persons/professoren/behr.html)的[金文擬音](https://www.researchgate.net/publication/281215287_Reimende_Bronzeinschriften_und_die_Entstehung_der_chinesischen_Endreimdichtung)同許氏的上古漢語擬音比較相似，合併到一起，標記了 `Ⓑ` 的候選準此。

## 上古漢語方案轉寫說明

| 擬音 | 轉寫 |
| :---: | :---: |
| ◌̂ - | 不寫 |
| ə | y |
| ŋ | ng |
| ʔ（*影） | x 或不寫 |
| ʔ（*上） | x |
| ◌̥ ◌̊ ʰ | h |
| ɦ | hh 或 f |
| i、j | 可以混淆 |
| u、w | 可以混淆 |
| 附加畢鶚擬音 | Z 鍵引導 |
| 大寫字母 | 單、雙小寫 |

## 東漢漢語方案轉寫說明

本方案將許氏東漢漢語擬音原有的記音符號用 IPA 標記：

| 原書符號 | IPA |
| :---: | :---: |
| ṭ ḍ ṇ | ʈ ɖ ɳ |
| ṣ ẓ | ʂ ʐ |
| ś ź ń | ɕ ʑ ȵ |

默認將 ṣ ẓ 記爲 ʂ ʐ 。取消 `OC_schuesslerLHC.schema.yaml` 中第 80、81 行的註釋可將其記爲 ʃ ʒ。

| 擬音 | 轉寫 |
| :---: | :---: |
| 調類 | 不寫 |
| ɑ | aa |
| ɛ | ee |
| ɔ | oo |
| ə | y |
| ɨ | r |
| ɥ | y |
| ʔ | x 或不寫 |
| ʰ | h |
| ŋ | ng |
| ʈ ɖ ɳ | tr dr nr |
| ʂ ʐ | sr zr |
| tɕ ɕ ʑ ȵ | tch sh zh nh |
| ɦ | hh 或 f |
| ɣ | xx 或 v |
| i、j | 可以混淆 |
| u、w | 可以混淆 |