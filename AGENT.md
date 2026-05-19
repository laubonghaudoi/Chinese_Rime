# 新增輸入方案收錄流程

本文件供代理或維護者在本倉庫新增 Rime 輸入方案時使用。所有操作應以倉庫現有結構爲準，不要臆測路徑、分支或檔案清單。

## 1. 先確認收錄資訊

- 讀取相關 issue、上游 README、上游檔案列表，確認語言分類、方案名稱、倉庫網址、預設分支、`schema_id`、需要發佈的檔案。
- 若該語言分類尚未存在，需同時建立 `sources/<分類>/` 與 `download/<分類>/`。
- `sources/` 下的子目錄名稱優先使用可讀的中文方案名稱，例如 `sources/贛語/撫州話拼音輸入方案`，不要只用倉庫 slug，除非現有慣例或使用者明確要求。
- `download/` 下的目錄名稱應使用實際方言或權威下載包名稱，例如 `download/贛語/撫州話`。

## 2. 加入上游配方

- 用 submodule 收錄上游配方：

```bash
git submodule add <上游倉庫網址> sources/<分類>/<方案名稱>
```

- 確認 submodule 指向正確 commit 與分支：

```bash
git submodule status sources/<分類>/<方案名稱>
git ls-remote --symref <上游倉庫網址> HEAD
```

- 若上游預設分支是 `main`，需將 `./<分類>/<方案名稱>` 加入 `script/update_submodules.sh` 的 `branch_mains`。若上游使用 `master`，通常不需新增；若使用其他分支，需仿照現有特殊分支判斷加入明確規則。

## 3. 建立下載包

- 建立目標下載目錄：

```bash
mkdir -p download/<分類>/<下載包名稱>
```

- 從 submodule 複製發佈所需檔案到 `download/<分類>/<下載包名稱>/`。通常至少包含該方案的 `.schema.yaml` 與 `.dict.yaml`；若上游提供 `.custom.yaml`、共用字典、詞庫、`LICENSE` 或部署必需檔，也一併收錄。
- 下載包應盡量保留上游檔案內容，不要因爲格式偏好修改碼表資料。若上游字典有尾隨空白或 tab 欄位，但這些內容是原始資料的一部分，應保留。

## 4. 更新自動化來源表

- 在 `script/source_info.yaml` 新增下載包對應關係：

```yaml
<分類>/<下載包名稱>:
  source: <分類>/<方案名稱>/
  files:
    - <需要複製的檔案一>
    - <需要複製的檔案二>
```

- `files` 的清單必須與下載包實際需要的檔案一致，因爲 `script/update_download.py` 會根據此表清空並重建對應的 `download/` 目錄。
- 修改後需確認 YAML 可解析：

```bash
python3 -c "import yaml; yaml.safe_load(open('script/source_info.yaml', encoding='utf-8'))"
```

## 5. 更新 README

- 更新方案總數與配方總數。
- 若該分類原本列在「暫缺」清單中，從中文與英文缺失說明中移除。
- 在「方案列表」對應分類下新增方案條目；配方需用 `℞` 標記，並列出倉庫 `<owner>/<repo>` 與實際 `schema_id`。
- 在「配方列表」對應分類下新增同一配方。
- 若新增了新的作者或維護者，於致謝清單中加入 GitHub 連結，保持現有排序風格。
- 如上游提供重要教程、白皮書或網站，視需要更新「資源」區塊。

## 6. 驗證

完成後至少執行以下檢查：

```bash
git submodule status sources/<分類>/<方案名稱>
ls sources/<分類>/<方案名稱>/*.yaml
ls download/<分類>/<下載包名稱>/*
python3 -c "import yaml; yaml.safe_load(open('script/source_info.yaml', encoding='utf-8'))"
cd script && python3 update_download.py
git status --short
```

- 若有修改 shell、YAML、README 等本倉庫維護檔，應額外檢查這些檔案沒有意外空白錯誤：

```bash
git diff --check -- README.md script/source_info.yaml script/update_submodules.sh .gitmodules
```

- 不要因爲 `download/` 中直接複製的上游碼表觸發空白警告就擅自改寫上游資料；除非使用者明確要求整理格式。

## 7. 交付注意事項

- 回報時列出新增的 submodule 路徑、下載包路徑、更新的自動化設定與 README 變更。
- 明確說明已執行的驗證，以及任何保留的上游格式問題。
- 不要自動關閉或回覆 GitHub issue，除非使用者明確要求。
