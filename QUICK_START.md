# ⚡ ClaudeV 快速開始指南

## 🚀 立即啟動

### 方法 1: VS Code 工作區
```bash
# 直接開啟完整工作區
code D:/claudeV/tools/vscode-config/workspace.code-workspace
```

### 方法 2: Git Bash 快速啟動
```bash
# 執行啟動腳本
D:/claudeV/tools/git-bash/start_claudev.bat
```

### 方法 3: 手動啟動
```bash
# Git Bash 中載入配置
source /d/claudeV/tools/git-bash/.bashrc_claudev
```

## 📂 快速導航

載入 ClaudeV 配置後，您可使用以下指令：

```bash
cdcv    # 回到 ClaudeV 根目錄
cdn     # 進入 naturetour-website 專案
cdtc    # 進入 travel-content-generator 專案
cdww    # 進入 wulitou-writer 專案
```

## 🛠️ 開發指令

```bash
# 專案狀態檢查
pstatus

# 啟動開發環境
startdev     # 開啟 VS Code 工作區
startweb     # 啟動網站開發模式
startpython  # 啟動 Python 虛擬環境

# 維護指令
pclean       # 清理專案檔案
pbackup      # 建立專案備份
```

## 🤖 Claude AI 使用

```bash
# 查看 Claude 使用說明
claude-help

# VS Code 中使用 Claude
# Ctrl+Shift+P > "Claude: ..."
```

## 📖 詳細文檔

完整開發指南請參閱: [DEVELOPMENT_GUIDE.md](./DEVELOPMENT_GUIDE.md)