const WebSocket = require('ws');
const url = require('url');

// 创建 WebSocket 服务器
const wss = new WebSocket.Server({ port: 8080 });

// 保存 Python 客户端和浏览器客户端的连接
const pythonClients = new Set();
const browserClients = new Set();

// 监听连接事件
wss.on('connection', (ws, req) => {
  console.log('新的连接已建立');

  // 解析连接的 URL
  const query = url.parse(req.url, true).query;

  // 判断消息的来源
  const source = query.source;

  // 将客户端连接保存到对应的集合中
  if (source === 'python') {
    pythonClients.add(ws);
  } else if (source === 'browser') {
    browserClients.add(ws);
  }

  // 监听消息接收事件
  ws.on('message', (message) => {
    const receivedMessage = Buffer.from(message).toString('utf8');
    console.log('接收到的消息:', receivedMessage);

    // 根据消息的来源转发消息给特定的客户端
    if (source === 'python') {
      // 转发消息给所有浏览器客户端
      browserClients.forEach((client) => {
        client.send(receivedMessage);
      });
    } else if (source === 'browser') {
      // 转发消息给所有 Python 客户端
      pythonClients.forEach((client) => {
        client.send(receivedMessage);
      });
    }
  });

  // 监听关闭事件
  ws.on('close', () => {
    console.log('连接已关闭');

    // 从对应的集合中移除断开连接的客户端
    if (source === 'python') {
      pythonClients.delete(ws);
    } else if (source === 'browser') {
      browserClients.delete(ws);
    }
  });
});