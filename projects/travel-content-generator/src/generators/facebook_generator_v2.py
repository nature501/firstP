#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Facebook 貼文生成器 V2.0
支援批量生成、自訂填入、細緻風格控制

作者：自然國際旅行社內容團隊
版本：2.0
更新：2024-09-24
"""

import random
import json
from enum import Enum
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional


class PostType(Enum):
    """貼文類型枚舉"""
    EDUCATIONAL = "educational"      # 教育性
    INSPIRATIONAL = "inspirational"  # 靈感性
    SERVICE_SHOWCASE = "service"     # 服務展示
    INTERACTIVE = "interactive"      # 互動參與


class Season(Enum):
    """季節枚舉"""
    SPRING = "spring"   # 春季
    SUMMER = "summer"   # 夏季
    AUTUMN = "autumn"   # 秋季
    WINTER = "winter"   # 冬季


class CustomerType(Enum):
    """客群類型枚舉"""
    YOUNG_COUPLES = "young_couples"      # 年輕情侶/朋友
    FAMILIES = "families"                # 小家庭
    SENIORS = "seniors"                  # 資深旅客


class ToneStyle(Enum):
    """語調風格枚舉"""
    PROFESSIONAL = "professional"  # 專業正式
    WARM = "warm"                  # 溫暖親切
    ENERGETIC = "energetic"        # 活潑有趣
    BALANCED = "balanced"          # 平衡適中


@dataclass
class PostTemplate:
    """貼文模板結構 - 包含可填入的空格"""
    post_id: str                 # 貼文編號
    post_type: PostType         # 貼文類型
    title: str                  # 貼文標題
    template_text: str          # 模板文案（包含{主題}、{具體內容}等佔位符）
    theme_guidance: str         # 主題填入指引
    content_guidance: str       # 內容填入指引
    example_theme: str          # 主題範例
    example_content: str        # 內容範例
    hashtags: List[str]
    call_to_action: str
    best_post_time: str
    engagement_tips: List[str]
    style_notes: str           # 風格指引
    word_count_target: str     # 目標字數


@dataclass
class CompletedPost:
    """完成的貼文內容結構"""
    post_id: str
    post_type: PostType
    filled_text: str           # 已填入主題和內容的完整文案
    hashtags: List[str]
    call_to_action: str
    best_post_time: str
    engagement_tips: List[str]
    actual_word_count: int


@dataclass
class BatchPostRequest:
    """批量生成請求結構"""
    destination: str
    season: Season
    customer_type: CustomerType
    post_count: int = 5
    post_types: List[PostType] = None
    tone_style: ToneStyle = ToneStyle.BALANCED
    specific_themes: List[str] = None
    include_templates: bool = True    # 是否包含模板（供填入）
    include_examples: bool = True     # 是否包含範例（完整貼文）


class FacebookPostGeneratorV2:
    """Facebook 貼文生成器 V2.0"""

    def __init__(self):
        """初始化生成器"""
        self.brand_values = {
            "core": ["專業", "熱情", "貼心", "創新", "誠信"],
            "tone": "友善而專業",
            "emotion": "溫暖、充滿熱情",
            "avoid": ["廉價", "匆忙", "標準化", "冷漠", "商業化"]
        }

        # 語調風格設定
        self.tone_styles = {
            ToneStyle.PROFESSIONAL: {
                "prefix": "專業建議",
                "emotion_level": "穩重",
                "vocabulary": ["專業", "建議", "分析", "經驗", "品質"],
                "sentence_style": "較長，詳細說明"
            },
            ToneStyle.WARM: {
                "prefix": "親切分享",
                "emotion_level": "溫暖",
                "vocabulary": ["溫暖", "分享", "感受", "體驗", "美好"],
                "sentence_style": "中等長度，感性描述"
            },
            ToneStyle.ENERGETIC: {
                "prefix": "活力推薦",
                "emotion_level": "興奮",
                "vocabulary": ["精彩", "驚喜", "活力", "探索", "冒險"],
                "sentence_style": "較短，節奏明快"
            },
            ToneStyle.BALANCED: {
                "prefix": "用心推薦",
                "emotion_level": "平和",
                "vocabulary": ["推薦", "體驗", "探索", "享受", "發現"],
                "sentence_style": "適中長度，平衡理性與感性"
            }
        }

        # 客群特定設定
        self.customer_styles = {
            CustomerType.YOUNG_COUPLES: {
                "style": "輕鬆、時尚、充滿活力",
                "keywords": ["浪漫", "打卡", "體驗", "分享", "獨特"],
                "pain_points": ["預算考量", "想要特殊體驗", "愛分享紀錄"],
                "communication": "親切活潑，使用年輕化用詞"
            },
            CustomerType.FAMILIES: {
                "style": "可靠、溫暖、專業",
                "keywords": ["安全", "親子", "教育", "便利", "溫馨"],
                "pain_points": ["安全考量", "教育意義", "服務品質"],
                "communication": "溫暖可靠，強調安全與品質"
            },
            CustomerType.SENIORS: {
                "style": "尊重、專業、詳細",
                "keywords": ["文化", "深度", "舒適", "品質", "專業"],
                "pain_points": ["文化深度", "舒適度", "專業服務"],
                "communication": "尊重專業，提供詳細資訊"
            }
        }

        # 季節主題庫
        self.seasonal_themes = {
            Season.SPRING: {
                "themes": ["賞花季節", "櫻花", "薰衣草", "溫和氣候", "畢業旅行", "春假親子遊"],
                "emotions": ["新生", "浪漫", "溫暖", "希望"],
                "activities": ["賞花", "戶外踏青", "文化體驗", "輕度健行"],
                "keywords": ["盛開", "綻放", "清香", "微風", "新綠"]
            },
            Season.SUMMER: {
                "themes": ["海島度假", "避暑勝地", "暑假家庭旅遊", "水上活動"],
                "emotions": ["活力", "清爽", "歡樂", "冒險"],
                "activities": ["海邊戲水", "潛水", "衝浪", "夏日祭典"],
                "keywords": ["陽光", "海風", "清涼", "活力", "歡樂"]
            },
            Season.AUTUMN: {
                "themes": ["賞楓行程", "溫泉養生", "美食之旅", "文化體驗"],
                "emotions": ["詩意", "溫馨", "豐收", "沉靜"],
                "activities": ["賞楓", "泡溫泉", "品嚐美食", "文化導覽"],
                "keywords": ["楓紅", "金黃", "溫泉", "美食", "豐收"]
            },
            Season.WINTER: {
                "themes": ["溫暖南方避寒", "雪景滑雪體驗", "年節慶典", "尾牙春酒旅遊"],
                "emotions": ["溫暖", "歡聚", "慶祝", "感恩"],
                "activities": ["滑雪", "溫泉", "聖誕市集", "新年慶典"],
                "keywords": ["溫暖", "雪花", "慶祝", "團聚", "感恩"]
            }
        }

    def generate_batch_posts(self, request: BatchPostRequest) -> Dict:
        """
        批量生成Facebook貼文模板和範例

        Args:
            request: 批量生成請求

        Returns:
            包含模板和範例的完整結果
        """

        # 決定貼文類型分配
        if request.post_types:
            post_types = request.post_types
        else:
            # 預設分配：教育性40%、靈感性30%、服務展示20%、互動10%
            post_types = (
                [PostType.EDUCATIONAL] * max(1, int(request.post_count * 0.4)) +
                [PostType.INSPIRATIONAL] * max(1, int(request.post_count * 0.3)) +
                [PostType.SERVICE_SHOWCASE] * max(1, int(request.post_count * 0.2)) +
                [PostType.INTERACTIVE] * max(1, int(request.post_count * 0.1))
            )

        # 調整到確切數量
        if len(post_types) > request.post_count:
            post_types = post_types[:request.post_count]
        elif len(post_types) < request.post_count:
            post_types.extend([PostType.EDUCATIONAL] * (request.post_count - len(post_types)))

        templates = []
        examples = []

        for i, post_type in enumerate(post_types, 1):
            # 生成模板
            if request.include_templates:
                template = self._generate_post_template(
                    post_id=f"POST_{i:02d}",
                    destination=request.destination,
                    post_type=post_type,
                    season=request.season,
                    customer_type=request.customer_type,
                    tone_style=request.tone_style,
                    specific_theme=request.specific_themes[i-1] if request.specific_themes and i-1 < len(request.specific_themes) else None
                )
                templates.append(template)

            # 生成範例
            if request.include_examples:
                example = self._generate_example_post(
                    post_id=f"EXAMPLE_{i:02d}",
                    destination=request.destination,
                    post_type=post_type,
                    season=request.season,
                    customer_type=request.customer_type,
                    tone_style=request.tone_style
                )
                examples.append(example)

        return {
            "request_summary": {
                "destination": request.destination,
                "season": request.season.value,
                "customer_type": request.customer_type.value,
                "tone_style": request.tone_style.value,
                "post_count": request.post_count,
                "generated_at": "2024-09-24"
            },
            "templates": [asdict(template) for template in templates] if request.include_templates else [],
            "examples": [asdict(example) for example in examples] if request.include_examples else [],
            "usage_instructions": {
                "template_usage": "在template_text中找到{主題}和{具體內容}，根據guidance填入您的具體內容",
                "word_count_guideline": "每篇貼文建議控制在150-200字之間",
                "hashtag_usage": "可以根據實際內容調整hashtag，但建議保留品牌相關標籤",
                "posting_schedule": "參考best_post_time安排發布時間以獲得最佳效果"
            }
        }

    def _generate_post_template(self, post_id: str, destination: str, post_type: PostType,
                               season: Season, customer_type: CustomerType,
                               tone_style: ToneStyle, specific_theme: Optional[str] = None) -> PostTemplate:
        """生成貼文模板"""

        seasonal_info = self.seasonal_themes[season]
        customer_info = self.customer_styles[customer_type]
        tone_info = self.tone_styles[tone_style]

        theme = specific_theme or random.choice(seasonal_info["themes"])

        # 根據類型生成不同的模板
        if post_type == PostType.EDUCATIONAL:
            return self._create_educational_template(
                post_id, destination, theme, season, customer_type, tone_style
            )
        elif post_type == PostType.INSPIRATIONAL:
            return self._create_inspirational_template(
                post_id, destination, theme, season, customer_type, tone_style
            )
        elif post_type == PostType.SERVICE_SHOWCASE:
            return self._create_service_template(
                post_id, destination, theme, season, customer_type, tone_style
            )
        else:  # INTERACTIVE
            return self._create_interactive_template(
                post_id, destination, theme, season, customer_type, tone_style
            )

    def _create_educational_template(self, post_id: str, destination: str, theme: str,
                                   season: Season, customer_type: CustomerType,
                                   tone_style: ToneStyle) -> PostTemplate:
        """建立教育性貼文模板"""

        customer_info = self.customer_styles[customer_type]

        if customer_type == CustomerType.YOUNG_COUPLES:
            opener = f"想和另一半在{destination}體驗{{主題}}嗎？✨"
            template_text = f"""{opener}

