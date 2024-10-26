# Lecture 6 -Supervised Non-linear 2

# Decision Tree for Classification:

**Supervised Tree-like representation** of a training dataset

Can handle **Regression** and C**lassification**

- **Decision node:** contain condition to split data
- Leave node: contain group of data and the associated label that share similar characteristics

### Binary Decision Trees:

1. Root R - contains the complete dataset
2. Find the **best feature (attribute)** using **Attribute Selection Measure (ASM)** to form a decision node.
3. divide R into subsets using the best feature and best condition
4. for each subset find best feature using AD< to split data again
5. repeat 2-4 until exit conditions are met (all data in branch belong in same class, value diff in each node are small enough)
    
    ![Screenshot 2024-10-18 at 11.17.24 AM.png](Lecture%206%20-Supervised%20Non-linear%202%20123224ca354c80e5aed9d13d55592914/Screenshot_2024-10-18_at_11.17.24_AM.png)
    

At each decision node: 

- Only one criteria on **one feature** can be used (so only horizontal and vert lines in 2D space)

### **ASM - selecting the best feature at each decision node [TESTED]**

- **“Entropy” -** measures uncertainty
    - if all data belong to same class, entropy = 0
    - Therefore, we will choose the **“best feature”** as the that gives the two result (after split) node the lowest entropy value.
- “**Information gain” [TODO] [TESTED]**
    - 
    - we want to maximise this value

#? how to choose feature and how to find the optimal threshold value at each decision node

# Decision Tree for Regression

- use variance as ASM
    
    ![Screenshot 2024-10-18 at 11.39.59 AM.png](Lecture%206%20-Supervised%20Non-linear%202%20123224ca354c80e5aed9d13d55592914/Screenshot_2024-10-18_at_11.39.59_AM.png)
    
- **use average of final leaf node as the predicted value**

# Random Forest

HyperParam:

- num of trees

Decision is made based on the aggregation of different **variety** of trees.

- one tree might not be sufficient but having a shit ton of trees might

**How to build: [TODO]**

Assume 1000 Samples (N), 100 Features (F), 500 trees (B)

**Bagging: [TODO]**

**Random Subspace: [TODO]**

### Feature Importance in RandForest (FS kinda)

- **Permutation Importance + Mean Decrease in Accuracy (MDA)**
    - Choose a feature and randomly assign values to sample:
        - predict again with tree and compare the final accuracy
    - **og_predict** - prediction based on pre-permutation (correct) training set
    - **p_predict** - prediction based on permutated training set (random bullshit prediction)
    - **If Diff(p_perdict, og_perdict) is not very big then this feature is probably not very good**