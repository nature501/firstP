# Facebook 貼文生成器 V2.0 使用指南

## 🌟 功能概述

這是專為**自然國際旅行社**設計的Facebook貼文生成器，完全符合您25年專業旅行社的品牌風格。**V2.0版本**新增了批量生成和自訂填入功能，讓您更靈活地創作內容。

## ✨ V2.0 新功能特色

### 🔥 主要改進
- **批量生成**：一次生成多篇貼文模板（預設5篇）
- **留空填入**：每個模板都有 `{主題}` 和 `{具體內容}` 佔位符供您填入
- **細緻風格控制**：4種語調風格可選（專業/溫暖/活潑/平衡）
- **完整指引**：每個模板都附有詳細的填入說明和範例
- **智能分配**：自動按比例分配貼文類型（教育40%、靈感30%、服務20%、互動10%）

### 📋 支援的內容類型
1. **教育性貼文（40%）**：提供實用旅遊資訊，建立專業形象
2. **靈感性貼文（30%）**：觸動情感，激發旅遊夢想
3. **服務展示貼文（20%）**：展現25年專業服務優勢
4. **互動參與貼文（10%）**：促進粉絲互動和參與

## 🚀 快速開始

### 基本使用流程

```python
from facebook_generator_v2 import (
    FacebookPostGeneratorV2,
    BatchPostRequest,
    Season,
    CustomerType,
    ToneStyle
)

# 1. 建立生成器
generator = FacebookPostGeneratorV2()

# 2. 設定生成請求
request = BatchPostRequest(
    destination="京都",                    # 目的地
    season=Season.SPRING,                  # 季節
    customer_type=CustomerType.YOUNG_COUPLES,  # 客群類型
    post_count=5,                          # 生成數量
    tone_style=ToneStyle.WARM,             # 語調風格
    include_templates=True,                # 包含可填入模板
    include_examples=True                  # 包含完整範例
)

# 3. 執行生成
result = generator.generate_batch_posts(request)

# 4. 取得結果
templates = result['templates']  # 可填入的模板
examples = result['examples']    # 完整範例
```

## 🎯 客群類型與風格

### 三大主要客群
1. **年輕情侶/朋友 (YOUNG_COUPLES)**
   - 年齡：25-35歲
   - 特色：重視體驗、愛分享、預算有限
   - 溝通風格：輕鬆時尚、充滿活力
   - 關鍵詞：浪漫、打卡、體驗、分享、獨特

2. **小家庭 (FAMILIES)**
   - 年齡：30-45歲父母
   - 特色：安全至上、教育意義、便利性
   - 溝通風格：可靠溫暖、專業詳細
   - 關鍵詞：安全、親子、教育、便利、溫馨

3. **資深旅客 (SENIORS)**
   - 年齡：50歲以上
   - 特色：文化深度、舒適品質、專業服務
   - 溝通風格：尊重專業、詳細解說
   - 關鍵詞：文化、深度、舒適、品質、專業

### 四種語調風格
- **PROFESSIONAL**：專業正式，強調經驗和品質
- **WARM**：溫暖親切，重視情感連結
- **ENERGETIC**：活潑有趣，充滿活力和探索精神
- **BALANCED**：平衡適中，理性與感性並重

## 📝 模板填入指南

### 模板結構說明
每個模板包含：
- `{主題}`：需要您填入的具體主題
- `{具體內容}`：需要您填入的詳細內容
- 完整的填入指引和範例

### 填入範例

**原始模板：**
```
想和另一半在京都體驗{主題}嗎？✨

💡 {具體內容}

🔸 25年專業經驗分享：我們的在地夥伴會即時更新最佳體驗地點和時機，確保您的旅程完美無遺憾！
```

**填入後效果：**
```
想和另一半在京都體驗櫻花季最佳賞花秘境嗎？✨

💡 清晨6點哲學之道人潮最少 📍 祇園夜櫻別有風情 🍽️ 櫻花季限定和菓子必嚐 🚌 購買市巴士一日券最划算

🔸 25年專業經驗分享：我們的在地夥伴會即時更新最佳體驗地點和時機，確保您的旅程完美無遺憾！
```

## 🗓️ 發布策略建議

### 最佳發布時間
- **教育性內容**：週二-週四 10:00-16:00
- **靈感性內容**：週五-週日 18:00-21:00
- **服務展示**：週一、週三 09:00-11:00
- **互動參與**：週五-週日 18:00-21:00

### 內容分配比例
- 教育性內容：40%（每週2-3次）
- 靈感性內容：30%（每週2次）
- 服務展示：20%（每週1-2次）
- 互動參與：10%（每週1次）

## 📁 檔案結構

```
src/generators/
├── facebook_generator_v2.py      # 主要生成器
├── demo_usage.py                 # 使用示範
├── test_facebook_generator.py    # 測試檔案
└── README.md                     # 詳細說明
```

## 🛠️ 進階使用

### 自訂主題列表
```python
request = BatchPostRequest(
    destination="沖繩",
    season=Season.SUMMER,
    customer_type=CustomerType.FAMILIES,
    post_count=5,
    specific_themes=[
        "親子友善海灘",
        "海洋生物觀察",
        "沖繩傳統文化",
        "安全戲水須知",
        "當地美食探索"
    ]
)
```

### 指定貼文類型
```python
request = BatchPostRequest(
    destination="台東",
    season=Season.AUTUMN,
    customer_type=CustomerType.SENIORS,
    post_count=3,
    post_types=[
        PostType.EDUCATIONAL,
        PostType.INSPIRATIONAL,
        PostType.SERVICE_SHOWCASE
    ]
)
```

### 匯出功能
```python
# 生成結果
result = generator.generate_batch_posts(request)

# 匯出為JSON檔案
filepath = generator.export_to_json(result, "京都春季貼文.json")
```

## 📊 輸出結果結構

### 模板結果 (templates)
每個模板包含：
- `post_id`：貼文編號
- `template_text`：含佔位符的模板文案
- `theme_guidance`：主題填入指引
- `content_guidance`：內容填入指引
- `example_theme`：主題範例
- `example_content`：內容範例
- `hashtags`：建議hashtag
- `best_post_time`：最佳發布時間
- `engagement_tips`：互動建議

### 完整範例 (examples)
- `filled_text`：已填入內容的完整貼文
- `actual_word_count`：實際字數統計
- 其他貼文相關資訊

## 🎨 品牌一致性保證

所有生成內容嚴格遵循自然國際旅行社品牌風格：

### 核心價值觀
- **專業**：25年經驗累積
- **熱情**：對旅遊的真正熱愛
- **貼心**：細膩關注客戶需求
- **創新**：不斷尋找新體驗
- **誠信**：透明誠實的服務

### 溝通風格
- 語調：友善而專業，溫暖充滿熱情
- 表達：簡潔明瞭，積極正面
- 個性：專業但不呆板，親切但不隨便
- 避免：廉價、匆忙、標準化、冷漠、商業化

## 🔧 故障排除

### 常見問題
1. **模板中的佔位符沒有被替換**
   - 確認使用正確的格式：`{主題}` 和 `{具體內容}`
   - 檢查是否有多餘的空格

2. **生成的內容字數過長**
   - 控制填入內容的長度
   - 參考 `word_count_target` 指引

3. **風格不符合預期**
   - 調整 `tone_style` 參數
   - 查看 `style_notes` 中的風格說明

## 📞 技術支援

如有任何問題或建議，請聯繫開發團隊。

---

**版本**：2.0
**更新日期**：2024-09-24
**適用品牌**：自然國際旅行社
**核心特色**：批量生成 + 自訂填入 + 細緻風格控制