💡 {{具體內容}}

🔸 25年專業經驗分享：我們的在地夥伴會即時更新最佳體驗地點和時機，確保您的旅程完美無遺憾！

想了解更多專業建議嗎？歡迎私訊我們！"""

            theme_guidance = f"填入具體的{theme}相關主題，如：櫻花季最佳賞花時間、當地特色文化體驗等"
            content_guidance = "填入3-4個實用貼士，每個貼士30-40字，包含時間、地點、方式等具體建議"
            example_theme = "櫻花季最佳賞花秘境"
            example_content = "清晨6點哲學之道人潮最少 📍 祇園夜櫻別有風情 🍽️ 櫻花季限定和菓子必嚐 🚌 購買市巴士一日券最划算"

        elif customer_type == CustomerType.FAMILIES:
            opener = f"帶著孩子到{destination}探索{{主題}}，寓教於樂的最佳選擇！👨‍👩‍👧‍👦"
            template_text = f"""{opener}

📚 {{具體內容}}

🔸 25年專業經驗分享：我們特別注重親子旅遊的安全性和教育意義，每個行程都經過仔細評估！

想為家人規劃完美行程嗎？讓我們協助您！"""

            theme_guidance = f"填入適合親子的{theme}主題，強調安全性和教育價值"
            content_guidance = "填入4-5個親子友善的實用建議，包含安全注意事項、教育意義、便利設施等"
            example_theme = "親子友善的文化體驗"
            example_content = "🛡️ 選擇有安全護欄的觀景台 🎓 參加互動式文化體驗課程 🏨 預訂有親子設施的飯店 🍎 準備孩子熟悉的食物 📱 下載緊急聯絡APP"

        else:  # SENIORS
            opener = f"深度探索{destination}的{{主題}}，讓旅程充滿文化底蘊 🎌"
            template_text = f"""{opener}

