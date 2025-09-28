# 🚀 ClaudeV 開發環境完整指南

> **整合 Claude AI 的多專案開發工作區**
> 專為 VS Code 和 Git Bash 協作開發而設計

## 📁 專案結構總覽

```
D:/claudeV/
├── 📂 projects/                    # 主要開發專案
│   ├── 🌐 naturetour-website/     # 自然國際旅行社官網升級
│   │   ├── 📚 docs/               # 開發文檔
│   │   ├── 📄 content/            # 內容結構規劃
│   │   ├── 🎨 branding/           # 品牌指南
│   │   ├── 📱 marketing/          # 行銷內容模板
│   │   ├── 🔧 elementor-widgets/  # 自訂 Elementor 元件
│   │   └── 🎨 wordpress-theme/    # WordPress 主題檔案
│   ├── 📝 travel-content-generator/# 旅遊內容生成工具
│   └── ✍️ wulitou-writer/          # 無厘頭寫作助手
├── 🛠️ tools/                       # 開發工具配置
│   ├── 💻 vscode-config/          # VS Code + Claude 設定
│   └── 🔧 git-bash/               # Git Bash 配置
├── 📋 README.md                    # 基本說明文件
└── 📖 DEVELOPMENT_GUIDE.md         # 此詳細指南
```

## 🎯 專案詳細說明

### 🌐 naturetour-website
**自然國際旅行社官網升級專案**

**技術棧**: WordPress + Elementor + Gulp
**主要功能**:
- 📱 完全響應式設計
- 🎨 品牌色彩系統化
- 📧 電子報內容管理
- 🤖 AI 輔助內容生成
- 🏷️ SEO 優化

**重要檔案**:
- `package.json` - Node.js 依賴和腳本
- `marketing/content_template_rules.md` - 內容規範和模板
- `marketing/travel_marketing_prompts.md` - AI Prompt 範例庫
- `branding/品牌色彩升級指南.md` - 品牌視覺規範

**開發指令**:
```bash
cd projects/naturetour-website
npm install           # 安裝依賴
npm run dev          # 開發模式（監控文件變化）
npm run build        # 建置生產版本
npm run deploy       # 部署到伺服器
```

### 📝 travel-content-generator
**旅遊內容自動生成工具**

**技術棧**: Python 3.8+
**主要功能**:
- 🎯 Facebook 貼文自動生成
- 📊 目標客群分析
- 🗺️ 目的地資料管理
- 📱 社群媒體內容最佳化

**重要檔案**:
- `src/generators/facebook_generator.py` - 主要生成器
- `data/destinations.json` - 目的地資料庫
- `README_Facebook_Generator.md` - 使用說明

**開發指令**:
```bash
cd projects/travel-content-generator
python -m venv venv                    # 建立虛擬環境
source venv/bin/activate               # 啟動虛擬環境 (Linux/Mac)
# 或 venv\Scripts\activate            # Windows
pip install -r requirements.txt       # 安裝依賴
python src/generators/demo_usage.py   # 執行示範
```

### ✍️ wulitou-writer
**無厘頭創意寫作工具**

**技術棧**: JavaScript/Node.js
**主要功能**:
- 🎭 多種創意寫作風格
- 📊 文章輸出管理
- ⚙️ 可自訂角色設定
- 🎯 主題導向創作

**重要檔案**:
- `src/wulitou_writer.js` - 主程式
- `config/character_profile.json` - 角色設定
- `templates/input_template.json` - 輸入範本

**開發指令**:
```bash
cd projects/wulitou-writer
npm install                    # 安裝依賴
node src/wulitou_writer.js    # 執行程式
```

## 🛠️ 開發環境完整設置

### 1️⃣ VS Code 完整配置

**必裝擴展**:
```json
{
  "recommendations": [
    "claude-ai.claude-code",      // Claude AI 官方整合
    "eamodio.gitlens",           // Git 增強功能
    "ms-python.python",          // Python 支援
    "bradlc.vscode-tailwindcss", // CSS 框架支援
    "formulahendry.auto-rename-tag", // HTML 標籤自動重命名
    "ms-vscode.vscode-json"      // JSON 格式支援
  ]
}
```

