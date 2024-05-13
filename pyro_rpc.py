# 服务端代码
import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message: None of the above."

daemon = Pyro4.Daemon()
uri = daemon.register(GreetingMaker)

print("Ready. Object uri =", uri)

# 创建一个名字服务器
ns = Pyro4.locateNS(host="127.0.0.1", port=5002)
ns.register("example.greeting", uri)

daemon.requestLoop()



# 客户端代码
import Pyro4

# 根据服务的名称查找 URI
uri = Pyro4.locateNS(host="127.0.0.1", port=5002).lookup("example.greeting")

greeting_maker = Pyro4.Proxy(uri)
print(greeting_maker.get_fortune("Simon"))
