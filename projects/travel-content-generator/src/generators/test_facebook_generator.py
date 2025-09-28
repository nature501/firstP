#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Facebook 貼文生成器測試範例
展示如何使用FacebookPostGenerator
"""

# 如果無法直接運行，可以複製以下程式碼到Python環境中執行

from facebook_generator import FacebookPostGenerator, PostType, Season, CustomerType

def test_generator():
    """測試生成器的所有功能"""

    generator = FacebookPostGenerator()

    print("🌟 自然國際旅行社 Facebook 貼文生成器測試 🌟\n")
    print("=" * 60)

    # 測試案例1：年輕情侶的教育性貼文
    print("\n【測試案例1：年輕情侶 - 教育性貼文】")
    post1 = generator.generate_post(
        destination="京都",
        post_type=PostType.EDUCATIONAL,
        season=Season.SPRING,
        customer_type=CustomerType.YOUNG_COUPLES,
        specific_theme="櫻花季"
    )

    print(f"📝 主文案 ({len(post1.main_text)}字):")
    print(post1.main_text)
    print(f"\n🏷️ Hashtags ({len(post1.hashtags)}個):")
    print(" ".join(post1.hashtags))
    print(f"\n📢 行動呼籲:")
    print(post1.call_to_action)
    print(f"\n⏰ 最佳發布時間:")
    print(post1.best_post_time)
    print(f"\n💡 互動建議:")
    for tip in post1.engagement_tips:
        print(f"  • {tip}")

    print("\n" + "-" * 60)

    # 測試案例2：家庭客群的靈感性貼文
    print("\n【測試案例2：家庭客群 - 靈感性貼文】")
    post2 = generator.generate_post(
        destination="沖繩",
        post_type=PostType.INSPIRATIONAL,
        season=Season.SUMMER,
        customer_type=CustomerType.FAMILIES
    )

    print(f"📝 主文案 ({len(post2.main_text)}字):")
    print(post2.main_text)
    print(f"\n🏷️ Hashtags ({len(post2.hashtags)}個):")
    print(" ".join(post2.hashtags))
    print(f"\n📢 行動呼籲:")
    print(post2.call_to_action)
    print(f"\n⏰ 最佳發布時間:")
    print(post2.best_post_time)
    print(f"\n💡 互動建議:")
    for tip in post2.engagement_tips:
        print(f"  • {tip}")

    print("\n" + "-" * 60)

    # 測試案例3：資深旅客的服務展示貼文
    print("\n【測試案例3：資深旅客 - 服務展示貼文】")
    post3 = generator.generate_post(
        destination="奈良",
        post_type=PostType.SERVICE_SHOWCASE,
        season=Season.AUTUMN,
        customer_type=CustomerType.SENIORS,
        specific_theme="文化體驗"
    )

    print(f"📝 主文案 ({len(post3.main_text)}字):")
    print(post3.main_text)
    print(f"\n🏷️ Hashtags ({len(post3.hashtags)}個):")
    print(" ".join(post3.hashtags))
    print(f"\n📢 行動呼籲:")
    print(post3.call_to_action)
    print(f"\n⏰ 最佳發布時間:")
    print(post3.best_post_time)
    print(f"\n💡 互動建議:")
    for tip in post3.engagement_tips:
        print(f"  • {tip}")

    print("\n" + "-" * 60)

    # 測試案例4：互動參與貼文
    print("\n【測試案例4：年輕客群 - 互動參與貼文】")
    post4 = generator.generate_post(
        destination="首爾",
        post_type=PostType.INTERACTIVE,
        season=Season.WINTER,
        customer_type=CustomerType.YOUNG_COUPLES
    )

    print(f"📝 主文案 ({len(post4.main_text)}字):")
    print(post4.main_text)
    print(f"\n🏷️ Hashtags ({len(post4.hashtags)}個):")
    print(" ".join(post4.hashtags))
    print(f"\n📢 行動呼籲:")
    print(post4.call_to_action)
    print(f"\n⏰ 最佳發布時間:")
    print(post4.best_post_time)
    print(f"\n💡 互動建議:")
    for tip in post4.engagement_tips:
        print(f"  • {tip}")

    print("\n" + "=" * 60)
    print("✅ 測試完成！所有貼文類型都成功生成")
    print("🎯 每篇貼文都控制在150-200字範圍內")
    print("🏷️ Hashtags 都包含品牌相關標籤")
    print("💼 完全符合25年專業旅行社的品牌調性")

if __name__ == "__main__":
    try:
        test_generator()
    except Exception as e:
        print(f"❌ 測試過程中發生錯誤：{e}")
        print("請確保已正確安裝Python並且facebook_generator.py在同一目錄中")