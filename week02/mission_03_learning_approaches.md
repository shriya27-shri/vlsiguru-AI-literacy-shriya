# Mission 3 — Understanding the Main ML Approaches

## 1. Introduction

Machine learning approaches differ in the type of information or feedback used during learning. The main approaches covered here are supervised learning, unsupervised learning, reinforcement learning, and self-supervised learning.

## 2. Supervised Learning

Supervised learning uses training examples containing inputs and known target answers.

**Example:** Predict whether a chip-design run will pass or fail timing using historical measurements.

**Training signal:** Known labels or target values.

**Typical outputs:** A trained model that predicts categories or numerical values.

**Limitation:** The model depends on suitable labelled examples. Incorrect or unrepresentative labels can reduce performance.

## 3. Unsupervised Learning

Unsupervised learning looks for patterns or structure in data without supplied target labels.

**Example:** Group physical-design runs with similar congestion and area measurements.

**Training signal:** Structure and relationships within the input data, rather than provided target answers.

**Typical outputs:** Groups, patterns, or lower-dimensional representations of data.

**Limitation:** The discovered groups may not correspond to useful engineering categories and can require expert interpretation.

## 4. Reinforcement Learning

Reinforcement learning involves an agent taking actions and receiving rewards or penalties based on the results.

**Example:** An experimental system explores design choices and receives a reward based on specified power, performance, and area objectives.

**Training signal:** Rewards or feedback associated with actions and outcomes.

**Typical outputs:** A policy for choosing actions in a given situation.

**Limitation:** Learning may require many trials, and a poorly designed reward can encourage undesirable behaviour.

## 5. Self-Supervised Learning

Self-supervised learning creates training targets from the data itself. For example, a language model may learn to predict a hidden word or the next token in a sequence.

**Training signal:** Targets derived from the input data rather than manually supplied labels for every example.

**Typical outputs:** A model that learns useful patterns or representations from data.

**Limitation:** The learning objective may not fully match the requirements of the final task, so further evaluation or adaptation may be needed.

Self-supervised learning is closely related to unsupervised learning in that it can use unlabelled data, but it creates an explicit training target from that data. The terms are related, not always interchangeable.

## 6. Comparison Table

| Approach | Training signal | Example | Main limitation |
|---|---|---|---|
| Supervised | Known labels or target values | Predict timing Pass/Fail | Needs suitable labelled examples |
| Unsupervised | Structure in unlabelled data | Group similar design runs | Groups may be difficult to interpret |
| Reinforcement | Rewards from actions and outcomes | Explore design choices using a reward | Trials and reward design can be challenging |
| Self-supervised | Targets derived from the data | Predict hidden or next tokens | Training objective may not match the final task |

## 7. Simple Learning Process Diagrams

### Supervised Learning

Labelled examples → Training algorithm → Trained model → Prediction

### Unsupervised Learning

Unlabelled data → Pattern discovery → Groups or representations

### Reinforcement Learning

Agent → Action → Environment → Reward or feedback → Updated behaviour

### Self-Supervised Learning

Raw data → Create training targets from data → Train model → Learned representations

## 8. When Is Each Approach Suitable?

- **Supervised learning:** When historical examples include reliable answers for the outcome we want to predict.
- **Unsupervised learning:** When we want to explore a dataset and discover groups or patterns without known target labels.
- **Reinforcement learning:** When a system must learn a sequence of actions through interaction and meaningful reward feedback.
- **Self-supervised learning:** When large amounts of raw data are available and useful training targets can be generated from that data.

## 9. Conclusion

The learning approach should be selected according to the problem, the available data, and the feedback needed for learning. These approaches are not interchangeable: they differ in their training signals, typical outputs, and limitations.

## 10. Sources

Add reliable sources you actually consult and explain which claims they support.

Suggested starting points:
- Google Introduction to Machine Learning: https://developers.google.com/machine-learning/intro-to-ml
- Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
