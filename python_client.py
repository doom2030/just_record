import websocket
from loguru import logger
import time
import re
import requests

class PythonClient(object):
    def __init__(self) -> None:
        # WebSocket 连接 URL
        self.url = 'ws://127.0.0.1:8080/?source=python'
        # 连接到 WebSocket 服务器
        self.ws = websocket.create_connection(self.url)


    # 定义消息发送函数
    def send_message(self, msg):
        logger.debug("发送到node服务端消息: %s" % msg)
        self.ws.send(msg)

    # 定义消息接收函数
    def receive_message(self):
        msg_ls = []
        try_num = 0
        while True:
            if try_num >= 3:
                break
            msg = self.ws.recv()
            logger.debug('接收到node服务端消息: %s' % msg)
            msg_ls.append(msg)
            try_num += 1
        # self.ws.close()
        return str(msg_ls)


def get_encrypt_data(pc):
    # pc = PythonClient()
    now_time = int((time.time() * 1000))
    # now_time = 1707015648790
    pc.send_message(str(now_time))
    time.sleep(3)
    data = pc.receive_message()
    logger.success("data: %s" % data)
    data_ls = eval(data)
    data_info_ls = []
    for data in data_ls:
        dict_info = {}
        for i in data.split(","):
            dict_info[i.split("=")[0]] = i.split("=")[1]
        dict_info["time"] = now_time
        logger.info("dict_info: %s" % dict_info)
        data_info_ls.append(dict_info)
    return data_info_ls

def request_data(data_info_list):
    for dict_info in data_info_list:
        url = f'https://haokan.baidu.com/haokan/ui-web/video/feed?time={dict_info["time"]}&hk_nonce={dict_info["hk_nonce"]}&hk_timestamp={dict_info["hk_timestamp"]}&hk_sign={dict_info["hk_sign"]}&hk_token={dict_info["hk_token"]}'
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "BAIDUID=206D0791FD617386AA28C2780626AC60:FG=1; BAIDUID_BFESS=206D0791FD617386AA28C2780626AC60:FG=1; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1706755781; ab_sr=1.0.1_NTMzMDk0M2MwNzFmYTJhMzU5NzZjYjE5OTZmM2MyYjBlODUzODkxYjNmYWM3ZWVlOWI5ZWRmNzQxMDVhMjZmNzkzZGEwMWU5ZjEwMDJmZjIwZGMxZDc4MTY2ZmE4NWI4ZDI4NGYzZmI0OWJiYzRjOGMwZTZjODcxYWExMjY3YmU4YmU5YzJkYWYxOTUzYTJmYTRkOTMyNDAzNzllZThjZg==; reptileData=%7B%22data%22%3A%222e8b2d1862f97a2f9921e35053f669b94bdbb39926dc00bb1baffd0f619530b4832b64842797f4d7d3baeb426149d14fb14943f1ab42c4966dba5be6a6a7716095d46999a5ac29f46140ec53501f0a2c8c545ea73a1d9660710f9b1f73f3f5b7%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22d69fd5be%22%7D; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1707015649",
            "Referer": "https://haokan.baidu.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        resp = requests.get(url=url, headers=headers)
        json_data = resp.json()
        if json_data["status"] == 0:
            logger.info("json_data: %s" % json_data)
            logger.success("请求成功了, dict_info: %s" % dict_info)
            break
        else:
            logger.error("请求失败了, dict_info: %s" % dict_info)




if __name__ == "__main__":
    pc = PythonClient()
    try:
        while True:
            encrypt_info = get_encrypt_data(pc)
            request_data(encrypt_info)
            time.sleep(6)
    except KeyboardInterrupt as e:
        print("exit")
