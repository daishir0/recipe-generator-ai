import os
import sys
import yaml
import requests
from openai import OpenAI
from typing import List, Dict

def load_config() -> dict:
    """
    設定ファイルを読み込む
    """
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def analyze_image(client: OpenAI, image_url: str) -> List[str]:
    """
    Vision APIを使用して画像から食材リストを抽出する
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "この画像に写っているお買い得な食材を探してみましょう！各食材の名前、量（グラム数など）、お値段を教えてください。箇条書きでわかりやすく表示してくださいね。"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ],
        max_tokens=500
    )
    
    return response.choices[0].message.content.split('\n')

def generate_recipes(client: OpenAI, ingredients: List[str]) -> List[Dict[str, str]]:
    """
    食材リストから3つのレシピを生成する
    """
    ingredients_text = "\n".join(ingredients)
    prompt = f"""
    見つけた食材を使って、美味しそうなレシピを3つ考えてみましょう！
    各レシピには以下の情報を入れてくださいね：
    - 素敵な料理名
    - 必要な材料と量
    - わかりやすい手順
    - およその費用（※ざっくり計算で大丈夫です）

    今回使える食材はこちらです：
    {ingredients_text}

    家族や友達と楽しく作れるレシピを提案してください！
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a friendly and enthusiastic cooking assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000
    )
    
    return response.choices[0].message.content

def generate_creative_recipe(client: OpenAI, ingredients: List[str]) -> str:
    """
    食材リストから奇抜なレシピを生成する
    """
    ingredients_text = "\n".join(ingredients)
    prompt = f"""
    さぁ、ちょっと冒険してみましょう！
    見つけた食材を使って、驚きと楽しさいっぱいの斬新なフュージョン料理を考えてみましょう。

    以下の情報を含めた、ワクワクするようなレシピを教えてください：
    - インパクトのある面白い料理名
    - 必要な材料と量
    - 誰でも挑戦できる詳しい手順
    - およその費用（※ざっくり計算で大丈夫です）
    - この料理の魅力や楽しいポイント

    使える食材はこちらです：
    {ingredients_text}

    みんなで「わぁ！」と驚けるような、楽しい料理にしましょう！
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a creative and enthusiastic cooking innovator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500
    )
    
    return response.choices[0].message.content

def print_usage():
    """
    使用方法を表示
    """
    print("🍳 レシピジェネレーターの使い方 🍳")
    print("----------------------------------------")
    print("python recipe_generator.py <画像URL>")
    print("\n例えば、こんな感じです：")
    print("python recipe_generator.py https://example.com/food-image.jpg")
    print("\nスーパーのチラシやお料理の写真のURLを指定してくださいね！")

def main():
    # コマンドライン引数をチェック
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
    
    # 画像URLを取得
    image_url = sys.argv[1]
    
    try:
        # 設定を読み込んでOpenAIクライアントを初期化
        config = load_config()
        client = OpenAI(api_key=config['openai']['api_key'])
        
        # 1. 画像から食材リストを抽出
        print("🔍 お買い得な食材を探しています...")
        ingredients = analyze_image(client, image_url)
        print("\n✨ 見つけた食材はこちら！")
        for ingredient in ingredients:
            if ingredient.strip():  # 空行を除外
                print(ingredient)
        
        # 2. 通常のレシピを生成
        print("\n📝 美味しいレシピを考えています...")
        recipes = generate_recipes(client, ingredients)
        print("\n🍽️ おすすめレシピの提案です！")
        print(recipes)
        
        # 3. 奇抜なレシピを生成
        print("\n🎨 斬新なレシピを考えています...")
        creative_recipe = generate_creative_recipe(client, ingredients)
        print("\n🌟 特別なレシピの提案です！")
        print(creative_recipe)
        
        print("\n🎉 以上で完了です！素敵なお料理をお楽しみください！")
        
    except Exception as e:
        print(f"😢 申し訳ありません。エラーが発生しました: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()