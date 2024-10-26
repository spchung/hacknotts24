# Lecture 4 - models

## **Linear Algos:**

Linear Regression; Logistic Regression; Naive Bayes; Support Vector Machine (SVM;

## **Non-Linear Algos:**

K Nearest Neighbours; Kernel SVM; Decision Trees; Neural Networks;

### Term: “Linear Separable”

- where a data set with x labels can be separated cleanly by a decision surface (or line), which implies **no class-overlap.**
- **Rare**

### Parametric vs Non-Parametric Algos:

**Parametric algos** assumes that data follows a specific distribution in its features or have a deterministic relationshiop between features and outcomes.

**Parametric:**

- linear regression (follows *a* and *b* to graph decision line)
- gaussian naive bayes (assumes points are centered)
- ma likelihood classifier

**Non** **Parametric:**

- Decision Trees (no assumption)
- Neural Networks

### Overfitting & Underfitting

- over-fit: where the decision boundary is too closely related to the training data (achieve perfect accuracy on training data)
- under-fit: where decision boundary is too general and have low accuracy on training data

### Variance and Bias

- Bias - how far away are you from the target
- variance - **the amount that** **the estimate of the target function will change given different training data**
    
    ![Screenshot 2024-10-16 at 2.58.19 PM.png](Lecture%204%20-%20models%20121224ca354c800cb021f36c2b857bab/Screenshot_2024-10-16_at_2.58.19_PM.png)
    

### Intrinsic Params vs Hyper Params:

- Intrinsic
    - learned efficiently on the training set
    - large in number
    - e.g. weights in linear regression and NN
- Hyper
    - must be learned through **generalisation error**
    - no efficient search - something that we find using **trial and error through validation sets.**
    - smaller in number
    - e.g. number of nodes in an ANN or the **weights of two terms** in a loss function (learning rate)

### **Univariate vs Multivariate Linear Regression**

**Univariate** - only one independent variable

- using one label X to predict the independent variable Y
- e.g. Predicting a person’s weight based on height alone.

**MultiVariate -** use n independent variables

- each label Xn will be assigned a weight
- is the linear sum of the multiplication of each of the features with their corresponding weight terms
    
    ![Screenshot 2024-10-16 at 3.19.46 PM.png](Lecture%204%20-%20models%20121224ca354c800cb021f36c2b857bab/Screenshot_2024-10-16_at_3.19.46_PM.png)
    

Comparison:

![Screenshot 2024-10-16 at 3.20.59 PM.png](Lecture%204%20-%20models%20121224ca354c800cb021f36c2b857bab/Screenshot_2024-10-16_at_3.20.59_PM.png)

## #? Linear Classification (Logistic Regression)

- Provides probabilities of new sample’s classification with a number between 0 to 1
- Logistic function aka [**sigmoid function**](https://en.wikipedia.org/wiki/Sigmoid_function)
    
    ![Screenshot 2024-10-16 at 3.26.56 PM.png](Lecture%204%20-%20models%20121224ca354c800cb021f36c2b857bab/Screenshot_2024-10-16_at_3.26.56_PM.png)
    
- altering the values of W0 and W1 will alter the curve of the decision boundary

## Multinomial Naive Bayes

![Screenshot 2024-10-16 at 3.48.09 PM.png](Lecture%204%20-%20models%20121224ca354c800cb021f36c2b857bab/Screenshot_2024-10-16_at_3.48.09_PM.png)

- “what is the prob of event A depending on event B
- Case Spam email detection:
    - calculate the probability of selected words appearing in **Normal** or **Spam** emails

## Gaussian Naive Bayes

case: predicting if you’ll pass a course based on study hours, math marks, and number of missed lectures

- **Convert data into gaussian distribution**
    - for students who failed and passed course
        - calculate a distribution of each group using the three features
            
            ![Screenshot 2024-10-16 at 4.07.36 PM.png](Lecture%204%20-%20models%20121224ca354c800cb021f36c2b857bab/Screenshot_2024-10-16_at_4.07.36_PM.png)