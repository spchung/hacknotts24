# Lecture 5 - Bias 2

The ecosystem of data for AI:

**People ↔ Data ↔ Systems**

Quality of Data:

- **Representativeness**
- coverage
- validity … etc

What can we do about biased data:

- remove from source
- be transparent with your data

**Ecological Validity:**

- the extent of a study or finding can be properly generalised to real-world settings.
- **real** vs **simulated**  situations

**Data Statements:**

- a characterisation of  a dataset that provides context to allow devs to unserstand better
    - what are some potential issues with this dataset and how to properly use it.

**Crowdsourcing**

- usage of labelled data from a group of ppl

**Debiasing biased data:**

example with Word Embedding

- **Hard Debiasing**
    - Removing unwanted associateion
- **Soft Debiasing**
    - Reduces the difference between sets while **maintaining as much similarity to the original embedding as possible**
- **HOWEVER, these techniques do not solve the root of the problem.** it only serves to highlight the bias and not the