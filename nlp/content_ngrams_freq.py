import os
import strip_markdown
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from pprint import pprint
import DatabaseUtils
from Entities.Doc_Term_Map import DocTermMap

# nltk.download("stopwords")

dir_path = os.path.join("nlp", "CS MSc 10a224ca354c80df988cc2782f81a45a", "Human-AI 111224ca354c80208ccdf1d4e30914ac")
file_content = ""

def get_content(file_path):
    content = ""
    with open(file_path, "r", encoding="utf8") as f:
        for line in f:
            content += line

    return content

def build_page_to_bigram_map(pages_raw_text, docs):
    raw_text = "\n".join(pages_raw_text)
    file_tokens = word_tokenize(raw_text)

    file_token_sw = []
    for word in file_tokens:
        if word not in stopwords.words() and word.isalpha():
            file_token_sw.append(word)

    bigram = list(ngrams(file_token_sw, 2))
    # trigram = list(ngrams(file_token_sw, 3))

    # unigram_freq = nltk.FreqDist(file_token_sw)
    bigram_freq = nltk.FreqDist(bigram)
    # trigram_freq = nltk.FreqDist(trigram)

    # print("Unigram Frequencies:", str(unigram_freq.most_common(5)))
    print("Bigram Frequencies:", str(bigram_freq.most_common(5)))
    # print("Trigram Frequencies:", str(trigram_freq.most_common(5)))

    bigram_terms = []
    for bigram, count in bigram_freq.items():
        if count > 1:
            term = bigram[0] + " " + bigram[1]
            bigram_terms.append(term)

    page_to_page_bigram = []
    # raw_text = DatabaseUtils.get_raw_text_from_db()
    # docs = DatabaseUtils.list_docs()
    for doc in docs:
        current_row = []
        file_summary = {
            'file_id': doc.uuid,
        }
        for term in bigram_terms:
            count = doc.doc_content.count(term)
            current_row.append((term, count))
        file_summary["bigrams"] = current_row
        page_to_page_bigram.append(file_summary)
    
    return page_to_page_bigram

def build_relationshiop(page_to_page_bigram):
    # find document pairs with same bigrams
    
    doc_to_term_freq = []
    for i in range(len(page_to_page_bigram)):
        page_id = page_to_page_bigram[i]['file_id']
        bigrams = page_to_page_bigram[i]['bigrams']
        for term, freq in bigrams:
            doc_to_term_freq.append(
                DocTermMap(doc_id=page_id, term=term, term_freq=freq)
            )
    return doc_to_term_freq