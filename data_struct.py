from typing import List, Any
from collections import deque


class Stack(object):
    """
    栈: 后进先出 LIFO
    列表实现栈
    """
    def __init__(self):
        self.stack = []

    def push(self, val: Any) -> bool:
        """
        进栈
        :param val:
        :return:
        """
        self.stack.append(val)
        return True

    def pop(self) -> Any:
        """
        出栈
        :return:
        """
        if not self.is_empty():
            return self.stack.pop()
        return -1

    def get_top(self) -> Any:
        """
        取栈顶
        :return:
        """
        return self.stack[-1]

    def is_empty(self) -> bool:
        """
        栈空
        :return:
        """
        return self.stack == []

    def deep(self) -> int:
        """
        栈深
        :return:
        """
        return len(self.stack)


class SimpleQueue(object):
    """
    简单队列: 先进先出 FIFO
    列表实现
    """
    def __init__(self, max_size=10) -> None:
        self.max_size = max_size
        self.simple_queue = []

    def is_full(self) -> bool:
        """
        队满
        :return:
        """
        return len(self.simple_queue) == self.max_size

    def is_empty(self) -> bool:
        """
        队空
        :return:
        """
        return len(self.simple_queue) == 0

    def push(self, val: Any) -> bool:
        """
        入队
        :param val:
        :return:
        """
        if not self.is_full():
            self.simple_queue.append(val)
            return True
        return False

    def pop(self) -> Any:
        """
        出队
        :return:
        """
        if not self.is_empty():
            return self.simple_queue.pop(0)
        else:
            return False

    def length(self) -> int:
        """
        队列长度
        :return:
        """
        return len(self.simple_queue)


class CircleQueue(object):
    """
    环形队列: 节省空间
    """
    def __init__(self, size: int = 10) -> None:
        self.head = 0
        self.tail = 0
        self.size = size
        self.circle_queue = []
        self.length = 0

    def is_empty(self) -> bool:
        return self.tail == self.head

    def is_full(self) -> bool:
        return (self.tail + 1) % self.size == self.head

    def length(self) -> int:
        return self.length

    def push(self, val: Any) -> bool:
        if not self.is_full():
            self.circle_queue.append(val)
            self.length += 1
            self.tail = (self.tail + 1) % self.size
            return True
        return False

    def pop(self) -> any:
        if not self.is_empty():
            val = self.circle_queue.pop(0)
            self.head = (self.head + 1) % self.size
            return val
        return False


class PrimaryQueue(object):
    """
    优先级队列,value值带优先级别(value, level)
    """
    def __init__(self, max_size: int = 10) -> None:
        self.max_size = max_size
        self.primary_queue: List[tuple] = []

    def push(self, val: Any, level: int) -> bool:
        self.primary_queue.append((val, level))
        sorted(self.primary_queue)
        return True

    def pop(self) -> Any:
        return self.primary_queue.pop(0)


