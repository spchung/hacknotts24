# Lecture 2 - NLP

**Definitions:**

- “Natural Language” → languages that developed naturally over time.

**Mass Data Collection:**

- mass data enables translation and other language process features

**NLU →** natural language **understanding**

- human give instruction to computer in natural language

**NLG → Natural language generation:**

- Machine to human communication in natural language
- Generate from:
    - natural lang → user query to machine generated response
    - structured data →

**Advances in speech recognition**

- benefitted the revival of natural language interfaces
    - no longer limited to text based interface

## **NLP Development:**

1. Rule based system
    1. use regex 
    2. text classification using lexicons
    3. conditions extracted elements and tules to build dynamically generated reports
2. **Machine learning**
    1. machine learning methods but came with bias issues
3. **Deep learning**
    1. convolutional networks (started with images)
    2. Recurrent Neural Networks
    3. Transformers models
    4. LLM

# NLP Pipeline

definitions:

`document`  

- a unit of interest for the purpose of analysis
    - e.g. a book, a chapter in a book, a paragraph, a tweet
    - it really depends on the NLP program your working with

`corpus`

- A collection of documents of interest
    - e.g. The Glutenburg project lib (list of books), an arbitrary subset of an exist corpus

**Steps:**

1. **Tokenisation**
    1. a doc is made of tokens
    2. tokens could be any length
        1. could be multi words or single letters
            1. e.g. if we care about spelling - **chars as tokens**
            2. if we care about speech recognition - **syllables as tokens**
2. Annotation
    1. **aka Part of Speech annotation**
        1. must adapt to the languages being analysed
3. Lemmatisation or Stemming
    1. `inflection` - when a word is modified to modify the meaning
    
    ```
    definition:
    
    The inflection of verbs is called conjugation,
    and one can refer to the inflection of nouns, adjectives, adverbs, pronouns, determiners,
    participles, prepositions and postpositions, numerals, articles etc., as declension.
    ```
    
    b. **Lemmatisation -** reduce to dictionary form (the lemma)
    
    - dogs Dog dog → “dog”
    - produces consistent content but is **computationally expensive and slow**
    - often requires POS tagging first
    
    c. **Stemming -** reduce terms to their word stem (the common part its inflections)
    
    - programming → program
    - programmer → prgramm
    - often create **words that don’t exist** but is much faster
4. **Step word filtering**
    1. Not all words matter
        1. common words and rare words can mean very little
    2. use a **stop-list** of words for those to exclude
    
    ![Screenshot 2024-10-21 at 3.26.48 PM.png](Lecture%202%20-%20NLP%20126224ca354c80b7a950f39cdd9ae2b3/Screenshot_2024-10-21_at_3.26.48_PM.png)