# Coursework

### Question recognition:

- Sents with “?” or starts with “what” “how” “can you”
- intent:
    - POV isolation → get all verbs and nouns
    - pipe (verb, noun) into similarity search

### Similarity Search:

- use output of Question recog to search a term-doc similarity
    - produce a most likely structured query