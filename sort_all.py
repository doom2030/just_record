from typing import List


def bubble_sorted(ls: List[int]) -> List[int]:
    """
    冒泡排序,遍历n-1趟,每趟比较前后两个元素值,交换位置
    每趟将一个最大(最小值)移动到尾端,待排序序列长度每次减1
    稳定排序,时间复杂度0(n**2),空间复杂度O(1)
    :param ls:
    :return:
    """
    for i in range(len(ls) - 1):
        for j in range(len(ls) - i - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
    return ls


def choose_sorted(ls: List[int]) -> List[int]:
    """
    选择排序,遍历n-1趟,每趟将待排序序列的第一个索引值默认为最大(最小)值
    依次比较后面的元素,获得最大(最小)位置的索引并和第一个索引值进行调换
    将最大(最小)元素移动到前端位置,待排序序列减1
    稳定排序,时间复杂度O(n**2),空间复杂度O(1)
    :param ls:
    :return:
    """
    for i in range(len(ls) - 1):
        min_idx = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[min_idx]:
                min_idx = j
        ls[i], ls[min_idx] = ls[min_idx], ls[i]
    return ls


def insert_sorted(ls: List[int]) -> List[int]:
    """
    插入排序,默认第一个索引元素的值为已排序序列,依次遍历待排序序列,
    将待排序序列和已排序序列中的值进行比较,插入到合适的位置,已排序序列
    依次向后移动位置
    稳定排序,时间复杂度O(n**2),空间复杂度O(1)
    :param ls:
    :return:
    """
    for i in range(1, len(ls)):
        cur = ls[i]
        pre_idx = i - 1
        while cur < ls[pre_idx] and pre_idx >= 0:
            ls[pre_idx+1] = ls[pre_idx]
            pre_idx -= 1
        ls[pre_idx+1] = cur
    return ls


def shell_sorted(ls: List[int]) -> List[int]:
    """
    希尔排序,插入排序的优化方案,通过设置一个gap值,将序列
    分为多个序列,每个序列进行局部的插入排序,达到每个序列的局部有序
    最后将gap值置为1,进行一次全局的插入排序
    不稳定排序,时间复杂度O(nlogn),空间复杂度O(1)
    :param ls:
    :return:
    """
    gap = 3
    while gap >= 1:
        for i in range(gap, len(ls)):
            cur = ls[i]
            pre_idx = i - gap
            while cur < ls[pre_idx] and pre_idx >= 0:
                ls[pre_idx+gap] = ls[pre_idx]
                pre_idx -= gap
            ls[pre_idx+gap] = cur
        gap //= 2
    return ls


def merge_sorted(ls: List[int]) -> List[int]:
    """
    归并排序,递归分组,左右序列的比较排序
    不稳定排序,时间复杂度O(nlogn),空间复杂度O(n)
    :param ls:
    :return:
    """
    if len(ls) <= 1:
        return ls
    left_ls = ls[:len(ls) // 2]
    right_ls = ls[len(ls) // 2:]
    return merge(merge_sorted(left_ls), merge_sorted(right_ls))


def merge(left_list: List[int], right_list: List[int]) -> List[int]:
    res_ls = []
    while left_list and right_list:
        if left_list[0] < right_list[0]:
            res_ls.append(left_list.pop(0))
        else:
            res_ls.append(right_list.pop(0))
    while left_list:
        res_ls.append(left_list.pop(0))
    while right_list:
        res_ls.append(right_list.pop(0))
    return res_ls


def quick_sorted(ls: List[int]) -> List[int]:
    """
    快速排序,通过递归分组进行排序
    不稳定排序,时间复杂度O(nlogn),空间复杂度O(logn)
    :param ls:
    :return:
    """
    if len(ls) <= 1:
        return ls
    mid_val = ls[0]
    left_ls, mid_ls, right_ls = [], [], []
    for val in ls:
        if val < mid_val:
            left_ls.append(val)
        elif val == mid_val:
            mid_ls.append(val)
        else:
            right_ls.append(val)
    return quick_sorted(left_ls) + mid_ls + quick_sorted(right_ls)


def heapify_sorted(ls: List[int]) -> List[int]:
    """
    1. 建立大根堆(小根堆),第一个父节点为开始节点,比较子节点值大小交换位置
    2. 反向遍历序列,将堆顶元素和堆底元素进行互换,获取堆顶的最大值(最小值),
    排序序列长度减一
    不稳定排序,时间复杂度O(nlogn),空间复杂度O(1)
    :param ls:
    :return:
    """
    for i in range(len(ls) // 2 - 1, -1, -1):
        max_heapify(ls, i, len(ls) - 1)

    arr_len = len(ls)
    for j in range(len(ls)-1, 0, -1):
        ls[j], ls[0] = ls[0], ls[j]
        arr_len -= 1
        max_heapify(ls, 0, arr_len)
    return ls


def max_heapify(arr: List[int], begin_idx: int, end_idx: int) -> List[int]:
    """
    建立大根堆
    :param arr:
    :param begin_idx:
    :param end_idx:
    :return:
    """
    large_idx = begin_idx
    left_idx = begin_idx * 2 + 1
    right_idx = begin_idx * 2 + 2
    if left_idx < end_idx and arr[left_idx] > arr[large_idx]:
        large_idx = left_idx
    if right_idx < end_idx and arr[right_idx] > arr[large_idx]:
        large_idx = right_idx
    if large_idx != begin_idx:
        arr[large_idx], arr[begin_idx] = arr[begin_idx], arr[large_idx]
        return max_heapify(arr, large_idx, end_idx)


def count_sorted(ls: List[int]) -> List[int]:
    """
    计数排序,获取序列最大值,生成一个有序的可包容所有元素的列表,
    将序列的值和列表的下标索引相对应,依次遍历列表,取出元素即可
    不稳定排序,时间复杂度O(n+k),空间复杂度O(n+k)
    :param ls:
    :return:
    """
    max_val = max(ls)
    count_ls = [0 for _ in range(max_val+1)]
    for val in ls:
        count_ls[val] += 1
    res_ls = []
    for i in range(len(count_ls)):
        for j in range(count_ls[i]):
            res_ls.append(i)
    return res_ls


def bucket_sorted(ls: List[int]) -> List[int]:
    """
    桶排序,将序列按照大小范围放入相应的桶内,进行各自排序,最后依次从
    桶中取出元素即可
    1.获取序列最大值, 最小值
    2.设置桶内元素数量的大小
    3.将一定范围内的元素放入相应桶内
    不稳定排序,时间复杂度O(n+k),空间复杂度O(n+k)
    :param ls:
    :return:
    """
    max_val, min_val = max(ls), min(ls)
    bucket_size = len(ls)
    bucket_num = (max_val - min_val) // bucket_size + 1
    bucket_ls = [[] for _ in range(bucket_num)]
    for val in ls:
        bucket_ls[(val - min_val) // bucket_size].append(val)
    res_ls = []
    for bucket in bucket_ls:
        sorted_bucket = sorted(bucket)
        res_ls.append(sorted_bucket)
    return [n for m in res_ls for n in m]


def base_sorted(ls: List[int]) -> List[int]:
    """
    基数排序,获取序列最大值的位数,按位数进行遍历次数的排序
    不稳定排序,时间复杂度O(n+k),空间复杂度O(n)
    :param ls:
    :return:
    """
    bit_num = len(str(max(ls)))
    base = 10
    for i in range(bit_num):
        base_ls = [[] for _ in range(10)]
        for val in ls:
            base_ls[(val // base**i) % base].append(val)
        ls = [n for m in base_ls for n in m]
    return ls


if __name__ == "__main__":
    sort_ls = [32, 17, 69, 20, 13, 27, 50, 49, 8, 44, 28, 36, 49]
    print(bubble_sorted(sort_ls))
    print(choose_sorted(sort_ls))
    print(insert_sorted(sort_ls))
    print(shell_sorted(sort_ls))
    print(merge_sorted(sort_ls))
    print(quick_sorted(sort_ls))
    print(count_sorted(sort_ls))
    print(bucket_sorted(sort_ls))
    print(base_sorted(sort_ls))
    print(heapify_sorted(sort_ls))

