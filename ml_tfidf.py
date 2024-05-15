import numpy as np
import pandas as pd
from loguru import logger
import math
from typing import *

doc_a = "I love coding with python python is good"
doc_b = "I love coding with rust rust is fast"

# 拆分文档单词
d_a_words, d_b_words = doc_a.split(" "), doc_b.split(" ")

# 获取所有文档单词的集合
words_set = set(d_a_words).union(set(d_b_words))

# 统计文档中每个单词的数量
a_word_count_dict, b_word_count_dict = dict.fromkeys(words_set, 0), dict.fromkeys(words_set, 0)
for word in d_a_words:
    a_word_count_dict[word] += 1
for word in d_b_words:
    b_word_count_dict[word] += 1

# 计算tf
def compute_tf(word_count_dict: Dict[str, Any], words):
    tf_dict = {}
    words_count = len(words)
    for word, count in word_count_dict.items():
        tf_dict[word] = count / words_count
    return tf_dict

a_tf = compute_tf(a_word_count_dict, d_a_words)
b_tf = compute_tf(b_word_count_dict, d_b_words)
logger.debug(f"单词在每个文档中的频率 a_tf: {a_tf}, b_tf: {b_tf}")

# 计算idf
def compute_idf(word_count_dict_list: List[Dict[str, Any]]):
    # 随便取其中一个，因为都是相同的key
    id_dict = dict.fromkeys(word_count_dict_list[0], 0)
    doc_count = len(word_count_dict_list)
    for word_count_dict in word_count_dict_list:
        for word, count in word_count_dict.items():
            if count > 0:
                id_dict[word] += 1
    idf_dict = {}
    for word, t_count in id_dict.items():
        idf_dict[word] = math.log10((doc_count + 1) / (t_count+1))
    return idf_dict

idf = compute_idf([a_word_count_dict, b_word_count_dict])
logger.debug(f"idf: {idf}")

# 计算tf_idf
def compute_tfidf(tf, idf):
    tfidf = {}
    for word, tf_val in tf.items():
        tfidf[word] = tf_val * idf[word]
    return tfidf

a_tfidf = compute_tfidf(a_tf, idf)
b_tfidf = compute_tfidf(b_tf, idf)
logger.info(f"a_tfidf: {a_tfidf}, b_tfidf: {b_tfidf}")

df = pd.DataFrame([a_tfidf, b_tfidf])
df2 = df[df>0].dropna(axis=1, how="all")
print(df2)