class DoubleQueue(object):
    """
    双端队列,两个列表组成,左列表，右列表
    3 4 5 6 7 8
    """
    def __init__(self, init_list: List[Any] = None) -> None:
        self.init_list = init_list
        if self.init_list is None:
            self.left_list = []
            self.right_list = []
        self.left_list = self.init_list[:len(self.init_list) // 2]
        self.right_list = self.init_list[len(self.init_list) // 2:]

    def append(self, val: Any) -> bool:
        self.right_list.append(val)
        return True

    def pop(self) -> Any:
        return self.right_list.pop()

    def append_left(self, val: Any) -> bool:
        self.left_list.insert(0, val)
        return True

    def pop_left(self) -> Any:
        return self.left_list.pop(0)

    def length(self) -> int:
        if not self.left_list and not self.right_list:
            return 0
        if not self.left_list:
            return len(self.left_list)
        if not self.right_list:
            return len(self.right_list)
        if self.left_list and self.right_list:
            return len(self.left_list) + len(self.right_list)


class Node(object):
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SimpleLink(object):
    """
    简单链表
    """
    def __init__(self) -> None:
        self.head = None

    def append(self, node: Node) -> None:
        if self.head is None:
            self.head = node
        cur: Node = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def pop(self) -> Any:
        if self.head is None:
            raise 'not any element'
        cur: Node = self.head
        before_cur = None
        while cur.next is not None:
            before_cur = cur
            cur = cur.next
        before_cur.next = None
        del cur

    def insert(self, idx: int, node: Node) -> None:
        pass


class CircleLink(object):
    """
    循环链表
    末尾元素的next不再指向None,而是指向head
    """
    pass


class DoubleNode(object):
    def __init__(self, val: Any):
        self.val = val
        self.next = None
        self.before = None


class DoubleLink(object):
    """
    双向链表
    前节点有指针指向后一个节点
    后节点有指针指向前一个节点
    """
    def __init__(self) -> None:
        self.head = None

    def append(self, node: DoubleNode) -> None:
        pass

    def pop(self) -> Any:
        pass

    def insert(self, idx, node: DoubleNode) -> None:
        pass


class DoubleCircleLink(object):
    """
    双向循环链表
    head前指针指向尾部的节点
    尾部节点的next指针指向head节点
    """
    pass


class MaxHeapify(object):
    """
    大根堆
    """
    def __init__(self) -> None:
        self.heapify_container = []

    def heapify(self, arr, begin, end):
        large_idx = begin
        left_idx = begin // 2 - 1
        right_idx = begin // 2 - 2

        if large_idx < end and left_idx > large_idx:
            large_idx = left_idx

        if large_idx < end and right_idx > large_idx:
            large_idx = right_idx

        if large_idx != begin:
            arr[large_idx], arr[begin] = arr[begin], arr[large_idx]
            return self.heapify(arr, large_idx, end)

    def to_heapify(self):
        for i in range(len(self.heapify_container) // 2 - 1, -1, -1):
            self.heapify(self.heapify_container, i, len(self.heapify_container) - 1)


class MinHeapify(object):
    """
    小根堆
    """
    def __init__(self) -> None:
        self.heapify_container = []


    def heapify(self, arr, begin_idx, end_idx):
        min_idx = begin_idx
        left_idx = begin_idx * 2 + 1
        right_idx = begin_idx * 2 + 2

        while left_idx < end_idx and arr[left_idx] < arr[min_idx]:
            min_idx = begin_idx
        while right_idx < end_idx and arr[right_idx] < arr[min_idx]:
            min_idx = right_idx
        if min_idx != begin_idx:
            arr[min_idx], arr[begin_idx] = arr[begin_idx], arr[min_idx]
            self.heapify(arr, min_idx, end_idx)

    def to_heapify(self):
        for i in range(len(self.heapify_container)// 2 -1, -1, -1):
            self.heapify(self.heapify_container, i, len(self.heapify_container)-1)


class BlancTree(object):
    """
    平衡二叉树
    """
    pass


class BlancSearchTree(object):
    """
    二叉搜索树
    """
    pass


class RedBlackTree(object):
    """
    红黑树
    """
    pass

class TableGraph(object):
    """
    基于字典 邻接表实现图
    """
    def __init__(self) -> None:
        """
        self.info = {
            "v1": {
                "v2": 100,
                "v3": 200
            },
            "v2": {
                "v4": 150,
                "v5": 120
            }
        }
        """
        self.info = {}

    def add_vertix(self, v):
        if v in self.info.keys():
            raise "当前节点已存在"
        self.info[v] = {}


    def add_edge(self, from_v, to_v, value):
        if from_v not in self.info.keys():
            self.add_vertix(from_v)
        if to_v not in self.info.keys():
            self.add_vertix(to_v)
        if to_v in self.info[from_v].keys():
            raise "当前节点边已存在"
        self.info[from_v][to_v] = value


    def remove_vertix(self, v):
        if v not in self.info.keys():
            raise "当前顶点不存在"
        del self.info[v]
        for val in self.info.values():
            if v in val.keys():
                del val[v]
        

    def remove_edge(self, from_v, to_v):
        if from_v not in self.info.keys():
            raise "开始顶点不存在"
        if to_v not in self.info.keys():
            raise "结束顶点不存在"
        if to_v not in self.info[from_v].keys():
            raise "结束顶点不在开始顶点关系中"
        del self.info[from_v][to_v]

    def get_vertix_to_edges(self, vertix):
        if vertix not in self.info.keys():
            raise "顶点不存在"
        return self.info[vertix]

    def get_all_vertix(self):
        if not self.info:
            return None
        return self.info.keys()

    def get_all_edges(self):
        edges = []
        if self.info:
            for key, value in self.info.items():
                for k, v in value.items():
                    edge_item = (key, k, v)
                    edges.append(edge_item)
        return edges

    def len_vertix(self):
        return len(self.info.keys())

    def len_edges(self):
        return len(self.get_all_edges)


class Graph(object):
    """
    邻居矩阵实现无向图
    """
    def __init__(self, point_num) -> None:
        self.point_num = point_num
        self.matrix = [[0]*self.point_num for _ in range(self.point_num)]

    def add_edge(self, begin_point, end_point, value):
        if begin_point < 0 or begin_point > self.point_num or end_point < 0 or end_point > self.point_num:
            raise ValueError("索引异常")
        self.matrix[begin_point][end_point] = value
        self.matrix[end_point][begin_point] = value

    def remove_dege(self, begin_point, end_point):
        if begin_point < 0 or begin_point > self.point_num or end_point < 0 or end_point > self.point_num:
            raise ValueError("索引异常")
        self.matrix[begin_point][end_point] = 0
        self.matrix[end_point][begin_point] = 0


    def add_point(self):
        num = len(self.matrix)
        for line in self.matrix:
            line.append(0)
        self.matrix.append([0 for _ in num+1])

    def remove_point(self):
        self.matrix.pop()
        for line in self.matrix:
            line.pop()


class DirectGraph(object):
    """
    邻接矩阵实现有向图
    判断有向无向( 只要有一项matrix[i][j] != matrix[j][i] 就是有向, 如果所有的matrix[i][j] == matrix[j][i]就是无向)
    """
    def __init__(self, point_num) -> None:
        self.point_num = point_num
        self.matrix = [[0]*self.point_num for _ in range(self.point_num)]

    def add_edge(self, begin_point, end_point, value):
        if begin_point < 0 or begin_point > self.point_num or end_point < 0 or end_point > self.point_num:
            raise ValueError("索引异常")
        self.matrix[begin_point][end_point] = value

    def remove_edge(self, begin_point, end_point):
        if begin_point < 0 or begin_point > self.point_num or end_point < 0 or end_point > self.point_num:
            raise ValueError("索引异常")
        self.matrix[begin_point][end_point] = 0

    def add_point(self):
        for line in self.matrix:
            line.append(0)
        num = len(self.matrix)
        self.matrix.append([0 for _ in range(num+1)])

    def remove_point(self):
        self.matrix.pop()
        for line in self.matrix:
            line.pop()




