# 简单工厂模式、工厂模式、单列模式、责任链模式、策略模式、代理模式、适配器模式(实例化、多继承)、发布订阅模式、外观模式、模板模式、建造者模式、组合模式


from abc import ABCMeta, abstractmethod


"""
# 简单工厂模式
class SpiderFactory(object):
    def __init__(self, spider_type) -> None:
        self.spider_type = spider_type

    def create_spider(self):
        if self.spider_type == "image":
            return ImageSpider()
        elif self.spider_type == "video":
            return VideoSpider()
        else:
            raise ValueError("invalid spider type")


class Spider(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

class ImageSpider(Spider):
    def start(self):
        print("start image spider")

class VideoSpider(Spider):
    def start(self):
        print("start video spider")


if __name__ == "__main__":
    image_spider = SpiderFactory("image").create_spider()
    image_spider.start()
    video_spider = SpiderFactory("video").create_spider()
    video_spider.start()

"""

"""
# 工厂模式
class SpiderFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_spider(self):
        pass

class ImageSpiderFactory(SpiderFactory):
    def create_spider(self):
        print("create image spider")
        return ImageSpider()

class VideoSpiderFactory(SpiderFactory):
    def create_spider(self):
        print("create video spider")
        return VideoSpider()

class Spider(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

class ImageSpider(Spider):
    def start(self):
        print("start image spider")

class VideoSpider(Spider):
    def start(self):
        print("start video spider")

if __name__ == "__main__":
    image_spider = ImageSpiderFactory().create_spider()
    image_spider.start()
    video_spider = VideoSpiderFactory().create_spider()
    video_spider.start()

"""

"""
# 单列模式
class SingleInstance(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance
    
class SingleInstance2(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            setattr(cls, "_instance", super().__new__(cls))
        return cls._instance
    
class Test(SingleInstance):
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    print(id(Test()) == id(Test()))

"""
"""
# 责任链模式
class FileHandler(metaclass=ABCMeta):
    @abstractmethod
    def handler(self):
        pass

class BigFileHandler(FileHandler):
    def __init__(self, file_size) -> None:
        self.file_size = file_size

    def handler(self):
        if self.file_size > 500:
            raise ValueError("file is too big")
        else:
            print("big_file_handler dealwith")

class MidFileHandler(FileHandler):
    def __init__(self, file_size) -> None:
        self.file_size = file_size
        self.file_handler = BigFileHandler(self.file_size)

    def handler(self):
        if self.file_size <= 200:
            print("mid_file_handler dealwith")
        elif self.file_size > 200:
            self.file_handler.handler()

class SmallFileHandler(FileHandler):
    def __init__(self, file_size) -> None:
        self.file_size = file_size
        self.file_handler = MidFileHandler(self.file_size)
    
    def handler(self):
        if self.file_size <= 10:
            print("small_file_handler dealwith")
        elif self.file_size > 10:
            self.file_handler.handler()

if __name__ == "__main__":
    file_handler = SmallFileHandler(900)
    file_handler.handler()

"""
"""
# 策略模式
class Spider(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

class RequestSpider(Spider):
    def start(self):
        print("start request spider")

class RPCSpider(Spider):
    def start(self):
        print("start rpc spider")

class SeleniumSpider(Spider):
    def start(self):
        print("start selenium spider")

class Context(object):
    def __init__(self, spider) -> None:
        self.spider = spider

    def change_spider(self, spider):
        self.spider = spider

    def execute_spider(self):
        self.spider.start()

if __name__ == "__main__":
    request_spider = RequestSpider()
    rpc_spider = RPCSpider()
    selenium_spider = SeleniumSpider()
    context = Context(request_spider)
    context.execute_spider()
    context.change_spider(rpc_spider)
    context.execute_spider()
    context.change_spider(selenium_spider)
    context.execute_spider()

"""

"""
# 代理模式
class Spider(object):
    def __init__(self) -> None:
        print("init spider")

    def start(self):
        print("start spider")


class SpiderProxy(object):
    def __init__(self) -> None:
        print("init proxy spider")
        self.spider = Spider()

    def start_spider_record(self):
        print("spider start time")
        self.spider.start()
        print("spider end time")


if __name__ == "__main__":
    spider = SpiderProxy()
    spider.start_spider_record()

"""

