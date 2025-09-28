#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Facebook 貼文生成器
針對25年專業旅行社品牌風格設計

作者：自然國際旅行社內容團隊
版本：1.0
更新：2024-09-24
"""

import random
from enum import Enum
from dataclasses import dataclass
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


@dataclass
class PostContent:
    """貼文內容結構"""
    main_text: str
    hashtags: List[str]
    call_to_action: str
    best_post_time: str
    engagement_tips: List[str]


class FacebookPostGenerator:
    """Facebook 貼文生成器主類"""

    def __init__(self):
        """初始化生成器"""
        self.brand_values = {
            "core": ["專業", "熱情", "貼心", "創新", "誠信"],
            "tone": "友善而專業",
            "emotion": "溫暖、充滿熱情",
            "avoid": ["廉價", "匆忙", "標準化", "冷漠", "商業化"]
        }

        # 客群特定的溝通風格
        self.customer_styles = {
            CustomerType.YOUNG_COUPLES: {
                "style": "輕鬆、時尚、充滿活力",
                "keywords": ["浪漫", "打卡", "體驗", "分享", "獨特"],
                "pain_points": ["預算有限", "想要特殊體驗", "愛分享"]
            },
            CustomerType.FAMILIES: {
                "style": "可靠、溫暖、專業",
                "keywords": ["安全", "親子", "教育", "便利", "溫馨"],
                "pain_points": ["安全考量", "教育意義", "服務品質"]
            },
            CustomerType.SENIORS: {
                "style": "尊重、專業、詳細",
                "keywords": ["文化", "深度", "舒適", "品質", "專業"],
                "pain_points": ["文化體驗", "舒適度", "專業導覽"]
            }
        }

        # 季節性主題
        self.seasonal_themes = {
            Season.SPRING: {
                "themes": ["賞花季節", "櫻花", "薰衣草", "溫和氣候", "畢業旅行", "春假親子遊"],
                "emotions": ["新生", "浪漫", "溫暖", "希望"],
                "activities": ["賞花", "戶外踏青", "文化體驗", "輕度健行"]
            },
            Season.SUMMER: {
                "themes": ["海島度假", "避暑勝地", "暑假家庭旅遊", "水上活動"],
                "emotions": ["活力", "清爽", "歡樂", "冒險"],
                "activities": ["海邊戲水", "潛水", "衝浪", "夏日祭典"]
            },
            Season.AUTUMN: {
                "themes": ["賞楓行程", "溫泉養生", "美食之旅", "文化體驗"],
                "emotions": ["詩意", "溫馨", "豐收", "沉靜"],
                "activities": ["賞楓", "泡溫泉", "品嚐美食", "文化導覽"]
            },
            Season.WINTER: {
                "themes": ["溫暖南方避寒", "雪景滑雪體驗", "年節慶典", "尾牙春酒旅遊"],
                "emotions": ["溫暖", "歡聚", "慶祝", "感恩"],
                "activities": ["滑雪", "溫泉", "聖誕市集", "新年慶典"]
            }
        }

        # 常用hashtag庫
        self.hashtag_pool = {
            "brand": ["#自然國際旅行社", "#25年專業經驗", "#客製化旅遊", "#專業旅遊規劃"],
            "general": ["#旅遊", "#旅行", "#度假", "#探索世界", "#美好時光", "#專業服務"],
            "emotional": ["#夢想成真", "#美好回憶", "#深度體驗", "#文化探索", "#在地體驗"],
            "service": ["#客製化行程", "#專業導遊", "#24小時服務", "#安心旅遊", "#品質保證"]
        }

    def generate_post(self,
                     destination: str,
                     post_type: PostType,
                     season: Season,
                     customer_type: CustomerType,
                     specific_theme: Optional[str] = None) -> PostContent:
        """
        生成Facebook貼文

        Args:
            destination: 目的地
            post_type: 貼文類型
            season: 季節
            customer_type: 客群類型
            specific_theme: 特定主題（可選）

        Returns:
            PostContent: 完整的貼文內容
        """

        # 根據類型生成對應內容
        if post_type == PostType.EDUCATIONAL:
            return self._generate_educational_post(destination, season, customer_type, specific_theme)
        elif post_type == PostType.INSPIRATIONAL:
            return self._generate_inspirational_post(destination, season, customer_type, specific_theme)
        elif post_type == PostType.SERVICE_SHOWCASE:
            return self._generate_service_post(destination, season, customer_type, specific_theme)
        elif post_type == PostType.INTERACTIVE:
            return self._generate_interactive_post(destination, season, customer_type, specific_theme)
        else:
            raise ValueError(f"不支援的貼文類型: {post_type}")

    def _generate_educational_post(self, destination: str, season: Season,
                                 customer_type: CustomerType, specific_theme: Optional[str]) -> PostContent:
        """生成教育性貼文"""

        customer_style = self.customer_styles[customer_type]
        seasonal_info = self.seasonal_themes[season]

        # 選擇季節相關主題
        theme = specific_theme or random.choice(seasonal_info["themes"])
        activity = random.choice(seasonal_info["activities"])

        # 根據客群調整開頭
        if customer_type == CustomerType.YOUNG_COUPLES:
            opener = f"想和另一半在{destination}來場{theme}嗎？✨"
        elif customer_type == CustomerType.FAMILIES:
            opener = f"帶著孩子到{destination}體驗{theme}，寓教於樂的最佳選擇！👨‍👩‍👧‍👦"
        else:
            opener = f"深度探索{destination}的{theme}，讓旅程充滿文化底蘊 🎌"

        # 主要內容（教育性資訊）
        educational_tips = [
            f"💡 最佳{activity}時間：建議避開人潮，選擇清晨或傍晚時段",
            f"📍 必訪景點：當地人推薦的隱藏版景點，讓您體驗最道地的{destination}",
            f"🍽️ 美食推薦：品嚐季節限定料理，感受{destination}的飲食文化",
            f"🚌 交通貼士：善用當地交通工具，既環保又能深入了解當地生活"
        ]

        selected_tips = random.sample(educational_tips, 3)
        tips_text = "\n\n".join(selected_tips)

        # 專業建議
        professional_advice = f"\n\n🔸 25年專業經驗分享：{destination}的{theme}每年都有微妙變化，我們的在地夥伴會即時更新最佳觀賞地點和時機，確保您的旅程完美無遺憾！"

        # 組合主文案
        main_text = f"{opener}\n\n{tips_text}{professional_advice}"

        # 確保字數控制在150-200字
        if len(main_text) > 200:
            main_text = main_text[:197] + "..."

        # 生成hashtag
        hashtags = self._generate_hashtags(destination, season, customer_type, ["教育", "攻略", "貼士"])

        # CTA
        cta = "想了解更多專業建議嗎？歡迎私訊我們，讓25年經驗為您規劃最完美的行程！"

        # 最佳發布時間
        best_time = "週二至週四 10:00-16:00（教育性內容的黃金時段）"

        # 互動建議
        engagement_tips = [
            "在留言區分享更多實用小貼士",
            "邀請粉絲分享自己的旅遊經驗",
            "提供免費的旅遊諮詢服務"
        ]

        return PostContent(
            main_text=main_text,
            hashtags=hashtags,
            call_to_action=cta,
            best_post_time=best_time,
            engagement_tips=engagement_tips
        )

    def _generate_inspirational_post(self, destination: str, season: Season,
                                   customer_type: CustomerType, specific_theme: Optional[str]) -> PostContent:
        """生成靈感性貼文"""

        seasonal_info = self.seasonal_themes[season]
        customer_style = self.customer_styles[customer_type]

        # 情感詞彙
        emotion = random.choice(seasonal_info["emotions"])
        theme = specific_theme or random.choice(seasonal_info["themes"])

        # 根據客群調整靈感開頭
        if customer_type == CustomerType.YOUNG_COUPLES:
            opener = f"💕 還在煩惱要和心愛的人去哪裡製造美好回憶嗎？"
        elif customer_type == CustomerType.FAMILIES:
            opener = f"👨‍👩‍👧‍👦 想給家人一個難忘的{season.value}假期嗎？"
        else:
            opener = f"🌟 人生就該有幾次深度的{emotion}之旅..."

        # 夢想場景描述
        if customer_type == CustomerType.YOUNG_COUPLES:
            dream_scene = f"想像一下，您和另一半漫步在{destination}的{theme}中，陽光灑在臉上，微風輕拂，這一刻的幸福感會成為你們最珍貴的回憶 ✨"
        elif customer_type == CustomerType.FAMILIES:
            dream_scene = f"看著孩子們在{destination}開心探索{theme}，那純真的笑容和好奇的眼神，是給父母最好的禮物 🎁"
        else:
            dream_scene = f"在{destination}的{theme}中，感受歲月沉澱的智慧與{emotion}，每一個轉彎都是新的發現，每一次體驗都是心靈的豐富 🍃"

        # 品牌價值連結
        brand_connection = f"\n\n自然國際旅行社25年來，就是希望為每位旅客創造這樣的{emotion}時刻。我們相信，旅行不只是移動，更是心靈的觸動與成長 🌱"

        # 行動激勵
        motivation = f"\n\n不要讓夢想只是夢想，讓我們一起把它變成美好的現實！"

        main_text = f"{opener}\n\n{dream_scene}{brand_connection}{motivation}"

        # 字數控制
        if len(main_text) > 200:
            main_text = main_text[:197] + "..."

        # 生成hashtag
        hashtags = self._generate_hashtags(destination, season, customer_type, ["夢想", "靈感", "美好"])

        # CTA
        cta = "準備好開始您的夢想之旅了嗎？讓我們聊聊您心中的旅遊藍圖吧！💌"

        # 最佳發布時間
        best_time = "週五至週日 18:00-21:00（休閒放鬆時段，更容易觸動情感）"

        # 互動建議
        engagement_tips = [
            "邀請粉絲分享他們的旅遊夢想",
            "詢問最想去的目的地",
            "分享旅客的美好回憶故事"
        ]

        return PostContent(
            main_text=main_text,
            hashtags=hashtags,
            call_to_action=cta,
            best_post_time=best_time,
            engagement_tips=engagement_tips
        )

    def _generate_service_post(self, destination: str, season: Season,
                             customer_type: CustomerType, specific_theme: Optional[str]) -> PostContent:
        """生成服務展示貼文"""

        customer_style = self.customer_styles[customer_type]

        # 服務特色展示
        services = [
            "🎯 完全客製化行程規劃：根據您的喜好、預算、時間，量身打造專屬旅程",
            "👥 專業在地導覽團隊：深度了解當地文化，讓您的旅行更有深度",
            "📞 24小時緊急聯絡服務：無論何時何地，我們都是您最可靠的後盾",
            "💬 專屬LINE群組服務：出發前詳細說明，旅途中即時支援",
            "🏆 25年專業經驗累積：服務過無數旅客，擁有豐富的實戰經驗",
            "🤝 當地合作夥伴網絡：與全球優質旅行社合作，提供最佳在地體驗"
        ]

        # 根據客群選擇重點服務
        if customer_type == CustomerType.YOUNG_COUPLES:
            opener = f"計劃到{destination}的浪漫之旅嗎？讓我們的專業服務為您打造完美回憶！💕"
            key_services = [s for s in services if any(word in s for word in ["客製化", "專屬", "完美"])]
        elif customer_type == CustomerType.FAMILIES:
            opener = f"帶著全家到{destination}旅遊，安全和品質是您最在意的嗎？我們懂您的需求！👨‍👩‍👧‍👦"
            key_services = [s for s in services if any(word in s for word in ["安全", "聯絡", "專業", "支援"])]
        else:
            opener = f"想要深度體驗{destination}的文化精髓嗎？25年的專業經驗為您開啟不同層次的旅遊體驗！🎌"
            key_services = [s for s in services if any(word in s for word in ["專業", "深度", "文化", "經驗"])]

        # 選擇2-3個重點服務
        selected_services = random.sample(key_services or services[:3], min(2, len(key_services or services)))
        services_text = "\n\n".join(selected_services)

        # 客戶見證（簡短）
        testimonial = f"\n\n💭 客戶回饋：「自然國際真的很用心！每個細節都幫我們想到了，讓我們玩得很安心又開心！」"

        # 差異化說明
        difference = f"\n\n🌟 這就是我們與一般旅行社的不同：不只是賣行程，更是您的旅遊夥伴！"

        main_text = f"{opener}\n\n{services_text}{testimonial}{difference}"

        # 字數控制
        if len(main_text) > 200:
            main_text = main_text[:197] + "..."

        # 生成hashtag
        hashtags = self._generate_hashtags(destination, season, customer_type, ["專業服務", "客製化", "品質保證"])

        # CTA
        cta = "想體驗我們的專業服務嗎？立即私訊或來電諮詢，免費為您規劃專屬行程！"

        # 最佳發布時間
        best_time = "週一、週三 09:00-11:00（商務時段，決策考量時期）"

        # 互動建議
        engagement_tips = [
            "邀請客戶分享服務體驗",
            "提供免費諮詢優惠",
            "展示更多服務細節照片"
        ]

        return PostContent(
            main_text=main_text,
            hashtags=hashtags,
            call_to_action=cta,
            best_post_time=best_time,
            engagement_tips=engagement_tips
        )

    def _generate_interactive_post(self, destination: str, season: Season,
                                 customer_type: CustomerType, specific_theme: Optional[str]) -> PostContent:
        """生成互動參與貼文"""

        seasonal_info = self.seasonal_themes[season]
        theme = specific_theme or random.choice(seasonal_info["themes"])

        # 互動問題類型
        interaction_types = [
            "選擇題投票",
            "經驗分享",
            "願望清單",
            "推薦詢問",
            "小測驗"
        ]

        interaction_type = random.choice(interaction_types)

        if interaction_type == "選擇題投票":
            if customer_type == CustomerType.YOUNG_COUPLES:
                question = f"💕 和另一半到{destination}{theme}，您最想體驗什麼？"
                options = ["🌸 浪漫賞花野餐", "📸 網美景點拍照", "🍽️ 當地特色美食", "🎭 傳統文化體驗"]
            elif customer_type == CustomerType.FAMILIES:
                question = f"👨‍👩‍👧‍👦 帶孩子到{destination}，您最重視什麼？"
                options = ["🛡️ 安全完善的設施", "🎓 寓教於樂的體驗", "🏨 親子友善的住宿", "🍎 健康的飲食安排"]
            else:
                question = f"🎌 到{destination}深度旅遊，您最期待什麼？"
                options = ["🏛️ 歷史文化探索", "🍵 傳統工藝體驗", "🌿 自然景觀欣賞", "👥 當地人文交流"]

        elif interaction_type == "經驗分享":
            question = f"🗣️ 來分享一下！您去過{destination}嗎？最難忘的{theme}體驗是什麼？"
            options = ["我們很想聽聽您的故事！", "還沒去過但很想去？告訴我們您的期待！"]

        elif interaction_type == "願望清單":
            question = f"✨ 說說看，{destination}的{theme}中，您最想實現的旅遊願望是什麼？"
            options = ["在留言區許下您的旅遊願望", "讓我們一起幫您實現夢想！"]

        elif interaction_type == "推薦詢問":
            question = f"🤔 正在規劃{destination}之旅嗎？關於{theme}，您最想知道什麼？"
            options = ["最佳時間？", "必去景點？", "當地美食？", "交通方式？", "住宿推薦？"]

        else:  # 小測驗
            question = f"🧠 小測驗時間！您對{destination}的{theme}了解多少？"
            options = ["專家級！", "略知一二", "完全新手", "想要學習更多！"]

        # 建立互動內容
        main_content = f"{question}\n\n"

        if isinstance(options, list) and len(options) > 2:
            for i, option in enumerate(options, 1):
                main_content += f"{option}\n"
        else:
            main_content += "\n".join(options)

        # 品牌專業性展示
        expert_tip = f"\n\n💡 小貼士：作為{destination}旅遊專家，我們發現{theme}的最佳體驗往往藏在細節中。25年來累積的在地資源，讓我們能為您安排最道地的體驗！"

        # 互動鼓勵
        encouragement = f"\n\n快在下面留言跟我們互動吧！我們會親自回覆每一位朋友 😊"

        main_text = f"{main_content}{expert_tip}{encouragement}"

        # 字數控制
        if len(main_text) > 200:
            main_text = main_text[:197] + "..."

        # 生成hashtag
        hashtags = self._generate_hashtags(destination, season, customer_type, ["互動", "分享", "交流"])

        # CTA
        cta = "快來留言分享您的想法，讓我們一起規劃最棒的旅程！"

        # 最佳發布時間
        best_time = "週五至週日 18:00-21:00（社交活躍時段）"

        # 互動建議
        engagement_tips = [
            "及時回覆每一個留言",
            "詢問更深入的問題延續討論",
            "分享相關的專業建議"
        ]

        return PostContent(
            main_text=main_text,
            hashtags=hashtags,
            call_to_action=cta,
            best_post_time=best_time,
            engagement_tips=engagement_tips
        )

    def _generate_hashtags(self, destination: str, season: Season,
                          customer_type: CustomerType, theme_tags: List[str]) -> List[str]:
        """生成相關hashtag"""

        hashtags = []

        # 品牌hashtag（必選）
        hashtags.extend(random.sample(self.hashtag_pool["brand"], 2))

        # 一般旅遊hashtag
        hashtags.extend(random.sample(self.hashtag_pool["general"], 2))

        # 情感hashtag
        hashtags.append(random.choice(self.hashtag_pool["emotional"]))

        # 服務hashtag
        hashtags.append(random.choice(self.hashtag_pool["service"]))

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
        unique_hashtags = list(dict.fromkeys(hashtags))  # 保持順序去重
        return unique_hashtags[:12]  # 限制在12個以內


def main():
    """主函數 - 使用範例"""

    generator = FacebookPostGenerator()

    # 使用範例
    print("=== Facebook 貼文生成器範例 ===\n")

    # 範例1：教育性貼文
    post1 = generator.generate_post(
        destination="京都",
        post_type=PostType.EDUCATIONAL,
        season=Season.SPRING,
        customer_type=CustomerType.YOUNG_COUPLES,
        specific_theme="櫻花季"
    )

    print("【教育性貼文範例】")
    print(f"主文案：\n{post1.main_text}\n")
    print(f"Hashtags: {' '.join(post1.hashtags)}\n")
    print(f"行動呼籲：{post1.call_to_action}\n")
    print(f"最佳發布時間：{post1.best_post_time}\n")
    print(f"互動建議：{', '.join(post1.engagement_tips)}\n")
    print("-" * 50)

    # 範例2：靈感性貼文
    post2 = generator.generate_post(
        destination="峇里島",
        post_type=PostType.INSPIRATIONAL,
        season=Season.SUMMER,
        customer_type=CustomerType.FAMILIES
    )

    print("【靈感性貼文範例】")
    print(f"主文案：\n{post2.main_text}\n")
    print(f"Hashtags: {' '.join(post2.hashtags)}\n")
    print(f"行動呼籲：{post2.call_to_action}\n")
    print(f"最佳發布時間：{post2.best_post_time}\n")
    print(f"互動建議：{', '.join(post2.engagement_tips)}\n")
    print("-" * 50)


if __name__ == "__main__":
    main()