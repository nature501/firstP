#!/usr/bin/env node

const fs = require('fs').promises;
const path = require('path');

class WulitouWriter {
    constructor() {
        this.projectRoot = __dirname + '/..';
        this.characterProfile = null;
        this.styleGuide = null;
        this.loadConfigurations();
    }

    async loadConfigurations() {
        try {
            // 載入角色設定
            const characterData = await fs.readFile(
                path.join(this.projectRoot, 'config/character_profile.json'),
                'utf8'
            );
            this.characterProfile = JSON.parse(characterData);

            // 載入寫作風格指南
            this.styleGuide = await fs.readFile(
                path.join(this.projectRoot, 'config/writing_style_guide.md'),
                'utf8'
            );
        } catch (error) {
            console.error('載入配置文件時發生錯誤:', error.message);
        }
    }

    generatePrompt(inputData) {
        const character = this.characterProfile.character;
        const { 主題, 文字量, 摘要備註 } = inputData.writing_request;

        const prompt = `
你現在是"無俚頭"，一位生於1968年的台灣資深寫手，真性情的老江湖。

## 你的核心特質：
- **出生年份**：1968年，現年56歲，經歷完整的台灣社會變遷
- **目標讀者**：${character.target_audience}
- **內容方針**：${character.content_approach}

## 你的寫作超能力：
- **文體變色龍**：${character.writing_superpowers.style_versatility}
- **語調大師**：${character.writing_superpowers.tone_mastery}
- **內容適應性**：${character.writing_superpowers.content_adaptability}
- **幽默光譜**：${character.writing_superpowers.humor_spectrum}
- **真實性**：${character.writing_superpowers.authenticity}

## 你的人格特色：
- **幽默風格**：${character.personality.humor_style}
- **寫作語調**：${character.personality.writing_tone}
- **人生觀點**：${character.personality.perspective}
- **特殊技能**：${character.personality.special_traits}

## 你的專精領域：
${character.writing_specialties.nostalgia_comparison}、${character.writing_specialties.cultural_observation}、${character.writing_specialties.technology_adaptation}、${character.writing_specialties.human_nature}、${character.writing_specialties.generational_gap}、${character.writing_specialties.adult_topics}、${character.writing_specialties.dark_humor}

## 你的招牌用語：
${character.signature_phrases.join('、')}

## 你的寫作關鍵字：
${character.writing_keywords.join('、')}

## 豐富的人生經歷：
### 童年1970年代：
政治：${character.life_experiences.childhood_1970s.political_environment}
社會：${character.life_experiences.childhood_1970s.social_life}
科技：${character.life_experiences.childhood_1970s.technology}
娛樂：${character.life_experiences.childhood_1970s.entertainment}
成人記憶：${character.life_experiences.childhood_1970s.adult_memories}

### 青年1980年代：
政治：${character.life_experiences.youth_1980s.political_environment}
社會：${character.life_experiences.youth_1980s.social_life}
科技：${character.life_experiences.youth_1980s.technology}
娛樂：${character.life_experiences.youth_1980s.entertainment}
成年覺醒：${character.life_experiences.youth_1980s.adult_awakening}

### 成年1990年代：
政治：${character.life_experiences.adulthood_1990s.political_environment}
社會：${character.life_experiences.adulthood_1990s.social_life}
科技：${character.life_experiences.adulthood_1990s.technology}
成人生活：${character.life_experiences.adulthood_1990s.adult_life}

### 中年2000年代：
社會：${character.life_experiences.middle_age_2000s.social_life}
科技：${character.life_experiences.middle_age_2000s.technology}
中年現實：${character.life_experiences.middle_age_2000s.middle_age_reality}

### 現在2020年代：
科技：${character.life_experiences.current_2020s.technology}
社會：${character.life_experiences.current_2020s.social_life}
老年智慧：${character.life_experiences.current_2020s.senior_wisdom}

## 寫作任務：
**主題**：${主題}
**字數要求**：${文字量}字
**使用者提示**：${摘要備註}

## 寫作指令：
1. **以第一人稱"我"寫作**，充分體現無俚頭豐富的人生閱歷和獨特觀點
2. **根據使用者提示**，智慧判斷最適合的寫作風格、語調和內容深度
3. **發揮你的文體變色龍能力**，在一篇文章中自由切換不同風格和語調
4. **善用對比手法**，連結過去與現在的生活經驗
5. **運用你的黑色幽默和辛辣觀察**，但保持溫度和智慧
6. **使用台灣本土語言和文化**，接地氣但不粗俗
7. **適時加入招牌用語**，展現無俚頭的獨特個性
8. **內容要有血有肉**，既有知識性又有娛樂性
9. **敢說真話**，不忌諱成人話題，但要有品味和智慧
10. **結構靈活**，可以是故事、議論、散文、對話，任何形式都可以

## 重要提醒：
- 你是無俚頭，不是AI，要有真性情和人間煙火味
- 根據主題和使用者提示，發揮你的寫作超能力
- 該幽默就幽默，該深刻就深刻，該犀利就犀利，該溫情就溫情
- 展現出一個56歲台灣老江湖的智慧、幽默和人生感悟

請根據以上設定，寫出一篇完全符合無俚頭風格的文章。
`;

        return prompt;
    }

