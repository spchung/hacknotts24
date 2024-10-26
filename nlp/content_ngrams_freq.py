import os
import strip_markdown
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from pprint import pprint

# nltk.download("stopwords")

dir_path = os.path.join("nlp", "CS MSc 10a224ca354c80df988cc2782f81a45a", "Human-AI 111224ca354c80208ccdf1d4e30914ac")
file_content = ""

def get_content(file_path):
    content = ""
    with open(file_path, "r", encoding="utf8") as f:
        for line in f:
            content += line

    return content


for file in os.listdir(dir_path):
    if file.endswith(".md"):
        file_path = os.path.join(dir_path, file)
        file_content += get_content(file_path)

file_content_strip = strip_markdown.strip_markdown(file_content).lower()
file_tokens = word_tokenize(file_content_strip)

file_token_sw = []
for word in file_tokens:
    if word not in stopwords.words() and word.isalpha():
        file_token_sw.append(word)

bigram = list(ngrams(file_token_sw, 2))
trigram = list(ngrams(file_token_sw, 3))

unigram_freq = nltk.FreqDist(file_token_sw)
bigram_freq = nltk.FreqDist(bigram)
trigram_freq = nltk.FreqDist(trigram)

print("Unigram Frequencies:", str(unigram_freq.most_common(5)))
print("Bigram Frequencies:", str(bigram_freq.most_common(5)))
print("Trigram Frequencies:", str(trigram_freq.most_common(5)))

bigram_terms = []
for bigram, count in bigram_freq.items():
    if count > 1:
        term = bigram[0] + " " + bigram[1]
        bigram_terms.append(term)

result = []
for file in os.listdir(dir_path):
    if file.endswith(".md"):
        file_path = os.path.join(dir_path, file)
        current_file = get_content(file_path)
        current_file_strip = strip_markdown.strip_markdown(current_file).lower()
        file_summary = {
            'file': file,
            }
          
        current_row = []
        for term in bigram_terms:
            count = current_file_strip.count(term)
            current_row.append((term, count))
        file_summary["row"] = current_row
        result.append(file_summary)


pprint(result)
pprint(len(result))