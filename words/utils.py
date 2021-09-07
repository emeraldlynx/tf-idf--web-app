import collections
import math
import re
import pandas as pd

class TFIDF:
    @staticmethod
    def apply(text: str) -> dict:
        '''
        Return table in dict with keys 'Word', 'TF', 'TFIDF' and indecies list.
        '''
        words = TFIDF.separate_text(text)
        words_stats = TFIDF.compute_tf_idf(words)[:50].to_dict()
        indecies = list(range(len(words_stats['Word'])))

        return {'words_stats': words_stats, 'indecies': indecies}

    @staticmethod
    def compute_tf_idf(words):
        columns = ['Word', 'TF', 'TFIDF']

        tf = TFIDF.compute_tf(words).most_common(50)
        tf_idf = pd.DataFrame(columns=columns)

        for word_stat in tf:
            rows = [[*word_stat, word_stat[1] * TFIDF.compute_idf(word_stat[0], words)]]
            temp_df = pd.DataFrame(rows, columns=columns)
            tf_idf = tf_idf.append(temp_df, ignore_index=True)

        tf_idf_sorted = tf_idf.sort_values(columns[2], ascending=False, ignore_index=True)
        return tf_idf_sorted

    @staticmethod
    def compute_tf(text):
        tf_text = collections.Counter(text)
        for i in tf_text:
            tf_text[i] = tf_text[i]/float(len(text))
        return tf_text

    @staticmethod
    def compute_idf(word, corpus):
        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

    @staticmethod
    def separate_text(text: str) -> list[str]:
        words = re.findall('([а-яА-Яa-zA-Z]+)',  text)
        words = list(map(lambda word: word.lower(), words))
        return words
