# Lecture 8 - Validation

### K-fold cross Validation:

- split training data into K sections
    - for each k/N we use **k-1 sections for training** and **k for validation** and rotate until all sections have been used to validate

### Evaluation Metrics (Evaluation) [TESTED] [NO EQUATION]

![Screenshot 2024-10-25 at 11.31.55 AM.png](Lecture%208%20-%20Validation%2012a224ca354c80b0950efc16ac57c1d6/Screenshot_2024-10-25_at_11.31.55_AM.png)

- **Classification accuracy: (TP+TN)/(TP+FP+FN+TN)**
- Balanced classification accuracy = (Sensitivity + Specificity) / 2

### Precision and Recall:

- **Precision - TP/(TP+FP)**
    - percentage of correct predictions among predicted positive predictions
- **Recall  - TP/(TP+FN)**
    - percentage of correct positive predictions among all real positive cases
- **Sensitivity = Recall and Specificity = TN/(TN+FP)**

### F Measure

- A Measurement that combines Precision and Recall
- $B$ as beta term [0,1]

- Because $B$ is a multiplier of P. The greater B is the less P matters and vice versa.

![Screenshot 2024-10-25 at 11.43.48 AM.png](Lecture%208%20-%20Validation%2012a224ca354c80b0950efc16ac57c1d6/Screenshot_2024-10-25_at_11.43.48_AM.png)

### ROC (Receiver Operator Characteristic) Curve

- ##? Decision Threshold

## Regression Evalutation Metrics

- MSE
    - squared to magnify large errors
- RootMSE
    - punishes large errors like MSE while retaining the original unit
- Mean Absolute Error
    - retains original unit but changes into linear

## Statistical Testing

issue: sample data will never represent the whole population

- **T Test:**
    - how the mean of two groups are diff **(Assuming norm distribution)**
    - null-hypothesis: the two means are the same
    - check the P value
        - if p_val < 0.05 then **singnificant**
- **Wilconxon signed-reank test**
    - non-parametric, does not have to be gaussian distribution

## Confidence Interval