🏛️ {{具體內容}}

🔸 25年專業經驗分享：我們與當地資深導遊合作，提供深度的文化解說和舒適的行程安排！

想要更深入的文化體驗嗎？歡迎與我們討論！"""

            theme_guidance = f"填入具有文化深度的{theme}主題，強調歷史背景和文化意義"
            content_guidance = "填入4-5個深度體驗建議，包含歷史背景、文化意義、專業導覽、舒適安排等"
            example_theme = "傳統工藝文化深度體驗"
            example_content = "🏛️ 參訪百年老店了解工藝傳承 👥 安排專業工藝師親自解說 🍵 體驗傳統茶道文化 🚌 提供舒適接送服務 📚 準備詳細文化背景資料"

        return PostTemplate(
            post_id=post_id,
            post_type=PostType.EDUCATIONAL,
            title=f"{destination}{theme} - 教育性貼文",
            template_text=template_text,
            theme_guidance=theme_guidance,
            content_guidance=content_guidance,
            example_theme=example_theme,
            example_content=example_content,
            hashtags=self._generate_hashtags(destination, season, customer_type, ["教育", "攻略", "貼士"]),
            call_to_action="想了解更多專業建議嗎？歡迎私訊我們，讓25年經驗為您規劃最完美的行程！",
            best_post_time="週二至週四 10:00-16:00",
            engagement_tips=["分享更多實用小貼士", "邀請粉絲分享經驗", "提供免費諮詢"],
            style_notes=f"語調：{customer_info['communication']}，重點提供實用資訊建立專業形象",
            word_count_target="150-200字"
        )

    def _create_inspirational_template(self, post_id: str, destination: str, theme: str,
                                     season: Season, customer_type: CustomerType,
                                     tone_style: ToneStyle) -> PostTemplate:
        """建立靈感性貼文模板"""

        customer_info = self.customer_styles[customer_type]

        if customer_type == CustomerType.YOUNG_COUPLES:
            template_text = f"""💕 還在煩惱要和心愛的人去哪裡製造美好回憶嗎？

