import socket
import json
import time

point = ("127.0.0.1", 42069) #XSOverlayのポート

#各々の設定
title = input("表示するタイトル: ")
content = input("表示する内容: ")
tick = input("通知する間隔(分): ")

#間隔のintチェック
while not tick.isnumeric():
	print("通知する間隔は数値で入力してください。")
	tick = input("通知する間隔(分): ")

tick = int(tick)
tick = tick*60

while True:
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	data_msg = {
		"messageType": 1,
		"title": title,
		"content": content,
		"height": 120.0,
		"sourceApp": "meru-notify",
		"timeout": 5,
		"volume": 1.0,
		"audioPath": "default",
		"useBase64Icon": False,
		"icon": "",
		"opacity": 1.0,
	}
	msg_str = json.dumps(data_msg)

	sock.sendto(msg_str.encode("utf-8"), point)

	time.sleep(tick)
