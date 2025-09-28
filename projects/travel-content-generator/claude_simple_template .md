# CLAUDE_SIMPLE.md - 旅遊社群行銷系統 (Git Bash版)

> **Project**: 25年旅行社 5通路社群行銷系統  
> **Environment**: Git Bash Terminal  
> **Learning Stage**: Day 1 實戰任務  
> **Focus**: 旅遊貼文生成器 + 基礎規則

## 🎯 **今日任務目標**
建立能為FB、IG、LINE、官網、電子報生成優質旅遊內容的系統

### ✅ **BEFORE EVERY TASK - ACKNOWLEDGE**
```
✅ RULES ACKNOWLEDGED - I will follow basic prohibitions and requirements
✅ BRAND PROFILE READY - I will refer to ../BRAND_PROFILE.md for brand style
✅ 5-CHANNEL FOCUS - I will create content suitable for all 5 marketing channels
```

## 🚨 **ESSENTIAL RULES FOR TRAVEL MARKETING**

### ❌ **NEVER DO (絕對禁止)**
```yaml
NEVER_CREATE_IN_ROOT:
  # 絕不在根目錄建立檔案
  wrong: "post_generator.py in root directory"
  right: "src/generators/post_generator.py"

NEVER_USE_BAD_COMMANDS:
  # 絕不使用會失敗的指令  
  prohibited: ["find", "grep", "cat", "head", "tail"]
  use_instead: ["Read", "LS", "Grep", "Glob"]

NEVER_GENERIC_CONTENT:
  # 絕不生成通用內容，必須符合25年旅行社品牌
  wrong: "一般旅遊貼文"
  right: "基於BRAND_PROFILE.md的專業品牌風格內容"

NEVER_SKIP_COMMIT:
  # 絕不跳過提交
  rule: "每完成一個生成器就立即 commit"
  reason: "記錄開發進度，防止工作遺失"
```

### ✅ **ALWAYS DO (必須執行)**
```yaml
REFER_BRAND_PROFILE:
  # 總是參考品牌檔案
  command: "請根據../BRAND_PROFILE.md中的品牌風格..."
  reason: "確保所有內容符合25年旅行社的專業形象"

SEARCH_BEFORE_CREATE:
  # 創建前先搜尋
  command: "Grep pattern='generator.*travel' include='*.py'"
  reason: "避免重複開發類似功能"

READ_BEFORE_EDIT:
  # 編輯前必讀
  command: "Read file_path='src/generators/post_generator.py'"
  reason: "編輯工具需要先讀取檔案"

MULTI_CHANNEL_DESIGN:
  # 多通路設計
  rule: "每個內容生成器都要考慮5個行銷通路的需求"
  channels: ["Facebook", "Instagram", "LINE", "Website", "Email"]

COMMIT_WITH_DETAILS:
  # 詳細提交訊息
  format: "feat: add [feature] for [channel] - [brief description]"
  example: "feat: add Facebook post generator - generates engaging travel posts with 25-year expertise"
```

## 📁 **TRAVEL MARKETING PROJECT STRUCTURE**
```
travel-content-generator/
├── CLAUDE_SIMPLE.md           # 這個規則檔案
├── README.md                  # 專案說明
├── BRAND_PROFILE.md          # 品牌檔案 (從上層複製)
├── src/                      # 所有程式碼
│   ├── generators/           # 內容生成器
│   │   ├── facebook_generator.py    # FB貼文生成器
│   │   ├── instagram_generator.py   # IG貼文生成器
│   │   ├── line_generator.py        # LINE內容生成器
│   │   ├── website_generator.py     # 官網文章生成器
│   │   └── email_generator.py       # 電子報生成器
│   ├── templates/            # 內容模板
│   │   └── brand_templates.py       # 品牌風格模板
│   └── utils/               # 工具函數
│       └── content_utils.py         # 內容處理工具
├── data/                    # 旅遊資料
│   ├── destinations.json    # 目的地資訊
│   ├── packages.json       # 套裝產品
│   └── customer_cases.json # 客戶案例
├── output/                  # 生成內容輸出
│   ├── facebook/           # FB貼文輸出
│   ├── instagram/          # IG貼文輸出
│   ├── line/              # LINE內容輸出
│   ├── website/           # 官網文章輸出
│   └── email/             # 電子報輸出
├── tests/                  # 測試檔案
└── .gitignore             # Git 忽略檔案
```

## 🛠️ **DAY 1 具體實施步驟**

### **步驟1-3: 基礎環境 (已完成)**
```bash
# 1. 建立專案 (你應該已經完成)
cd D:\claude-learning\git-bash-practice
mkdir travel-content-generator
cd travel-content-generator
git init

# 2. 建立結構 (你應該已經完成)
mkdir -p src/{generators,templates,utils} data output/{facebook,instagram,line,website,email} tests

# 3. 基礎檔案 (你應該已經完成)
echo "# 25年旅行社 5通路行銷內容生成系統" > README.md
```