"""
# 适配器模式
class Spider(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

class BaiduSpider(Spider):
    def start(self):
        print("start baidu spider")

class SougouSpider(Spider):
    def start(self):
        print("start sougou spider")

class GoogleSpider(object):
    def run(self):
        print("start google spider")


class AdjustGoogleSpider(object):
    def __init__(self) -> None:
        self.google_spider = GoogleSpider()

    def start(self):
        self.google_spider.run()

class AdjustGoogleSpider2(Spider, GoogleSpider):
    def start(self):
        self.run()

if __name__ == "__main__":
    ad_google_spider = AdjustGoogleSpider()
    ad_google_spider.start()
    ad_google_spider2 = AdjustGoogleSpider2()
    ad_google_spider2.start()

"""

"""
# 发布订阅模式
class Node(object):
    def __init__(self, node_name) -> None:
        self.node_name = node_name

    def notice(self, info):
        print(f"{self.node_name} receive master msg: {info}")

class Master(object):
    def __init__(self) -> None:
        self.node_set = set()

    def add_node(self, *args):
        self.node_set.update(*args)

    def remove_node(self, node):
        self.node_set.discard(node)

    def notify(self, info):
        for i in self.node_set:
            i.notice(info)

if __name__ == "__main__":
    node1 = Node("node1")
    node2 = Node("node2")
    master = Master()
    master.add_node((node1, node2))
    master.notify("start task")

"""

"""
# 外观模式
class ImageSpider(object):
    def __init__(self) -> None:
        self.baidu_spider = BaiduSpider()
        self.google_spider = GoogleSpider()
    
    def run(self):
        self.baidu_spider.start()
        self.google_spider.start()


class Spider(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

class BaiduSpider(Spider):
    def start(self):
        print("start baidu spider")
        # todo1
        # todo2
        print("over")

class GoogleSpider(Spider):
    def start(self):
        print("start google spider")
        # todo1
        # todo2
        print("over")

if __name__ == "__main__":
    image_spider = ImageSpider()
    image_spider.run()

"""

"""
# 模板模式
class SpiderTemplate(object):
    def get_index_page(self):
        pass

    def exact_request_url(self):
        pass

    def request_data(self):
        pass

class Spider(SpiderTemplate):
    def get_index_page(self):
        print("get index page")

    def exact_request_url(self):
        print("exact request url")

    def request_data(self):
        print("request data")

if __name__ == "__main__":
    spider = Spider()
    spider.get_index_page()
    spider.exact_request_url()
    spider.request_data()

"""

"""
# 建造者模式
class Role(object):
    def __init__(self) -> None:
        self.face = None
        self.body = None
        self.footer = None

    def set_face(self, face):
        self.face = face

    def set_body(self, body):
        self.body = body

    def set_footer(self, footer):
        self.footer = footer

    def show_role(self):
        print(f"{self.face, self.body, self.footer}")

class buildRole(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_footer(self):
        pass

class Girl(buildRole):
    def __init__(self) -> None:
        self.role = Role()

    def build_face(self):
        self.role.set_face("girl face")
    
    def build_body(self):
        self.role.set_body("girl body")
    
    def build_footer(self):
        self.role.set_footer("girl footer")
    
class Boy(buildRole):
    def __init__(self) -> None:
        self.role = Role()

    def build_face(self):
        self.role.set_face("boy face")
    
    def build_body(self):
        self.role.set_body("boy body")
    
    def build_footer(self):
        self.role.set_footer("boy footer")
    
class Directory(object):
    def __init__(self, build_role) -> None:
        self.build_role = build_role

    def create(self):
        self.build_role.build_face()
        self.build_role.build_body()
        self.build_role.build_footer()
        return self.build_role.role

if __name__ == "__main__":
    girl = Girl()
    directory = Directory(girl)
    role = directory.create()
    role.show_role()

"""

"""
# 组合模式
class Color(metaclass=ABCMeta):
    @abstractmethod
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        return "Filled with red color."

class Blue(Color):
    def fill(self):
        return "Filled with blue color."

class Graph(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

class Circle(Graph):
    def __init__(self, color):
        self.color = color

    def draw(self):
        return f"Drawing circle. {self.color.fill()}"

class Triangle(Graph):
    def __init__(self, color):
        self.color = color

    def draw(self):
        return f"Drawing triangle. {self.color.fill()}"

if __name__ == "__main__":
    red = Red()
    blue = Blue()

    circle = Circle(red)
    print(circle.draw())

    triangle = Triangle(blue)
    print(triangle.draw())

"""



