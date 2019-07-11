# 兴化韵莆仙话输入方案

基于[Rime](https://rime.im/)的莆仙话拼音输入方案。

由于莆仙话并无清浊对立，拼音的声母采用类普拼式，方便初学者学习掌握；韵母采用国际音标转写式，更为精确。

本拼音个人称为「莆拼」或「兴拼」，下文用「兴拼」代称。

本方案适用于莆田市区口音，其他口音使用者如果有词表也可以联系本人制作成输入码表。
Rime使用[具体教程](https://laubonghaudoi.github.io/dialects/)

## 莆仙拼音与国际音标的对照

### 声母

| 兴拼 | 国际音标 | 例字 |     
| :------: | :--------: | :----------: | 
| b |  p  | 白 ba 墨 bah | 
| p |  pʰ  | 浮 pu 蜂 pang |
| m |  m  | 名 mia 满 mua |
| d |  t  | 大 dua 德 deh |
| t |  tʰ  | 听 tia 窗 toeng |
| n |  n  | 篮 nor 年 ning |
| l |  l  | 留 lau 力 lih |
| z |  ts  | 姊 zi 装 zung |
| c |  tsʰ  | 菜 cai 葱 cang |
| s |  ɬ  | 线 syor 蟳 sing |
| g |  k  | 寒 gua  京 ging |
| k |  kʰ  | 看 kua 级 kih |
| ng |  ŋ  | 五 ngou 迎 nging |
| h |  h  | 虾 hor 兴 hing |
| 零声母 |  ʔ/不标  |  碗 ua 园 oeng |

### 韵母

#### 阴声韵
| 兴拼 | 国际音标 | 例字 |     
| :------: | :--------: | :----------: | 
| a |  a  | 生 sa 家 ga |
| or |  ɒ  | 三 sor 爬 bor |
| ae |  ɛ  | 十 sae 哂 sae |
| e |  e  | 街 ge 鞋 e |
| ee |  ø  | 螺 lee 酸 see |
| o |  o  | 学 o 过 go |
| i |  i  | 枝 gi 米 bi |
| y |  y  | 鱼 hy 箸 dy |
| u |  u  | 有 u 旧 gu |
| ai | ai  | 知 zai 眉 bai |
| au | au  | 走 zau 瓯 au |
| ou | ɔu  | 铺 pou 雨 hou |
| ia | ia  | 车 cia 声 sia |
| ieu | ieu  | 药 ieu 姜 gieu |
| iu | iu  | 油 iu 酒 ziu |
| ua | ua  | 花 hua 话 ua |
| ue | ue  | 火 hue 软 nue |
| ui | ui  | 水 zui 雷 lui |
| yor | yɒ  | 纸 zyor 蚮 dyor |

#### 阳声韵
| 兴拼 | 国际音标 | 例字 |     
| :------: | :--------: | :----------: | 
| ang | aŋ  | 东 dang 红 ang |
| orng | ɒŋ  | 工 gorng 丰 porng |
| eng | ɛŋ  |  边 beng 信 seng |
| oeng | œŋ  |  中 doeng 勇 oeng |
| ong | ɔŋ  |  分 bong 军 gong |
| ing | iŋ  |  冰 bing 天 ting |
| ieng | iɛŋ  |  咸 gieng 掀 hieng |
| ung | uŋ  |  糖 tung 两 nung |
| uang | uaŋ  |  蒜 suang 湾 uang |
| yng | yŋ  |  斤 gyng 恩 yng |
| yorng | yɒŋ  |  乡 hyorng 央 yorng |
| 声化韵ng | ŋ̍  |  黄 ng 方 hng |

#### 入声韵
| 兴拼 | 国际音标 | 例字 |     
| :------: | :--------: | :----------: | 
| ah | aʔ  | 读 tah 盒 ah |
| orh | ɒʔ  | 木 borh 曝 porh |
| eh | ɛʔ  | 热 zeh 踢 teh |
| oeh | œʔ  | 肉 noeh 熟 soeh |
| oh | ɔʔ  | 骨 goh 出 coh |
| ih | iʔ  | 笔 bih 日 dih |
| iah | iaʔ  | 食 siah 揲 iah |
| ieh | iɛʔ  | 叶 ieh 接 zieh |
| uah | uaʔ  | 发 huah 刷 suah |
| uoh | uoʔ  | 我 guoh |
| yh | yʔ  | 疫 yh 汝 dyh |
| yorh | yɒʔ  | 却 kyorh 芍 syorh |

#### 声调标记方法示例
使用时不需要输入声调，候选字会附带调号以提供辨识，如「兴」hing1。

| 调类 | 调值 | 例字/调号 |     
| :------: | :--------: | :----------: | 
| 阴平 |  533 | 诗 si1 |
| 阳平 | 13  | 时 si2 |
| 上声 | 453  | 始 si3 |
| 阴去 | 42  | 四 si4 |
| 阳去 | 11  | 寺 si5 |
| 阴入 | 21  | 室 sih6 |
| 阳入 | 4  | 实 sih7 |

#### 模糊音的使用
本方案加入了模糊音，分为简码和类普拼输入、容错。

简码是为了提高输入速度；

类普拼是为了辅助不熟悉「兴拼」的初学者，使用音近的普通话拼音也能键入正确的字。

容错是允许一部分键位错误，如把「安 ang」打成「am」,也是能打出这个字的。

#### 类普拼式
| 原码 | 模糊码 | 例字 |
| :------: | :--------: | :----------: | 
| y | v  | 鱼 |
| au | ao | 豆 |
| ieng | ian | 咸 |
| ieng | yan | 盐 |
| ieu | iao | 药 |
| yorng | iong | 伤 |
| ia | ya | 野 |
| i | yi | 衣 |
| iu | you | 游 |
| y | yu | 于 |
| uang | wan | 弯 |
| ue | wei | 丸 |
| ui | wui | 为 |
| ua | wa | 画 |
| u | wu | 污 |

#### 简码
| 原码 | 模糊码 | 例字 |
| :------: | :--------: | :----------: | 
| yor | yo | 蚁 |
| yor | io | 艾 |
| yorng | yong | 强 |
| yorng | iong | 厂 |
| yorh | yoh | 约 |
| orh | oq | 国 |
| zyor | jo | 纸 |
| zyorng | jong | 章 |
| ung | ng | 囥 |
 
#### 鼻音韵尾简化
鼻音韵尾可以略去g，如「安 ang」可用「an」键入，以此类推。

#### 颚化
| 原码 | 模糊码 | 例字 |
| :------: | :--------: | :----------: | 
| zi | ji | 字 |
| ci | qi | 饲 |
| si | xi | 舌 |
| zy | ju | 煮 |
| cy | qu | 鼠 |
| sy | xu | 薯 |