想像一下，{{具體內容}}

自然國際旅行社25年來，就是希望為每位旅客創造這樣的{{主題}}時刻。我們相信，旅行不只是移動，更是心靈的觸動與成長 🌱

不要讓夢想只是夢想，讓我們一起把它變成美好的現實！"""

            theme_guidance = "填入情感化的主題詞彙，如：浪漫、感動、驚喜、美好等"
            content_guidance = "描繪一個浪漫場景，讓讀者能夠想像和感受，約50-70字"
            example_theme = "浪漫"
            example_content = "您和另一半漫步在京都的櫻花樹下，粉色花瓣輕柔飄落，陽光透過花間灑在臉上，這一刻的幸福感會成為你們最珍貴的回憶 ✨"

        elif customer_type == CustomerType.FAMILIES:
            template_text = f"""👨‍👩‍👧‍👦 想給家人一個難忘的{destination}假期嗎？

{{具體內容}}

自然國際旅行社25年來，見證無數家庭的美好時光。我們深信，最珍貴的禮物就是和家人共度的每一個瞬間 💝

準備好為家人創造美好回憶了嗎？讓我們一起規劃專屬的家庭時光！"""

            theme_guidance = "填入家庭情感相關主題，如：溫馨、成長、陪伴、快樂等"
            content_guidance = "描述家庭旅遊的溫馨場景，突出親子互動和家庭和諧，約50-70字"
            example_theme = "溫馨"
            example_content = "看著孩子們在沖繩海邊開心地堆沙堡，爸媽在一旁輕鬆聊天，夕陽西下時全家人手牽手漫步海邊，那純真的笑容就是給父母最好的禮物 🎁"

        else:  # SENIORS
            template_text = f"""🌟 人生就該有幾次深度的{{主題}}之旅...