**VS Code 設定** (`tools/vscode-config/settings.json`):
```json
{
  "claude.autoComplete": true,
  "claude.diagnostics": true,
  "files.autoSave": "afterDelay",
  "editor.formatOnSave": true,
  "python.defaultInterpreterPath": "./venv/bin/python",
  "git.enableSmartCommit": true
}
```

**工作區設定**:
```bash
# 開啟整個工作區
code D:/claudeV

# 或開啟特定專案
code D:/claudeV/projects/naturetour-website
```

### 2️⃣ Git Bash 最佳化設置

**常用別名設置** (加入 `~/.bashrc` 或 `~/.bash_profile`):
```bash
# 專案快速切換
alias cdn='cd /d/claudeV/projects/naturetour-website'
alias cdtc='cd /d/claudeV/projects/travel-content-generator'
alias cdww='cd /d/claudeV/projects/wulitou-writer'
alias cdcv='cd /d/claudeV'

# Git 快速指令
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push origin'
alias gl='git pull origin'

# 專案狀態檢查
alias pstatus='cd /d/claudeV && echo "=== Git Status ===" && git status && echo -e "\n=== Project Structure ===" && ls -la projects/'
```

**批次檔快速啟動** (`tools/git-bash/quick_start.bat`):
```batch
@echo off
cd /d D:\claudeV
start "" "C:\Program Files\Git\bin\bash.exe"
```

### 3️⃣ Claude AI 整合設定

**Claude Code 配置** (`.claude/settings.local.json`):
```json
{
  "autoComplete": {
    "enabled": true,
    "languages": ["javascript", "python", "markdown", "json"]
  },
  "codeReview": {
    "enabled": true,
    "autoSuggest": true
  },
  "projectContext": {
    "include": ["projects/**", "tools/**", "*.md"],
    "exclude": ["node_modules/**", "*.log", "output/**"]
  }
}
```

## 🚀 開發工作流程

### 1️⃣ 日常開發流程

```bash
# 1. 啟動開發環境
cd /d/claudeV
git pull origin main           # 同步最新版本
code .                        # 開啟 VS Code

# 2. 選擇專案開發
cd projects/naturetour-website   # 選擇專案
git checkout -b feature/new-feature  # 建立功能分支

# 3. 開發階段 (使用 Claude AI)
# - 在 VS Code 中使用 Claude Code 擴展
# - 使用 Ctrl+Shift+P 呼叫 Claude 指令
# - 自動程式碼建議和重構

# 4. 測試與檢查
npm test                      # 執行測試 (如有)
npm run lint                  # 程式碼檢查

# 5. 提交變更
git add .
git commit -m "feat: implement new feature with Claude AI assistance

- Added new functionality
- Improved code structure
- Updated documentation

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# 6. 推送與合併
git push origin feature/new-feature
# 在 GitHub 建立 Pull Request
```

### 2️⃣ Claude AI 協作最佳實踐

**程式碼審查流程**:
```bash
# 使用 Claude 進行程式碼審查
# 在 VS Code 中：Ctrl+Shift+P > "Claude: Review Code"

# 或在 Git Bash 中請求審查
git diff --staged | claude-review  # 審查暫存變更
```

**文檔生成**:
```bash
# 自動生成 API 文檔
# VS Code: Ctrl+Shift+P > "Claude: Generate Documentation"

# 或手動請求文檔生成
claude-doc generate --project naturetour-website
```

### 3️⃣ 多專案管理

**專案狀態監控腳本** (`tools/git-bash/check_all_projects.sh`):
```bash
#!/bin/bash
echo "=== ClaudeV 專案狀態檢查 ==="
echo ""

for project in naturetour-website travel-content-generator wulitou-writer; do
    echo "📁 檢查 $project..."
    cd "/d/claudeV/projects/$project"

    echo "  Git 狀態:"
    git status --porcelain | head -5

    if [ -f "package.json" ]; then
        echo "  依賴狀態: $(npm outdated --depth=0 | wc -l) 個過期套件"
    fi

    echo ""
done

cd /d/claudeV
echo "✅ 檢查完成"
```

## 📚 重要檔案與配置說明

### 🔧 配置檔案詳解

