# Mission 7 — Understand Why ML Systems Fail

## 1. Introduction

Machine learning systems can fail even when they perform well during testing. Common reasons include poor-quality data, incorrect labels, data bias, data leakage and changes in real-world conditions. Human oversight is important because incorrect predictions can have real consequences.

## 2. Failure Case 1 — Poor-Quality Training Data

**Scenario:** A semiconductor company trains a model to predict whether a chip will pass timing checks. Some training records contain missing values and incorrect timing labels.

**Likely cause:** The model learns from incomplete or incorrect examples.

**Evidence to investigate:**
- Check for missing feature values.
- Compare selected labels with trusted timing reports.
- Check whether errors are concentrated in particular data sources.

**Possible mitigation:**
- Validate and clean the dataset.
- Correct labels using reliable engineering reports.
- Document missing data and re-evaluate the model after cleaning.

## 3. Failure Case 2 — Data Leakage

**Scenario:** A model predicts whether a chip will pass timing checks. During training, the dataset accidentally includes information generated only after the timing result is already known. The model achieves excellent test performance but performs poorly when used on new designs.

**Likely cause:** Data leakage. The model has access to information that would not genuinely be available at prediction time.

**Evidence to investigate:**
- Inspect the features and when each feature becomes available.
- Check the data preparation and train/test splitting process.
- Compare performance after removing suspicious features.

**Possible mitigation:**
- Remove information that reveals the answer or would not be available in practice.
- Split data in a way that reflects the intended real-world use.
- Repeat evaluation using a clean, independent test set.

## 4. Failure Case 3 — Changing Real-World Data

**Scenario:** A defect-detection model is trained using images from one manufacturing line. Later, the company changes a camera and lighting setup, and the model begins missing defects.

**Likely cause:** The new data differs from the training data. This is an example of data distribution shift.

**Evidence to investigate:**
- Compare old and new image characteristics.
- Review error rates before and after the equipment change.
- Check performance across different production lines and operating conditions.

**Possible mitigation:**
- Collect representative examples from the updated production setup.
- Re-evaluate and, if necessary, retrain the model.
- Monitor performance over time and involve engineers when predictions are uncertain.

## 5. Bias and Human Oversight

Data bias occurs when the training data does not adequately represent the situations in which a model will be used. Performance may therefore differ across production lines, chip types or operating conditions.

Human oversight is important when incorrect predictions could lead to defective products being accepted or good products being unnecessarily rejected. Engineers should investigate high-risk decisions instead of treating model outputs as automatically correct.

## 6. Summary Table

| Failure | Likely cause | Evidence to check | Mitigation |
|---|---|---|---|
| Poor-quality data | Missing values and incorrect labels | Data quality checks and trusted reports | Clean data and correct labels |
| Data leakage | Unavailable or answer-revealing information | Features and data-splitting process | Remove leakage and test independently |
| Changing data | New conditions differ from training conditions | Data and performance comparisons over time | Monitor, re-evaluate and retrain if needed |

## 7. Conclusion

Reliable machine learning requires more than selecting a model. Engineers must examine data quality, prevent leakage, check for bias, evaluate changing conditions and maintain human oversight. A model should be trusted only to the extent supported by appropriate evidence.

## 8. Sources to consult

- Google for Developers — Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
- Google for Developers — Introduction to Machine Learning: https://developers.google.com/machine-learning/intro-to-ml

I will check the relevant material, verify the concepts and revise this draft in my own words before submission.
