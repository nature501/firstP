# 🔐 GitHub 認證設定指南

## 📋 前置作業檢查

✅ Git 使用者名稱已設定為: `nature501`
✅ Email 已設定為: `nature.tour@msa.hinet.net`
✅ 目前連接到倉庫: `https://github.com/nature501/firstP.git`

## 🔑 認證方式選擇

### 方式A: Personal Access Token (建議)

1. **建立 Personal Access Token**
   - 前往: https://github.com/settings/tokens
   - 點擊 "Generate new token (classic)"
   - 設定名稱: `ClaudeV-Development`
   - 選擇權限: `repo` (完整倉庫權限)
   - 點擊 "Generate token"
   - **重要**: 複製並妥善保存 token

2. **設定 Git 使用 Token**
   ```bash
   # 方法1: 在推送時輸入 (一次性)
   git push origin main
   # 使用者名稱: nature501
   # 密碼: [貼上您的 Personal Access Token]

   # 方法2: 設定 credential helper (自動記住)
   git config --global credential.helper store
   git push origin main  # 第一次會要求輸入，之後自動記住
   ```

### 方式B: SSH Key (進階)

1. **檢查是否已有 SSH Key**
   ```bash
   ls -la ~/.ssh
   ```

2. **產生新的 SSH Key** (如果沒有)
   ```bash
   ssh-keygen -t ed25519 -C "nature.tour@msa.hinet.net"
   # 按 Enter 使用預設檔案位置
   # 可設定密碼或留空
   ```

3. **添加 SSH Key 到 GitHub**
   ```bash
   # 複製公鑰內容
   cat ~/.ssh/id_ed25519.pub
   ```
   - 前往: https://github.com/settings/keys
   - 點擊 "New SSH key"
   - 貼上公鑰內容

4. **更改遠端 URL 為 SSH**
   ```bash
   cd /d/claudeV
   git remote set-url origin git@github.com:nature501/firstP.git
   ```

## 🧪 測試連線

```bash
# 測試 HTTPS 連線 (使用 Token)
git push origin main

# 測試 SSH 連線 (如果使用 SSH)
ssh -T git@github.com
```

## 🔄 日常開發流程

設定完成後，您的日常工作流程：

```bash
# 1. 啟動開發環境
source /d/claudeV/tools/git-bash/.bashrc_claudev

# 2. 開始開發
cdn  # 或其他專案目錄

# 3. 開發完成後提交
git add .
git commit -m "feat: your feature description"
git push origin main  # 現在應該不需要再輸入密碼
```

## ⚠️ 安全注意事項

1. **Personal Access Token**:
   - 不要在程式碼中硬編碼
   - 定期輪換 (建議6個月)
   - 只給予必要的權限

2. **SSH Key**:
   - 私鑰不要分享
   - 使用密碼保護私鑰
   - 定期更新

## 🆘 故障排除

### 推送失敗
```bash
# 檢查遠端設定
git remote -v

# 檢查認證狀態
git config --global credential.helper

# 重新設定認證
git config --global --unset credential.helper
```

### Token 過期
- 重新產生新的 Personal Access Token
- 下次推送時輸入新的 token

### SSH 連線問題
```bash
# 測試 SSH 連線
ssh -T git@github.com

# 檢查 SSH agent
ssh-add -l
```