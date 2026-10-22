# Mission 5 — Understanding the Anatomy of an ML Model

## 1. Introduction

A machine learning system uses data and a learning method to build a model that can make predictions on new inputs. Understanding the difference between an algorithm, a model, training, and inference helps explain how this process works.

## 2. Algorithm, Model, and Parameters

### Algorithm
An algorithm is a method or procedure used to learn patterns from training data.

### Model
A model is the result of the learning process. It represents a learned relationship that can be used to produce predictions.

### Parameters
Parameters are internal values learned during training. They influence how the model converts input features into an output.

For example, a linear regression model learns parameters that determine how input measurements relate to a numerical prediction.

## 3. Training Versus Inference

### Training
During training, a learning algorithm processes training examples and adjusts the model's parameters to improve its predictions according to a learning objective.

### Inference
Inference occurs when a trained model receives an input and produces an output, such as a predicted delay or a Pass/Fail classification.

Training is the learning stage; inference is the stage in which the learned model is used.

## 4. Loss and Optimisation

A loss function measures how far a model's predictions are from the desired answers, according to a chosen measure.

Optimisation is the process of adjusting the model's parameters to improve the objective used during training.

Different algorithms use different learning and optimisation procedures. Reducing training loss alone does not guarantee that the model will perform well on unseen data.

## 5. Labelled Model Flow Diagram

The following flow shows a simplified supervised learning process:

Training examples with features and target answers  
→ Select a learning algorithm  
→ Train the model and adjust parameters  
→ Evaluate the trained model  
→ Use the trained model for inference  
→ Produce a prediction for a new input

Training and evaluation are distinct activities. A model should be evaluated using data appropriate for that purpose before relying on its predictions.

## 6. Linear Regression

Linear regression is a machine learning method used to estimate a numerical outcome from input features.

For example, an engineer might use historical design measurements to estimate the delay of a new design configuration.

During training, the method learns a relationship between the input features and known numerical outcomes. The resulting model can then estimate an outcome for a new input.

The relationship is represented using learned parameters. The prediction is an estimate, not a guarantee of the actual outcome.

## 7. Semiconductor Engineering Example

Suppose an engineering team wants to estimate chip-design delay using historical runs.

- **Input features:** Selected design measurements and configuration details.
- **Training target:** Measured delay from previous runs.
- **Learning method:** Linear regression, if a linear relationship is a reasonable starting point.
- **Trained model:** A learned relationship between the input features and delay.
- **Inference:** Provide measurements for a new run to obtain an estimated delay.
- **Limitation:** The estimate may be inaccurate if the relationship is not sufficiently linear, the data is poor, or the new design differs from the training examples.

## 8. Conclusion

A machine learning algorithm learns from examples to create a model with learned parameters. Training develops the model, while inference uses it to produce predictions. Loss and optimisation help guide training, but the model's usefulness must still be evaluated on appropriate data.

## 9. Sources

Add reliable sources you actually consult and state what each source supports.

Suggested starting points:
- Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
- Google Introduction to Machine Learning: https://developers.google.com/machine-learning/intro-to-ml
