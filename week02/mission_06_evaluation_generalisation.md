# Mission 6 — Understand Evaluation and Generalisation

## 1. Why do we evaluate an ML model?

Model evaluation helps us determine whether a model makes useful predictions on data it has not seen before. A model that performs well on its training data may still make poor predictions on new examples.

## 2. Training, validation and test datasets

- **Training set:** The data used to teach the model and learn its parameters.
- **Validation set:** The data used during development to compare models and tune settings.
- **Test set:** A separate set used to estimate how well the final model performs on unseen data.

The test set should not be repeatedly used to tune the model, because this can make the evaluation misleading.

## 3. Generalisation, overfitting and underfitting

- **Generalisation:** The ability of a model to perform well on new, unseen data.
- **Overfitting:** The model learns details or noise in the training data too closely and performs poorly on new data.
- **Underfitting:** The model is too simple or has not learned enough to capture important patterns, so it performs poorly even on the training data.

Training performance can differ from unseen-data performance because new examples may contain patterns, noise or situations that the model did not learn well.

## 4. Common evaluation metrics

- **Accuracy:** The proportion of all predictions that are correct.
- **Precision:** Among the examples predicted as positive, the proportion that are actually positive.
- **Recall:** Among all actual positive examples, the proportion the model correctly identifies.
- **False positive:** The model predicts positive when the true answer is negative.
- **False negative:** The model predicts negative when the true answer is positive.
- **Absolute error:** The size of the difference between a numerical prediction and its actual value, ignoring whether the difference is positive or negative.

The best metric depends on the problem. Missing a serious defect may be more costly than raising an unnecessary warning, so accuracy alone may not be enough.

## 5. Worked example: When accuracy is misleading

Imagine a dataset containing 1,000 manufactured chips:

- 990 chips pass inspection.
- 10 chips have a defect.

Suppose a model predicts that every chip will pass.

- Correct predictions: 990
- Incorrect predictions: 10
- Accuracy: 990 / 1,000 = 99%
- Recall for defective chips: 0 / 10 = 0%

Although the model has 99% accuracy, it fails to identify any defective chips. This demonstrates why accuracy can be misleading when classes are imbalanced.

**A useful additional metric is recall for the defective class**, because it measures the proportion of actual defective chips that the model catches. Precision is also useful when we need to understand how many flagged chips are genuinely defective.

## 6. Why use a simple baseline?

A baseline is a simple method used as a point of comparison. In this example, predicting that every chip passes already achieves 99% accuracy. A more useful model should be assessed on whether it identifies defects reliably, not just whether it achieves a high accuracy score.

## 7. Semiconductor engineering connection

For chip-defect detection, a false negative could allow a defective chip to be missed, while a false positive could cause a good chip to be flagged for additional inspection. Engineers should choose evaluation metrics based on the cost and consequences of these errors.

## 8. Sources to consult

- Google for Developers — Introduction to Machine Learning: https://developers.google.com/machine-learning/intro-to-ml
- Google for Developers — Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course

I will check the relevant sections of these sources and revise this explanation in my own words before submitting it.
