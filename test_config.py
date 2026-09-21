import os

names = [
    "RAKUTEN_APPLICATION_ID",
    "RAKUTEN_ACCESS_KEY",
    "RAKUTEN_AFFILIATE_ID",
    "RAKUTEN_KEYWORD",
    "THREADS_USER_ID",
    "THREADS_ACCESS_TOKEN",
]

for name in names:
    value = os.getenv(name)

    if value:
        print(f"{name}: 設定済み")
    else:
        print(f"{name}: 未設定")
