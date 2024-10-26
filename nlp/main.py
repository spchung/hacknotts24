import nltk
from nltk import word_tokenize, pos_tag
import markdown
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('maxent_ne_chunker_tab')
# nltk.download('words')



file = open('nlp/notes/Lecture 5 - Bias 2 11f224ca354c80a1a659cab0d9d7de84.md', 'r')

markdownHtml = markdown.markdown(file.read())

# markdown to raw text
# replace all tags with empty string
text = markdownHtml.replace('<p>', '').replace('</p>', '')

# use NER detection
# text = file.read()
# for sent in nltk.sent_tokenize(text):
#     for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#         if hasattr(chunk, 'label'):
#             print(chunk.label(), ' '.join(c[0] for c in chunk))