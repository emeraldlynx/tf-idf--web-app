import collections
import math
import re
from django.template.defaulttags import IfChangedNode
import pandas as pd

def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text

def compute_idf(word, corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

def compute_tf_idf(words):
    columns = ['Word', 'TF', 'TFIDF']

    tf = compute_tf(words).most_common(50)
    tf_idf = pd.DataFrame(columns=columns)

    for word_stat in tf:
        rows = [[*word_stat, word_stat[1] * compute_idf(word_stat[0], words)]]
        temp_df = pd.DataFrame(rows, columns=columns)
        tf_idf = tf_idf.append(temp_df, ignore_index=True)

    tf_idf_sorted = tf_idf.sort_values(columns[2], ascending=False, ignore_index=True)
    return tf_idf_sorted


def separate_text(text: str) -> list[str]:
    words = re.findall('([а-яА-Яa-zA-Z]+)',  text)
    words = list(map(lambda word: word.lower(), words))
    return words
