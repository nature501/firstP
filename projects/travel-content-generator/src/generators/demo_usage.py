#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Facebook 貼文生成器 V2.0 使用示範
展示批量生成、自訂填入、細緻風格控制功能
"""

from facebook_generator_v2 import (
    FacebookPostGeneratorV2,
    BatchPostRequest,
    PostType,
    Season,
    CustomerType,
    ToneStyle
)
import json

def demo_batch_generation():
    """示範批量生成功能"""

    print("🚀 Facebook 貼文生成器 V2.0 功能示範")
    print("=" * 50)

    generator = FacebookPostGeneratorV2()

    # 示範1：生成5篇京都春季貼文（年輕情侶客群）
    print("\n【示範1：批量生成 - 京都春季年輕客群貼文】")

    request1 = BatchPostRequest(
        destination="京都",
        season=Season.SPRING,
        customer_type=CustomerType.YOUNG_COUPLES,
        post_count=5,
        tone_style=ToneStyle.WARM,
        specific_themes=["櫻花季", "和服體驗", "抹茶文化", "夜櫻美景", "傳統工藝"],
        include_templates=True,
        include_examples=True
    )

    result1 = generator.generate_batch_posts(request1)

    print(f"✅ 成功生成 {len(result1['templates'])} 篇模板")
    print(f"✅ 成功生成 {len(result1['examples'])} 篇範例")

    # 顯示第一個模板
    template = result1['templates'][0]
    print(f"\n📋 模板範例 - {template['title']}")
    print(f"類型：{template['post_type']}")
    print(f"風格指引：{template['style_notes']}")
    print(f"\n📝 可填入的模板文案：")
    print(template['template_text'])
    print(f"\n💡 填入指引：")
    print(f"主題：{template['theme_guidance']}")
    print(f"內容：{template['content_guidance']}")
    print(f"\n🌰 範例示範：")
    print(f"主題範例：{template['example_theme']}")
    print(f"內容範例：{template['example_content']}")

    print("\n" + "-" * 50)

    # 示範2：生成3篇沖繩夏季貼文（家庭客群）
    print("\n【示範2：批量生成 - 沖繩夏季家庭客群貼文】")

    request2 = BatchPostRequest(
        destination="沖繩",
        season=Season.SUMMER,
        customer_type=CustomerType.FAMILIES,
        post_count=3,
        tone_style=ToneStyle.PROFESSIONAL,
        post_types=[PostType.EDUCATIONAL, PostType.SERVICE_SHOWCASE, PostType.INTERACTIVE],
        include_templates=True,
        include_examples=False  # 只要模板，不要範例
    )

    result2 = generator.generate_batch_posts(request2)

    print(f"✅ 成功生成 {len(result2['templates'])} 篇專業風格模板")

    # 顯示模板摘要
    for i, template in enumerate(result2['templates'], 1):
        print(f"\n📋 模板 {i}：{template['title']}")
        print(f"   類型：{template['post_type']} | 目標字數：{template['word_count_target']}")
        print(f"   最佳發布時間：{template['best_post_time']}")
        print(f"   主要hashtag：{', '.join(template['hashtags'][:5])}")

    print("\n" + "-" * 50)

    # 示範3：自訂填入展示
    print("\n【示範3：自訂填入功能展示】")

    # 取得一個模板
    template = result1['templates'][0]  # 使用京都春季的第一個模板

    print("📝 原始模板：")
    print(template['template_text'])

    # 模擬使用者填入內容
    user_theme = "哲學之道櫻花隧道"
    user_content = """早晨7點最佳拍照時刻，避開人潮 📸
沿途有多家特色咖啡廳可休憩 ☕
建議穿著淡色衣服與櫻花搭配 👘
記得帶行動電源，美景太多會狂拍照！ 🔋"""

    # 填入內容
    filled_text = template['template_text'].replace("{主題}", user_theme)
    filled_text = filled_text.replace("{具體內容}", user_content)

    print(f"\n✨ 填入內容後的完整貼文：")
    print(filled_text)
    print(f"\n📊 字數統計：{len(filled_text)} 字")
    print(f"🏷️ 建議hashtag：{' '.join(template['hashtags'])}")

    print("\n" + "=" * 50)
    print("🎯 V2.0 新功能總結：")
    print("✅ 批量生成：一次生成多篇貼文模板")
    print("✅ 留空填入：{主題}和{具體內容}供您客製化")
    print("✅ 細緻控制：語調風格、客群類型、季節主題")
    print("✅ 完整指引：每個模板都有詳細的填入說明")
    print("✅ 範例參考：提供完整填入範例供參考")
    print("✅ 品牌一致：嚴格遵循25年旅行社品牌風格")

def demo_customization_options():
    """示範客製化選項"""

    print("\n" + "=" * 50)
    print("🎨 客製化選項示範")

    generator = FacebookPostGeneratorV2()

    # 不同語調風格比較
    print("\n【語調風格比較】同一內容，不同風格表現：")

    base_request = BatchPostRequest(
        destination="台東",
        season=Season.AUTUMN,
        customer_type=CustomerType.SENIORS,
        post_count=1,
        post_types=[PostType.INSPIRATIONAL],
        include_templates=True,
        include_examples=False
    )

    styles = [ToneStyle.PROFESSIONAL, ToneStyle.WARM, ToneStyle.ENERGETIC, ToneStyle.BALANCED]

    for style in styles:
        base_request.tone_style = style
        result = generator.generate_batch_posts(base_request)
        template = result['templates'][0]

        print(f"\n🎭 {style.value.upper()} 風格：")
        print(f"   {template['template_text'][:100]}...")
        print(f"   風格特色：{template['style_notes']}")

def export_demo():
    """示範匯出功能"""

    print("\n" + "=" * 50)
    print("💾 匯出功能示範")

    generator = FacebookPostGeneratorV2()

    request = BatchPostRequest(
        destination="花蓮",
        season=Season.WINTER,
        customer_type=CustomerType.FAMILIES,
        post_count=3,
        include_templates=True,
        include_examples=True
    )

    result = generator.generate_batch_posts(request)

    # 匯出為JSON
    filepath = generator.export_to_json(result, "demo_花蓮冬季家庭貼文.json")
    print(f"✅ 結果已匯出至：{filepath}")

    # 顯示使用說明
    print(f"\n📋 使用說明：")
    for instruction in result['usage_instructions']:
        print(f"   {instruction}: {result['usage_instructions'][instruction]}")

if __name__ == "__main__":
    # 執行所有示範
    demo_batch_generation()
    demo_customization_options()
    export_demo()

    print("\n" + "🎉" * 20)
    print("示範完成！您現在可以：")
    print("1. 複製模板文案，填入您的{主題}和{具體內容}")
    print("2. 根據指引調整風格和內容")
    print("3. 參考範例了解填入方式")
    print("4. 依照建議時間發布獲得最佳效果")
    print("🎉" * 20)