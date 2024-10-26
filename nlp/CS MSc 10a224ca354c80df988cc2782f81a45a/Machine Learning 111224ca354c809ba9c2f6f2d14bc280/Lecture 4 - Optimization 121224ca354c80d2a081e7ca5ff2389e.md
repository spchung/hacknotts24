# Lecture 4 - Optimization

**PCA Review:**

- considered a **Linear Method**
- In a space with many features we can use PCA to find the dominant features in the space and get rid of less important features.
- We can do this by using
    - maximum variance
    - minimize average projection error
- **Drawback:**
    - To use PCA, the dataset **needs to be in the shape of a gaussian/normal distribution**, aka most points will have to be in the center of the space
        
        ![Screenshot 2024-10-16 at 1.40.24 PM.png](Lecture%204%20-%20Optimization%20121224ca354c80d2a081e7ca5ff2389e/Screenshot_2024-10-16_at_1.40.24_PM.png)
        
        ![Screenshot 2024-10-16 at 1.41.06 PM.png](Lecture%204%20-%20Optimization%20121224ca354c80d2a081e7ca5ff2389e/Screenshot_2024-10-16_at_1.41.06_PM.png)
        
    - **ELSE** the covariance method will not be able to fit the data and reduce features

## Manifold Learning (DR):

Intuition: high-dimensional datasets often vary due to only a small number of parameters. 

- “manifold learning algorithms attempt to map the data from high-dimensional space to a lower-dimensional manifold while maintaining relationships between points in the data.”

**A Dimensionality Reduction method Used for Non-linear distributed datasets**

**Why do we need this:**

- case: Swiss roll data set with PCA
    
    ![Screenshot 2024-10-16 at 1.46.59 PM.png](Lecture%204%20-%20Optimization%20121224ca354c80d2a081e7ca5ff2389e/Screenshot_2024-10-16_at_1.46.59_PM.png)
    
- If simply apply PCA, we will not get a good representation

**With Manifold Learning:**

![Screenshot 2024-10-16 at 2.26.50 PM.png](Lecture%204%20-%20Optimization%20121224ca354c80d2a081e7ca5ff2389e/Screenshot_2024-10-16_at_2.26.50_PM.png)

- #?? Question:
    - Is the lower 4 just the result of arbitrarily removing features?