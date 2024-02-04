const WebSocket = require('ws');

!(function(){
    window.zhiyuan = (0, h.appendCryptoParams);
    const url = 'ws://127.0.0.1:8080/?source=browser';
    const ws = new WebSocket(url);
    ws.onopen = function(evt){};
    ws.onmessage = function(evt) {
        console.log("接收到node服务端消息:", evt.data);
        var data = window.zhiyuan(evt.data);
        var info = "hk_nonce=" + data["hk_nonce"] + ",hk_sign=" + data["hk_sign"] + ",hk_timestamp=" + data["hk_timestamp"] + ",hk_token=" + data["hk_token"]
        ws.send(info);
    };
})()