**package.json 範例** (naturetour-website):
```json
{
  "name": "naturetour-website-upgrade",
  "version": "1.0.0",
  "description": "自然國際旅行社官網升級專案",
  "scripts": {
    "dev": "gulp watch",
    "build": "gulp build",
    "start": "gulp default",
    "deploy": "gulp deploy",
    "lint": "eslint src/**/*.js",
    "test": "jest"
  },
  "devDependencies": {
    "gulp": "^4.0.2",
    "gulp-sass": "^5.1.0",
    "browser-sync": "^2.27.10"
  }
}
```

**requirements.txt 範例** (travel-content-generator):
```txt
openai>=0.27.0
requests>=2.28.0
python-dotenv>=0.19.0
pandas>=1.4.0
beautifulsoup4>=4.11.0
```

### 📋 內容模板文件

**content_template_rules.md** - 完整的內容建立規範:
- 品牌聲音設定
- 目標客群分析
- 內容規範 (標題、內文、視覺)
- 季節性內容策略
- 品質控制流程

**travel_marketing_prompts.md** - AI Prompt 範例庫:
- 社群媒體貼文生成
- 官網內容創建
- 電子報內容規劃
- A/B 測試文案
- 多語言內容改寫

## 🧹 維護與最佳化

### 📦 定期維護腳本

**每週清理腳本** (`tools/maintenance/weekly_cleanup.sh`):
```bash
#!/bin/bash
echo "🧹 開始每週維護..."

# 1. Git 垃圾回收
cd /d/claudeV
git gc --prune=now
echo "✅ Git 垃圾回收完成"

# 2. 清理 node_modules (保留 package-lock.json)
find projects/ -name "node_modules" -type d -exec rm -rf {} + 2>/dev/null
echo "✅ Node.js 模組清理完成"

# 3. 清理 Python cache
find projects/ -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find projects/ -name "*.pyc" -delete 2>/dev/null
echo "✅ Python 快取清理完成"

# 4. 清理輸出檔案 (保留最近10個)
find projects/wulitou-writer/output -name "*.json" -type f | head -n -10 | xargs rm -f
echo "✅ 輸出檔案清理完成"

echo "🎉 維護完成！"
```

**依賴更新腳本** (`tools/maintenance/update_dependencies.sh`):
```bash
#!/bin/bash
echo "📦 開始更新依賴..."

# 更新 Node.js 專案
for project in naturetour-website wulitou-writer; do
    if [ -f "projects/$project/package.json" ]; then
        echo "🔄 更新 $project..."
        cd "projects/$project"
        npm update
        cd ../..
    fi
done

# 更新 Python 專案
if [ -f "projects/travel-content-generator/requirements.txt" ]; then
    echo "🔄 更新 travel-content-generator..."
    cd projects/travel-content-generator
    if [ -d "venv" ]; then
        source venv/bin/activate
        pip install --upgrade -r requirements.txt
        deactivate
    fi
    cd ../..
fi

echo "✅ 依賴更新完成！"
```

### 🔄 自動化同步

**自動備份腳本** (`tools/backup/auto_backup.sh`):
```bash
#!/bin/bash
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/d/claudeV_backups"

mkdir -p "$BACKUP_DIR"

# 建立完整備份 (排除 node_modules 等)
tar -czf "$BACKUP_DIR/claudeV_backup_$DATE.tar.gz" \
  --exclude="node_modules" \
  --exclude="__pycache__" \
  --exclude="venv" \
  --exclude=".git" \
  /d/claudeV

echo "✅ 備份完成: claudeV_backup_$DATE.tar.gz"

# 只保留最近 5 個備份
cd "$BACKUP_DIR"
ls -t claudeV_backup_*.tar.gz | tail -n +6 | xargs rm -f
echo "✅ 舊備份清理完成"
```

## 🎯 開發目標與路線圖

### 📅 短期目標 (1-3 個月)

**🌐 naturetour-website**:
- [ ] 完成首頁響應式設計
- [ ] 實作旅遊套裝頁面
- [ ] 整合線上預訂系統
- [ ] 完成 SEO 基礎設定
- [ ] 建立內容管理工作流程