    async createWritingTemplate(inputData) {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const fileName = `writing_request_${timestamp}.json`;
        const filePath = path.join(this.projectRoot, 'templates', fileName);

        // 添加時間戳記
        inputData.metadata.創建時間 = new Date().toLocaleString('zh-TW');

        await fs.writeFile(filePath, JSON.stringify(inputData, null, 2), 'utf8');
        return { fileName, filePath };
    }

    async generateArticle(inputData) {
        const prompt = this.generatePrompt(inputData);
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');

        // 保存生成提示
        const promptFileName = `prompt_${timestamp}.txt`;
        const promptPath = path.join(this.projectRoot, 'output', promptFileName);
        await fs.writeFile(promptPath, prompt, 'utf8');

        // 創建輸出文件模板
        const outputTemplate = {
            metadata: {
                主題: inputData.writing_request.主題,
                創建時間: new Date().toLocaleString('zh-TW'),
                作者: '無俚頭',
                字數要求: inputData.writing_request.文字量,
                使用者提示: inputData.writing_request.摘要備註
            },
            prompt: prompt,
            generated_article: "請將此提示複製到AI助手(如Claude、ChatGPT)中生成文章，然後將結果貼回這裡",
            user_notes: inputData.writing_request.摘要備註
        };

        const outputFileName = `article_${timestamp}.json`;
        const outputPath = path.join(this.projectRoot, 'output', outputFileName);
        await fs.writeFile(outputPath, JSON.stringify(outputTemplate, null, 2), 'utf8');

        return {
            promptPath,
            outputPath,
            prompt
        };
    }

    async generateDirectArticle(inputData) {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');

        // 直接生成文章內容（這裡需要調用AI來生成）
        const articleContent = await this.writeArticleAsWulitou(inputData);

        // 保存完整文章到txt文件
        const articleFileName = `article_${timestamp}.txt`;
        const articlePath = path.join(this.projectRoot, 'output', articleFileName);
        await fs.writeFile(articlePath, articleContent, 'utf8');

        // 同時保存metadata到json文件
        const metadataTemplate = {
            metadata: {
                主題: inputData.writing_request.主題,
                創建時間: new Date().toLocaleString('zh-TW'),
                作者: '無俚頭',
                字數要求: inputData.writing_request.文字量,
                使用者提示: inputData.writing_request.摘要備註,
                文章檔案: articleFileName
            },
            user_notes: inputData.writing_request.摘要備註
        };

        const metadataFileName = `metadata_${timestamp}.json`;
        const metadataPath = path.join(this.projectRoot, 'output', metadataFileName);
        await fs.writeFile(metadataPath, JSON.stringify(metadataTemplate, null, 2), 'utf8');

        return {
            articlePath,
            metadataPath,
            content: articleContent
        };
    }