### **步驟4: 建立品牌資訊檔案 (手動操作)**
```bash
# 4.1 複製品牌檔案
# 手動操作：將 D:\claude-learning\vscode-practice\BRAND_PROFILE.md 
# 複製到 D:\claude-learning\git-bash-practice\travel-content-generator\

# 4.2 建立基礎資料檔案
echo '{"destinations": ["日本", "韓國", "東南亞", "歐洲"], "specialties": ["客製化行程", "深度文化體驗", "美食之旅"]}' > data/destinations.json

# 4.3 建立.gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.so

# 輸出檔案
*.tmp
*.log

# 敏感資料
config/secrets.json

# IDE
.vscode/
.idea/
EOF

# 4.4 提交基礎設定
git add .
git commit -m "setup: initialize travel marketing project structure

✅ Created 5-channel marketing system structure
✅ Added brand profile and data files  
✅ Set up proper directory organization
✅ Ready for content generator development"
```

### **步驟5: 使用Claude建立第一個貼文生成器**
```bash
# 5.1 開始開發 Facebook 貼文生成器
claude "請根據我的BRAND_PROFILE.md檔案中的25年旅行社品牌風格，為我建立一個Facebook貼文生成器 (src/generators/facebook_generator.py)。

要求：
1. 能生成吸引人的旅遊FB貼文
2. 符合我們25年專業旅行社的品牌調性
3. 包含不同類型：教育性、靈感性、服務展示、互動參與
4. 可以根據目的地、季節、客群類型生成客製化內容
5. 每篇貼文控制在150-200字，包含適當hashtag

請直接建立檔案到正確位置。"

# 5.2 測試生成器功能
# Claude會建立檔案後，你可以執行：
python src/generators/facebook_generator.py

# 5.3 檢查輸出結果
ls output/facebook/
# 應該會看到生成的貼文檔案
```

### **步驟6: Git commit 記錄進度 (詳細操作)**
```bash
# 6.1 檢查當前狀態
git status
# 這會顯示：
# - 新增的檔案 (綠色 - 已staged)
# - 修改的檔案 (紅色 - 未staged)
# - 未追蹤的檔案 (紅色 - 新檔案)

# 6.2 查看具體變更內容
git diff
# 顯示檔案內容的具體變更

# 6.3 查看新建立的檔案
ls -la src/generators/
# 確認 facebook_generator.py 已建立

# 6.4 查看生成的內容
ls -la output/facebook/
# 確認有輸出檔案

# 6.5 加入所有新檔案到暫存區
git add .

# 6.6 確認暫存區狀態
git status
# 所有檔案應該顯示為綠色 (已staged)

# 6.7 提交變更 (使用詳細訊息)
git commit -m "feat: add Facebook post generator for travel marketing

✅ Implemented Facebook post generator based on 25-year travel agency brand
✅ Supports 4 content types: educational, inspirational, service, interactive
✅ Customizable by destination, season, and target audience
✅ Generates posts with optimal length (150-200 words) and hashtags
✅ Output saved to output/facebook/ directory

Generated sample posts for testing and validation."

# 6.8 查看提交歷史
git log --oneline
# 應該顯示你的提交記錄

# 6.9 查看詳細提交資訊
git log -1
# 顯示最近一次提交的完整資訊

# 6.10 確認工作目錄狀態
git status
# 應該顯示 "nothing to commit, working tree clean"
```

## 🔍 **如何檢查 Day 1 任務完成狀況**

### **完整檢查清單**
```bash
# ✅ 1. 檢查專案結構是否正確
tree  # 或使用 ls -la 檢查各資料夾

# ✅ 2. 檢查品牌檔案是否存在
cat BRAND_PROFILE.md  # 確認內容正確

# ✅ 3. 檢查Python檔案是否建立
ls -la src/generators/
cat src/generators/facebook_generator.py  # 確認程式碼內容

# ✅ 4. 檢查是否有輸出內容
ls -la output/facebook/
cat output/facebook/*.txt  # 查看生成的貼文

# ✅ 5. 檢查Git狀態
git status  # 應該顯示 clean
git log --oneline  # 查看提交記錄

# ✅ 6. 測試功能是否正常
python src/generators/facebook_generator.py  # 重新執行確認
```

## 🎯 **成功標準**
完成Day 1後，你應該有：
- [ ] 完整的專案資料夾結構
- [ ] BRAND_PROFILE.md 品牌檔案
- [ ] facebook_generator.py 可運行的生成器
- [ ] output/facebook/ 中有實際生成的貼文內容
- [ ] 清晰的Git提交記錄
- [ ] 無錯誤的程式執行結果

## 🚀 **下一步準備**
Day 1 完成後，準備開發：
- Instagram 貼文生成器
- LINE 內容生成器  
- 官網文章生成器
- 電子報內容生成器

每個生成器完成都要立即commit！