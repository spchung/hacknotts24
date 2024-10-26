from collections import defaultdict
from typing import List
from fuzzywuzzy import fuzz
import re

'''
Sample of Fuzzywuzzy library

Matching two strings with slight differences
string1 = "apple pie"
string2 = "applee piee"

Calculate the similarity ratio (0 to 100)
similarity = fuzz.ratio(string1, string2)
print(f"Similarity score: {similarity}")
'''


class CommonUtils:
    @staticmethod
    def fuzzy_search(query: str, query_range) -> List[str]:
        # return the list of top 3 most probably candidates
        similarity_dict = defaultdict(float)
        for term in query_range:
            similarity_dict[term] = fuzz.ratio(query, term)
        similarity_dict = sorted(similarity_dict.items(), key=lambda x: x[1], reverse=True)
        return [i[0] for i in similarity_dict][:3]

    @staticmethod
    def regex_search(pattern: str, query_range) -> List[str]:
        ans = set()
        for term in query_range:
            ans = ans.union(re.findall(pattern, term))
        return list(ans)


def test_fuzzy_search():
    assert (CommonUtils.fuzzy_search('apple', ['apple', 'this is an app', 'apple pie', 'appple', 'nothing related']) ==
            ['apple', 'appple', 'apple pie'])


def test_regex_search():
    assert ((sorted(
        CommonUtils.regex_search(query_range=["Please contact us at support@example.com or sales@example.org."],
                                 pattern=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"))) ==
            ['sales@example.org', 'support@example.com'])
