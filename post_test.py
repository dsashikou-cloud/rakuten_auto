import os
import time
import requests


access_token = os.environ["THREADS_ACCESS_TOKEN"]
base_url = "https://graph.threads.com/v1.0"


# 1. アクセストークンから自分のThreads情報を取得
print("Threadsアカウントを確認しています 。")

profile_response = requests.get(
    f"{base_url}/me",
    params={
        "fields": "id,username",
        "access_token": access_token,
    },
    timeout=30,
)

print("プロフィール確認結果:", profile_response.status_code)

if profile_response.status_code != 200:
    print(profile_response.text)
    raise SystemExit(
        "Threadsアカウントの確認に失敗しました。"
        "アクセストークンまたは権限を確認してください。"
    )

profile = profile_response.json()
user_id = profile.get("id")
username = profile.get("username")

if not user_id:
    print(profile)
    raise SystemExit("ThreadsユーザーIDを取得できませんでした")

print(f"Threadsユーザー確認完了: @{username}")


# 2. 投稿用コンテナを作成
text = "Threads APIのテスト投稿です。"

print("投稿用コンテナを作成しています。")

container_response = requests.post(
    f"{base_url}/{user_id}/threads",
    data={
        "media_type": "TEXT",
        "text": text,
        "access_token": access_token,
    },
    timeout=30,
)

print("コンテナ作成結果:", container_response.status_code)

if container_response.status_code != 200:
    print(container_response.text)
    raise SystemExit("投稿用コンテナの作成に失敗しました")

container_id = container_response.json().get("id")

if not container_id:
    print(container_response.text)
    raise SystemExit("コンテナIDを取得できませんでした")


# 3. 少し待ってから公開
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
