# Lecture 4.1 - Modelling and Representation

# Modeling:

### Probabilistic Language Models

```python
Given a sequence of tokens, **predict the next token** 
```

**Naive Bayesian Probability** 

![Screenshot 2024-10-22 at 1.55.08 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_1.55.08_PM.png)

We do this using the token directly before (n=1) the one we are tying to generate we get: 

![Screenshot 2024-10-22 at 1.57.15 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_1.57.15_PM.png)

⇒

![Screenshot 2024-10-22 at 1.57.54 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_1.57.54_PM.png)

### Level 1: Unigram Language Models

- We assume that words occur on its own.
- bad approach because it will just output the most common word

### **Level 2: Bigram**

- we assume that the next token depends directly on the previous token
    
    ![Screenshot 2024-10-22 at 2.01.12 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_2.01.12_PM.png)
    
- read: “probablity of sentence S1 is the **product** of the condition probability of $w_i$ dependent on $w_{i-1}$
    
    ![Screenshot 2024-10-22 at 2.05.23 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_2.05.23_PM.png)
    
    ![Screenshot 2024-10-22 at 2.05.51 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_2.05.51_PM.png)
    

## Maximum likelihood Estimation (MLE)

![Screenshot 2024-10-22 at 2.09.55 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_2.09.55_PM.png)

We can build a table that tracks the number of these occurrences, which gives us a rough starting point of probability table

![Screenshot 2024-10-22 at 2.11.16 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_2.11.16_PM.png)

Along with the count of each word in the corpus (unigram count)

![Screenshot 2024-10-22 at 2.13.30 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_2.13.30_PM.png)

we can calculate the **MLE** of the grid with normalised values:

![Screenshot 2024-10-22 at 2.14.49 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_2.14.49_PM.png)

With this grid, we can now **calculate the probability of a sentence** within this corpus!

### **Issues:**

- No sentences with unseen bigrams will be produced, **because the probability of an unseen bigram is 0. When we do the product of each bigram in a sentence**, any 0 term will automatically make the probability of the entire sentence 0.
    - **Solution - Additive/Laplace Smoothing**
        - When counting occurrences, add a quantity to the number (like 1)
            
            ![Screenshot 2024-10-22 at 2.21.33 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_2.21.33_PM.png)
            
        - Now if all words in the corpus is counted $count(word) + 1$ time, we need to adjust the MLE accordingly
            
            ![Screenshot 2024-10-22 at 2.22.42 PM.png](Lecture%204%201%20-%20Modelling%20and%20Representation%20126224ca354c8045b7f3f2c5481cec70/Screenshot_2024-10-22_at_2.22.42_PM.png)
            
        - $V = size(vocabulary)$
    - Other Solutions:
        - **Jelinek-Mercer, Katz, Witten-Bell, Kneser-Ney** smoothing
        - Point of these solutions is to **distribute probability from high prob events to events with low or no probability.**
            - **To make sure that no combination of words is impossible.**

# Evaluating Language Models:

**“Perplexity” =** inverse probability of the test dataset (normalised by num of words)

- LMs that **minimise** perplexity is the best
    - meaning it has a better chance to generate the test set than LMs with higher perplexity