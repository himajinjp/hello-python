import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    ]
    return random.choice(user_agents)

# セッションを作成
session = requests.Session()

# より詳細なヘッダー情報
headers = {
    'User-Agent': get_random_user_agent(),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ja,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="91", " Not;A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1'
}

url = "https://www.umitenki.jp/tenki/104/1hour"

# ランダムな待機時間（3-7秒）
time.sleep(random.uniform(3, 7))

try:
    # まずトップページにアクセス
    top_url = "https://www.umitenki.jp/"
    session.get(top_url, headers=headers)
    
    # さらにランダムな待機時間（2-5秒）
    time.sleep(random.uniform(2, 5))
    
    # 目的のページにアクセス
    res = session.get(url, headers=headers)
    res.raise_for_status()
    print(f"Status Code: {res.status_code}")
    print(f"Response Headers: {dict(res.headers)}")
    
    # レスポンスの内容も確認
    print("\nResponse Content Preview:")
    print(res.text[:500])
    
except requests.RequestException as e:
    print(f"エラーが発生しました: {e}")

