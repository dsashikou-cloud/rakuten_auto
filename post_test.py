import os
import time
import requests

user_id = os.environ["THREADS_USER_ID"]
access_token = os.environ["THREADS_ACCESS_TOKEN"]

base_url = "https://graph.threads.com/v1.0"

text = "Threads APIのテスト投稿です 。"

print("投稿用コンテナを作成しています。")

response = requests.post(
    f"{base_url}/{user_id}/threads",
    data={
        "media_type": "TEXT",
        "text": text,
        "access_token": access_token,
    },
    timeout=30,
)

print("コンテナ作成結果:", response.status_code)

if response.status_code != 200:
    print(response.text)
    raise SystemExit("コンテナ作成に失敗しました")

container_id = response.json().get("id")

if not container_id:
    raise SystemExit("コンテナIDを取得できませんでした")

print("30秒待機します。")
time.sleep(30)

print("Threadsへ公開しています。")

publish_response = requests.post(
    f"{base_url}/{user_id}/threads_publish",
    data={
        "creation_id": container_id,
        "access_token": access_token,
    },
    timeout=30,
)

print("公開結果:", publish_response.status_code)

if publish_response.status_code != 200:
    print(publish_response.text)
    raise SystemExit("Threadsへの公開に失敗しました")

print("テスト投稿が完了しました")
print(publish_response.text)