在{destination}，{{具體內容}}

自然國際旅行社25年的經驗告訴我們，最美的旅程往往在於深度的體驗與內心的觸動 🍃

準備好開始這趟心靈豐富之旅了嗎？"""

            theme_guidance = "填入深度體驗相關主題，如：文化、智慧、沉澱、感悟等"
            content_guidance = "描述深度文化體驗的場景，強調心靈層面的收穫，約50-70字"
            example_theme = "文化"
            example_content = "每一個古老廟宇都訴說著歷史的智慧，每一次與當地人的交流都是心靈的觸動，每一個轉彎都是新的發現，讓歲月沉澱出最美的人生風景"

        return PostTemplate(
            post_id=post_id,
            post_type=PostType.INSPIRATIONAL,
            title=f"{destination}{theme} - 靈感性貼文",
            template_text=template_text,
            theme_guidance=theme_guidance,
            content_guidance=content_guidance,
            example_theme=example_theme,
            example_content=example_content,
            hashtags=self._generate_hashtags(destination, season, customer_type, ["夢想", "靈感", "美好"]),
            call_to_action="準備好開始您的夢想之旅了嗎？讓我們聊聊您心中的旅遊藍圖吧！💌",
            best_post_time="週五至週日 18:00-21:00",
            engagement_tips=["邀請粉絲分享旅遊夢想", "詢問最想去的目的地", "分享客戶美好故事"],
            style_notes=f"語調：{customer_info['communication']}，重點觸動情感激發旅遊夢想",
            word_count_target="150-200字"
        )

    def _create_service_template(self, post_id: str, destination: str, theme: str,
                               season: Season, customer_type: CustomerType,
                               tone_style: ToneStyle) -> PostTemplate:
        """建立服務展示貼文模板"""

        customer_info = self.customer_styles[customer_type]

        if customer_type == CustomerType.YOUNG_COUPLES:
            opener = f"計劃到{destination}的浪漫之旅嗎？讓我們的專業服務為您打造完美回憶！💕"
        elif customer_type == CustomerType.FAMILIES:
            opener = f"帶著全家到{destination}旅遊，安全和品質是您最在意的嗎？我們懂您的需求！👨‍👩‍👧‍👦"
        else:
            opener = f"想要深度體驗{destination}的文化精髓嗎？25年的專業經驗為您開啟不同層次的旅遊體驗！🎌"

        template_text = f"""{opener}

🎯 {{具體內容}}

💭 客戶回饋：「自然國際真的很用心！每個細節都幫我們想到了，讓我們玩得很安心又開心！」

🌟 這就是我們與一般旅行社的不同：不只是賣行程，更是您的旅遊夥伴！"""

        return PostTemplate(
            post_id=post_id,
            post_type=PostType.SERVICE_SHOWCASE,
            title=f"{destination}專業服務 - 服務展示貼文",
            template_text=template_text,
            theme_guidance="選擇最符合該客群需求的服務特色作為主題",
            content_guidance="列出2-3個核心服務特色，每個特色30-40字，突出差異化優勢",
            example_theme="客製化專業服務",
            example_content="完全客製化行程規劃：根據您的喜好、預算、時間量身打造 👥 專業在地導覽團隊：深度了解當地文化 📞 24小時緊急聯絡服務：無論何時何地都是您的後盾",
            hashtags=self._generate_hashtags(destination, season, customer_type, ["專業服務", "客製化", "品質保證"]),
            call_to_action="想體驗我們的專業服務嗎？立即私訊或來電諮詢，免費為您規劃專屬行程！",
            best_post_time="週一、週三 09:00-11:00",
            engagement_tips=["邀請客戶分享服務體驗", "提供免費諮詢優惠", "展示服務細節"],
            style_notes=f"語調：{customer_info['communication']}，重點展現專業服務和差異化優勢",
            word_count_target="150-200字"
        )

    def _create_interactive_template(self, post_id: str, destination: str, theme: str,
                                   season: Season, customer_type: CustomerType,
                                   tone_style: ToneStyle) -> PostTemplate:
        """建立互動參與貼文模板"""

        customer_info = self.customer_styles[customer_type]

        template_text = f"""{{主題}}

