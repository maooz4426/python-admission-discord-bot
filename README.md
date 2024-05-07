# 概要
discord　botでサークルの入会管理を出来るようにしたbotです。
GASをAPIとして、discordもモーダルで入力した情報をスプレッドシートに書き込めるようにしています。

# 開発環境
- python 3.12.2 

- pycord 2.5.0

- docker

# envファイルの中身
```
TOKEN = "your_discordbot_token"

URL = "gas_url"

CIRCLE_MEMBER_ROLE_ID = "circle_member_role_id"

OBOG_ROLE_ID= "obog_role_id"
```