**📝 travel-content-generator**:
- [ ] 增加 Instagram Stories 生成
- [ ] 實作多語言支援 (英文、日文)
- [ ] 建立 Web API 介面
- [ ] 增加圖片自動生成功能

**✍️ wulitou-writer**:
- [ ] 新增對話模式創作
- [ ] 實作文章分類系統
- [ ] 建立使用者介面 (Web UI)
- [ ] 增加創作歷史記錄

### 📅 長期目標 (3-12 個月)

**整體系統**:
- [ ] 建立 CI/CD 自動化流程
- [ ] 實作雲端部署
- [ ] 建立監控和分析系統
- [ ] 開發手機應用程式

**Claude AI 整合**:
- [ ] 自訂 Claude 工作流程
- [ ] 建立專案特定的 AI 助手
- [ ] 實作智能程式碼審查
- [ ] 開發自動化測試生成

## 🤝 團隊協作規範

### Git 工作流程

**分支策略**:
```
main                    # 主分支 (生產環境)
├── develop            # 開發分支 (測試環境)
├── feature/功能名稱    # 功能開發分支
├── bugfix/錯誤描述     # 錯誤修復分支
├── hotfix/緊急修復     # 緊急修復分支
└── docs/文檔更新       # 文檔更新分支
```

**提交訊息規範**:
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**類型說明**:
- `feat`: 新功能
- `fix`: 錯誤修復
- `docs`: 文檔更新
- `style`: 程式碼格式調整
- `refactor`: 程式碼重構
- `test`: 測試相關
- `chore`: 維護任務

**範例**:
```
feat(naturetour): add booking form validation

- Implement client-side form validation
- Add error message display
- Improve user experience

Closes #123

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
```

### 程式碼審查流程

1. **建立 Pull Request**
2. **自動檢查** (linting, tests)
3. **Claude AI 審查** (程式碼品質、安全性)
4. **人工審查** (商業邏輯、設計決策)
5. **合併到主分支**

## 📊 監控與分析

### 專案健康度檢查

**檢查腳本** (`tools/monitoring/health_check.sh`):
```bash
#!/bin/bash
echo "🔍 ClaudeV 專案健康度檢查"
echo "========================"

# 1. Git 倉庫狀態
echo "📊 Git 倉庫統計:"
echo "  - 總提交數: $(git rev-list --all --count)"
echo "  - 分支數量: $(git branch -r | wc -l)"
echo "  - 未追蹤檔案: $(git status --porcelain | grep "^??" | wc -l)"

# 2. 程式碼統計
echo -e "\n📈 程式碼統計:"
echo "  - JavaScript 檔案: $(find projects/ -name "*.js" | wc -l)"
echo "  - Python 檔案: $(find projects/ -name "*.py" | wc -l)"
echo "  - Markdown 檔案: $(find . -name "*.md" | wc -l)"

# 3. 專案大小
echo -e "\n💾 專案大小:"
du -sh projects/* | sort -hr

# 4. 最近活動
echo -e "\n🕒 最近提交:"
git log --oneline -5

echo -e "\n✅ 健康度檢查完成"
```

## 📞 支援與資源

### 🔗 重要連結
- **GitHub 倉庫**: https://github.com/nature501/firstP
- **Claude AI 文檔**: https://docs.claude.com/
- **VS Code Claude 擴展**: https://marketplace.visualstudio.com/items?itemName=claude-ai.claude-code

### 📧 聯繫資訊
- **專案維護**: nature.tour@msa.hinet.net
- **技術支援**: 透過 GitHub Issues
- **急件聯繫**: 請標註 [URGENT] 在 issue 標題

### 📚 學習資源
- **Claude AI 最佳實踐**: 見 `tools/vscode-config/CLAUDE.md`
- **Git 工作流程**: https://www.atlassian.com/git/tutorials/comparing-workflows
- **WordPress + Elementor**: https://elementor.com/academy/

---

**⚡ 此指南由 Claude AI 協助建立與維護**

> 這個開發環境專為最大化 Claude AI 協作效益而設計，提供完整的專案管理、開發工具整合和自動化工作流程。定期更新此文檔以反映最新的開發實踐和工具配置。

**最後更新**: 2024-09-28
**版本**: 1.0.0