{{具體內容}}

💡 小貼士：作為{destination}旅遊專家，我們發現最佳體驗往往藏在細節中。25年來累積的在地資源，讓我們能為您安排最道地的體驗！

快來留言跟我們互動吧！我們會親自回覆每一位朋友 😊"""

        return PostTemplate(
            post_id=post_id,
            post_type=PostType.INTERACTIVE,
            title=f"{destination}互動討論 - 互動參與貼文",
            template_text=template_text,
            theme_guidance="設計一個能引起討論的問題或話題，搭配表情符號增加親切感",
            content_guidance="列出選項或引導討論的內容，鼓勵粉絲參與互動",
            example_theme="🤔 正在規劃京都之旅嗎？關於櫻花季，您最想知道什麼？",
            example_content="A. 最佳賞花時間？ B. 必去景點推薦？ C. 當地美食介紹？ D. 交通方式建議？ E. 住宿推薦？",
            hashtags=self._generate_hashtags(destination, season, customer_type, ["互動", "分享", "交流"]),
            call_to_action="快來留言分享您的想法，讓我們一起規劃最棒的旅程！",
            best_post_time="週五至週日 18:00-21:00",
            engagement_tips=["及時回覆每個留言", "詢問深入問題延續討論", "分享專業建議"],
            style_notes=f"語調：{customer_info['communication']}，重點促進互動和參與",
            word_count_target="120-180字"
        )

    def _generate_example_post(self, post_id: str, destination: str, post_type: PostType,
                             season: Season, customer_type: CustomerType,
                             tone_style: ToneStyle) -> CompletedPost:
        """生成完整範例貼文"""

        # 先生成模板
        template = self._generate_post_template(
            post_id, destination, post_type, season, customer_type, tone_style
        )

        # 用範例內容填入模板
        filled_text = template.template_text.replace("{主題}", template.example_theme)
        filled_text = filled_text.replace("{具體內容}", template.example_content)

        return CompletedPost(
            post_id=post_id,
            post_type=post_type,
            filled_text=filled_text,
            hashtags=template.hashtags,
            call_to_action=template.call_to_action,
            best_post_time=template.best_post_time,
            engagement_tips=template.engagement_tips,
            actual_word_count=len(filled_text)
        )

    def _generate_hashtags(self, destination: str, season: Season,
                          customer_type: CustomerType, theme_tags: List[str]) -> List[str]:
        """生成相關hashtag"""

        hashtag_pool = {
            "brand": ["#自然國際旅行社", "#25年專業經驗", "#客製化旅遊", "#專業旅遊規劃"],
            "general": ["#旅遊", "#旅行", "#度假", "#探索世界", "#美好時光", "#專業服務"],
            "emotional": ["#夢想成真", "#美好回憶", "#深度體驗", "#文化探索", "#在地體驗"],
            "service": ["#客製化行程", "#專業導遊", "#24小時服務", "#安心旅遊", "#品質保證"]
        }

        hashtags = []

        # 品牌hashtag（必選）
        hashtags.extend(random.sample(hashtag_pool["brand"], 2))

        # 一般旅遊hashtag
        hashtags.extend(random.sample(hashtag_pool["general"], 2))

        # 情感hashtag
        hashtags.append(random.choice(hashtag_pool["emotional"]))

        # 服務hashtag
        hashtags.append(random.choice(hashtag_pool["service"]))

        # 目的地相關
        hashtags.append(f"#{destination}")
        hashtags.append(f"#{destination}旅遊")

        # 季節相關
        season_tags = {
            Season.SPRING: ["#春遊", "#賞花"],
            Season.SUMMER: ["#夏日度假", "#海島旅遊"],
            Season.AUTUMN: ["#秋遊", "#賞楓"],
            Season.WINTER: ["#冬季旅遊", "#溫暖之旅"]
        }
        hashtags.extend(season_tags.get(season, ["#旅遊"]))

        # 客群相關
        customer_tags = {
            CustomerType.YOUNG_COUPLES: ["#情侶旅遊", "#浪漫之旅"],
            CustomerType.FAMILIES: ["#親子旅遊", "#家庭旅遊"],
            CustomerType.SENIORS: ["#深度旅遊", "#文化之旅"]
        }
        hashtags.extend(customer_tags.get(customer_type, ["#客製化旅遊"]))

        # 主題相關
        for theme in theme_tags:
            hashtags.append(f"#{theme}")

        # 移除重複並限制數量
        unique_hashtags = list(dict.fromkeys(hashtags))
        return unique_hashtags[:12]

    def export_to_json(self, result: Dict, filename: str = None) -> str:
        """匯出結果為JSON檔案"""
        if not filename:
            filename = f"facebook_posts_{result['request_summary']['destination']}_batch.json"

        filepath = f"/d/claudeV/git_bash/travel_content/output/{filename}"

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        return filepath


def main():
    """主函數 - 使用範例"""

    generator = FacebookPostGeneratorV2()

    print("🌟 Facebook 貼文生成器 V2.0 - 批量生成範例 🌟\n")

    # 建立批量請求
    request = BatchPostRequest(
        destination="京都",
        season=Season.SPRING,
        customer_type=CustomerType.YOUNG_COUPLES,
        post_count=3,
        tone_style=ToneStyle.WARM,
        include_templates=True,
        include_examples=True
    )

    # 生成批量貼文
    result = generator.generate_batch_posts(request)

    print("=" * 60)
    print("【生成摘要】")
    print(f"目的地：{result['request_summary']['destination']}")
    print(f"季節：{result['request_summary']['season']}")
    print(f"客群：{result['request_summary']['customer_type']}")
    print(f"語調風格：{result['request_summary']['tone_style']}")
    print(f"生成數量：{result['request_summary']['post_count']}")

    print("\n" + "=" * 60)
    print("【模板範例】（可填入您的具體內容）")

    for i, template in enumerate(result['templates'][:1], 1):  # 只顯示第一個模板
        print(f"\n--- 模板 {i} ---")
        print(f"類型：{template['post_type']}")
        print(f"標題：{template['title']}")
        print(f"\n📝 模板文案：")
        print(template['template_text'])
        print(f"\n💡 主題填入指引：")
        print(template['theme_guidance'])
        print(f"\n📋 內容填入指引：")
        print(template['content_guidance'])
        print(f"\n🌰 主題範例：{template['example_theme']}")
        print(f"\n📄 內容範例：")
        print(template['example_content'])

    print("\n" + "=" * 60)
    print("【完整範例】（參考用）")

    for i, example in enumerate(result['examples'][:1], 1):  # 只顯示第一個範例
        print(f"\n--- 範例 {i} ---")
        print(f"類型：{example['post_type']}")
        print(f"字數：{example['actual_word_count']}")
        print(f"\n📝 完整文案：")
        print(example['filled_text'])
        print(f"\n🏷️ Hashtags：")
        print(" ".join(example['hashtags']))

    print("\n" + "=" * 60)
    print("✅ 批量生成完成！")
    print("💡 使用說明：")
    print("1. 選擇模板，在{主題}和{具體內容}的位置填入您的內容")
    print("2. 參考guidance進行填寫")
    print("3. 可以根據實際情況調整hashtag")
    print("4. 建議在指定的最佳時間發布")


if __name__ == "__main__":
    main()