## Overview
Recipe Generator AI is a Python application that uses OpenAI's Vision and Chat APIs to analyze food ingredients from images and generate creative recipes. The program can extract ingredients (including quantities and prices) from supermarket flyers or food images, then create both traditional and fusion recipes using the identified ingredients.

## Installation
1. Clone the repository
```bash
git clone https://github.com/daishir0/recipe-generator-ai.git
cd recipe-generator-ai
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Configure API key
```bash
cp config.sample.yaml config.yaml
```
Edit `config.yaml` and add your OpenAI API key.

## Usage
Run the program with an image URL:
```bash
python recipe_generator.py <image_url>
```

Example:
```bash
python recipe_generator.py https://example.com/food-image.jpg
```

The program will:
1. 🔍 Analyze the specified image and extract food ingredients with their quantities and prices
2. 📝 Generate three traditional recipes using the identified ingredients
3. 🌟 Create one innovative fusion recipe
4. 💰 Include estimated costs for each recipe

### Example Output
Here's an example using a supermarket flyer:
```bash
python recipe_generator.py https://image.tokubai.co.jp/images/bargain_office_leaflets/o=true/XXXX.jpg
```

Output will look like this:
```
🔍 お買い得な食材を探しています...

✨ 見つけた食材はこちら！
- 鶏もも肉 200g ¥298
- 豚小間切れ 150g ¥198
- 牛ロース 100g ¥398
- うどん 2玉 ¥158
- スパークリングワイン 750ml ¥1,280
...

📝 美味しいレシピを考えています...

🍽️ おすすめレシピの提案です！
[3つの異なるレシピが表示されます]

🌟 特別なレシピの提案です！
[創造的なフュージョンレシピが表示されます]
```

## Notes
- Requires an OpenAI API key with access to GPT-4 Vision and Chat models
- Image URL must be publicly accessible
- Internet connection required for API access
- Processing time may vary depending on API response time
- The image URL should be a direct link to the image file
- Cost estimates are approximate and may vary by region

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# レシピジェネレーターAI 🍳

## 概要
レシピジェネレーターAIは、OpenAIのVisionおよびChatAPIを使用して、画像から食材を分析し、創造的なレシピを生成するPythonアプリケーションです。スーパーマーケットのチラシや食品の画像から材料（数量や価格を含む）を抽出し、その食材を使用した伝統的なレシピとフュージョンレシピの両方を作成できます。

## インストール方法
1. レポジトリをクローン
```bash
git clone https://github.com/daishir0/recipe-generator-ai.git
cd recipe-generator-ai
```

2. 必要なパッケージをインストール
```bash
pip install -r requirements.txt
```

3. APIキーの設定
```bash
cp config.sample.yaml config.yaml
```
`config.yaml`を編集し、OpenAI APIキーを追加してください。

## 使い方
画像URLを指定してプログラムを実行：
```bash
python recipe_generator.py <画像URL>
```

例：
```bash
python recipe_generator.py https://example.com/food-image.jpg
```

プログラムは以下の処理を行います：
1. 🔍 指定された画像を分析し、食材リストを数量や価格と共に抽出
2. 📝 抽出された食材を使用して3つの伝統的なレシピを生成
3. 🌟 1つの革新的なフュージョンレシピを作成
4. 💰 各レシピのおよその費用を計算

### 実行例
スーパーのチラシを使用した例：
```bash
python recipe_generator.py https://image.tokubai.co.jp/images/bargain_office_leaflets/o=true/XXXX.jpg
```

出力例：
```
🔍 お買い得な食材を探しています...

✨ 見つけた食材はこちら！
- 鶏もも肉 200g ¥298
- 豚小間切れ 150g ¥198
- 牛ロース 100g ¥398
- うどん 2玉 ¥158
- スパークリングワイン 750ml ¥1,280
...

📝 美味しいレシピを考えています...

🍽️ おすすめレシピの提案です！
[3つの異なるレシピが表示されます]

🌟 特別なレシピの提案です！
[創造的なフュージョンレシピが表示されます]
```

## 注意点
- OpenAI APIキー（GPT-4 VisionおよびChatモデルへのアクセス権限が必要）が必要です
- 画像URLは公開されているものである必要があります
- インターネット接続が必要です
- 処理時間はAPIのレスポンス時間によって変動する場合があります
- 画像URLは画像ファイルへの直接リンクである必要があります
- 費用の見積もりは概算であり、地域によって異なる場合があります

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