    async writeArticleAsWulitou(inputData) {
        // 這個方法將整合無俚頭的角色設定來寫文章
        // 實際使用時，這裡會通過Claude Code直接調用AI生成
        const character = this.characterProfile.character;
        const { 主題, 文字量, 摘要備註 } = inputData.writing_request;

        // 返回提示信息，實際生成需要通過外部AI
        return `請使用Claude Code直接調用AI來生成無俚頭風格的文章：

主題：${主題}
字數：${文字量}
需求：${摘要備註}

使用角色設定：${JSON.stringify(character, null, 2)}`;
    }

    async createUserInterface() {
        const template = await fs.readFile(
            path.join(this.projectRoot, 'templates/input_template.json'),
            'utf8'
        );

        const userInterfaceFile = path.join(this.projectRoot, 'user_input.json');
        await fs.writeFile(userInterfaceFile, template, 'utf8');

        console.log(`\n📝 無俚頭寫手系統已升級完成！\n`);
        console.log(`🎯 重點提醒：`);
        console.log(`   - 無俚頭現在是真性情的老江湖，什麼都敢寫`);
        console.log(`   - 對象是成人讀者，不忌諱任何話題`);
        console.log(`   - 最重要的是"摘要備註"欄位，請詳細描述您的需求\n`);
        console.log(`請編輯以下文件來輸入您的寫作需求：`);
        console.log(`文件路徑: ${userInterfaceFile}\n`);
        console.log(`編輯完成後，選擇以下方式之一：\n`);
        console.log(`💡 方法一（生成prompt）：node src/wulitou_writer.js generate`);
        console.log(`💡 方法二（直接生成）：node src/wulitou_writer.js generate direct`);
        console.log(`💡 方法三（使用Claude Code）：直接告訴Claude "請讀取user_input.json並生成文章"\n`);

        return userInterfaceFile;
    }
}

// 主程式邏輯
async function main() {
    const writer = new WulitouWriter();
    const command = process.argv[2];
    const subCommand = process.argv[3];

    if (command === 'generate') {
        try {
            const userInputPath = path.join(writer.projectRoot, 'user_input.json');
            const inputData = JSON.parse(await fs.readFile(userInputPath, 'utf8'));

            // 驗證必要欄位
            if (!inputData.writing_request.主題) {
                console.error('❌ 錯誤：請填入主題');
                return;
            }
            if (!inputData.writing_request.文字量) {
                console.error('❌ 錯誤：請填入字數要求');
                return;
            }
            if (!inputData.writing_request.摘要備註 || inputData.writing_request.摘要備註.includes('【重要】請在此詳細描述')) {
                console.error('❌ 錯誤：請在摘要備註中詳細描述您的寫作需求');
                return;
            }

            if (subCommand === 'direct') {
                // 方法二：直接生成完整文章
                const result = await writer.generateDirectArticle(inputData);

                console.log('\n✅ 無俚頭文章已生成！');
                console.log(`\n📄 文章檔案: ${result.articlePath}`);
                console.log(`📋 資料檔案: ${result.metadataPath}`);
                console.log(`\n🎭 無俚頭說：「文章寫好了，請直接使用Claude Code來完成！」\n`);
                console.log('📝 提醒：實際文章內容需要通過Claude Code的AI能力來生成');

            } else {
                // 方法一：生成prompt供外部AI使用
                const result = await writer.generateArticle(inputData);

                console.log('\n✅ 無俚頭的寫作提示已生成！');
                console.log(`\n📋 提示文件: ${result.promptPath}`);
                console.log(`📄 輸出模板: ${result.outputPath}`);
                console.log(`\n🎭 無俚頭說：「來吧，看我怎麼把這個主題寫得有血有肉！」\n`);
                console.log(`🤖 請複製以下提示到AI助手中：\n`);
                console.log('='.repeat(80));
                console.log(result.prompt);
                console.log('='.repeat(80));
            }

        } catch (error) {
            console.error('❌ 生成文章時發生錯誤:', error.message);
        }
    } else {
        await writer.createUserInterface();
    }
}

if (require.main === module) {
    main().catch(console.error);
}

module.exports = WulitouWriter;