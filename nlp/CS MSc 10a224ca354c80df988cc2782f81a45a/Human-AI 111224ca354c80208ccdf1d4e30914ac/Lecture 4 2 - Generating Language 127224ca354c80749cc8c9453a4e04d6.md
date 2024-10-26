# Lecture 4.2 - Generating Language

### Goals of any NLG system:

1. Produce understandable texts in the corpus language
2. construct texts with context that meets the specified communicative goals (answer the right questions)

### School of thoughts:

**Template Based - low error rate and** **low novelty**

- Gap filling → use variables for predefined sentences
- Rule-based → gap filling with if else
- Grammatical functions → use grammar n shit

**Dynamic Based - high novelty and high error rate**

- abstract representation of knowledge and fully dynamic generation

### Goal

- take data and generate natural sounding sentences.

### Stages of Template-based NLG:

1. content determination - what should we put in the text
2. Document Structuring - order of information, and grouping of sentences
3. Lexicon choice - the content words we use depend on genre, context, perception
4. Referring expression generation - creation of expressions referring to entities. e.g.”Paul went to the cafe. He was hungry”
5. Aggregation - merging syntactic or conceptual constituents
    1. e.g. Paris is warm. London is warm. → Paris and London are warm.
    2. e.g. Saturday and Sunday → The Weekend.
6. Realisation - building the actual output