# Mission 4 — Understanding ML Task Types

## 1. Introduction

Machine learning task types describe the kind of problem a model is expected to solve. The task type is different from the learning approach: a task describes the intended output, while the learning approach describes how the system learns.

## 2. Six Main ML Task Types

### 1. Classification

Classification predicts a category or class.

**Semiconductor example:** Predict whether a physical-design run will pass or fail timing.

- Input: Design measurements and configuration.
- Output: Pass or Fail.

### 2. Regression

Regression predicts a numerical value.

**Semiconductor example:** Estimate the delay of a design from its characteristics.

- Input: Design measurements and configuration.
- Output: Predicted delay in nanoseconds.

### 3. Clustering

Clustering groups observations according to similarities in their features, without requiring predefined target labels.

**Semiconductor example:** Group design runs with similar area and congestion measurements.

- Input: Measurements from multiple design runs.
- Output: Groups of similar runs.

### 4. Anomaly Detection

Anomaly detection identifies observations that differ substantially from expected patterns.

**Semiconductor example:** Flag an unusual measurement from a manufacturing process.

- Input: Process measurements or design-run data.
- Output: An anomaly score or an unusual/normal flag.

### 5. Dimensionality Reduction

Dimensionality reduction represents data using fewer dimensions while attempting to preserve useful information.

**Semiconductor example:** Simplify a dataset containing hundreds of design measurements so engineers can explore patterns.

- Input: A dataset with many features.
- Output: A lower-dimensional representation.

### 6. Recommendation or Ranking

Recommendation or ranking orders or suggests candidates according to a defined objective.

**Semiconductor example:** Rank candidate design configurations for further investigation based on estimated performance and area.

- Input: Candidate configurations and relevant measurements.
- Output: An ordered list of candidates.

## 3. Task Comparison Table

| Task | Input | Expected output |
|---|---|---|
| Classification | Design features | Pass/Fail category |
| Regression | Design features | Numerical delay estimate |
| Clustering | Unlabelled measurements | Groups of similar runs |
| Anomaly detection | Process measurements | Anomaly flag or score |
| Dimensionality reduction | Many numerical features | Fewer dimensions |
| Recommendation/ranking | Candidate configurations | Ordered candidates |

## 4. Learning Approach Versus Task Type

Learning approach and task type answer different questions.

- **Learning approach:** How does the model learn? Examples include supervised, unsupervised, and reinforcement learning.
- **Task type:** What result is the model expected to produce? Examples include classification, regression, clustering, and ranking.

For instance, a model can use supervised learning for classification when it learns from design examples with known Pass/Fail outcomes. Another model can use supervised learning for regression when it learns from examples with known numerical delay values.

Clustering is commonly used as an unsupervised task. The appropriate learning method depends on the problem formulation and available training signal.

## 5. Six Real-World Problems and Their Classification

1. **Email spam detection**
   - Task: Classification.
   - Input: Email characteristics.
   - Output: Spam or not spam.

2. **House-price estimation**
   - Task: Regression.
   - Input: Property characteristics.
   - Output: Estimated price.

3. **Customer segmentation**
   - Task: Clustering.
   - Input: Customer attributes.
   - Output: Groups of similar customers.

4. **Unusual manufacturing sensor readings**
   - Task: Anomaly detection.
   - Input: Sensor measurements.
   - Output: Anomaly score or flag.

5. **Simplifying a dataset with hundreds of measurements**
   - Task: Dimensionality reduction.
   - Input: High-dimensional data.
   - Output: A smaller set of dimensions.

6. **Ranking chip-design configurations**
   - Task: Recommendation/ranking.
   - Input: Candidate design configurations and measurements.
   - Output: Ranked candidates for further testing.

## 6. Conclusion

The correct task type depends on the output required by the problem. Engineers should identify whether they need a category, numerical estimate, group, anomaly flag, simplified representation, or ranked list before selecting a suitable learning approach.

## 7. Sources

Add links to reliable sources that you actually consult and state which claims they support.

Suggested starting point:
- Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
