# Mission 2 — Understanding Data in Machine Learning

## 1. Introduction

Machine learning systems use data to identify patterns and make predictions. The quality and suitability of the data strongly influence how useful the resulting model will be.

## 2. Important Data Concepts

- **Dataset:** A collection of examples used for analysis or machine learning.
- **Sample or observation:** One individual example or record in a dataset.
- **Feature:** An input property used by a model to make a prediction.
- **Label:** The known answer associated with an example in a labelled dataset.
- **Target:** The outcome a model is intended to predict.

For example, in a dataset of chip-design runs, each row could represent one run. Features might include clock frequency and estimated congestion, while the target could be whether the run passes timing.

## 3. Types of Data

### Structured and Unstructured Data

Structured data is organized into a defined format, such as rows and columns in a table.

Unstructured data does not follow the same simple tabular organization. Examples include images, audio recordings, and free-form text.

### Numerical and Categorical Features

- Numerical features represent quantities, such as delay in nanoseconds or power in milliwatts.
- Categorical features represent groups or types, such as technology node or design category.

### Labelled and Unlabelled Data

Labelled data contains examples paired with known target answers. Unlabelled data contains observations without supplied target labels.

## 4. Illustrative Dataset

The following is a synthetic dataset created for learning purposes. The values are illustrative, not measurements from a real chip-design project.

| Run | Clock Frequency (MHz) | Estimated Congestion (%) | Cell Area (arbitrary units) | Timing Result |
|---|---:|---:|---:|---|
| R1 | 400 | 35 | 120 | Pass |
| R2 | 500 | 62 | 150 | Fail |
| R3 | 350 | 28 | 110 | Pass |
| R4 | 600 | 75 | 180 | Fail |
| R5 | 450 | 42 | 135 | Pass |
| R6 | 550 | 68 | 165 | Fail |

### Identify the Features and Target

- **Dataset:** All six design-run records.
- **Samples:** R1 through R6; each row is one sample.
- **Features:** Clock frequency, estimated congestion, and cell area.
- **Target:** Timing result (Pass or Fail).
- **Task type:** Classification, because the target is a category.

This example illustrates how historical design data might be organized for a supervised learning task. It does not establish that the listed feature values reliably determine timing outcomes.

## 5. Data Quality

### Problem 1: Missing Values

Some design runs may have missing congestion or area measurements. A model may not be able to process these records correctly without suitable handling.

**Possible mitigation:** Investigate why values are missing, then use an appropriate strategy such as correcting the data source, excluding unsuitable records, or imputing values where justified.

### Problem 2: Incorrect or Noisy Labels

A timing result might be labelled Pass when the actual sign-off result is Fail. Incorrect labels can teach a model misleading relationships.

**Possible mitigation:** Check labels against trusted reports and investigate inconsistent records before training.

## 6. Why More Data Does Not Always Mean Better Data

A larger dataset can still be unhelpful if it contains inaccurate measurements, duplicated records, biased examples, or data that does not represent the intended use case.

Useful training data should be relevant, sufficiently representative, consistently labelled where labels are required, and collected with appropriate quality checks.

## 7. Conclusion

Machine learning depends on both the quantity and quality of its data. Understanding samples, features, and targets helps engineers organize a problem correctly. Data preparation and validation are important because errors in the input data can lead to unreliable predictions.

## 8. Sources

Record the reliable sources you actually consult and state what each supports.

Suggested starting point:
- Google Machine Learning Crash Course — https://developers.google.com/machine-learning/crash-course
