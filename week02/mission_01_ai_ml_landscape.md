# Mission 1 — Build the AI and ML Landscape

## 1. Introduction 

Artificial Intelligence (AI) is a broad field focused on building computer systems that perform tasks requiring capabilities such as reasoning, pattern recognition, prediction, or language understanding.

Machine Learning (ML) is a part of AI in which systems learn patterns from data instead of relying only on manually written rules.

## 2. AI, Rule-Based Programming, and Machine Learning

### Artificial Intelligence (AI)
AI is the broad field of creating systems that perform intelligent tasks. Some AI systems use predefined rules, while others use machine learning.

### Rule-Based Programming
In rule-based programming, a developer explicitly writes conditions and actions. For example, a program can flag a timing violation when a measured delay exceeds a specified limit.

### Machine Learning
In machine learning, a system learns patterns from example data. For example, a model could learn from historical chip-design measurements to predict whether a new design run is likely to pass timing.

## 3. Relationship Between AI, ML, Deep Learning, Generative AI, and LLMs

- **AI:** The broad field of intelligent computer systems.
- **Machine Learning:** A family of techniques that learn patterns from data.
- **Deep Learning:** A type of machine learning that uses neural networks with multiple layers.
- **Generative AI:** AI systems that generate new content, such as text, images, or code. They may use different underlying architectures.
- **Large Language Models (LLMs):** Models designed to process and generate language. Many modern LLMs use transformer architectures.

These terms are related, but they do not all describe the same type of thing. Deep learning is an ML approach, generative AI describes a capability, and LLMs are a class of language models.

## 4. Five Important Distinctions

### Distinction 1: AI vs. ML
AI is the broader field, whereas ML is one approach within AI. A rule-based expert system can be an AI system without learning from data.

### Distinction 2: Rule-Based Programming vs. ML
Rule-based programs follow explicitly written conditions. ML models learn patterns from training examples. Rules can be easier to inspect, while ML can be useful when patterns are too complex to specify manually.

### Distinction 3: ML vs. Deep Learning
ML includes many approaches, including decision trees and linear regression. Deep learning is a subset of ML based on multilayer neural networks.

### Distinction 4: Generative AI vs. Predictive ML
Predictive ML may estimate a numerical value or classify an observation. Generative AI creates content, such as a text response or a piece of code. Some generative systems also use predictive learning objectives.

### Distinction 5: LLMs vs. All Generative AI
LLMs focus on language. Generative AI is broader and includes systems that generate images, audio, and other content. Not every generative AI system is an LLM.

## 5. Three Examples and Their Classification

### Example 1: Fixed Timing-Rule Checker
A program checks whether a measured delay exceeds a predefined timing limit.

**Classification:** Rule-based programming.

**Reason:** The condition and threshold are explicitly defined by the developer. The program does not need to learn from historical examples.

### Example 2: Timing-Pass Prediction
A model uses historical design measurements to predict whether a new physical-design run will pass or fail timing.

**Classification:** AI using supervised machine learning; the task is classification.

**Reason:** The model learns from examples containing input measurements and known pass/fail outcomes.

### Example 3: AI Assistant for Explaining Verilog
A language model generates an explanation of a Verilog code snippet.

**Classification:** Generative AI using a large language model.

**Reason:** The system generates natural-language content. Its response may be helpful, but it still needs to be checked for technical correctness.

## 6. Conclusion

AI includes different ways to create intelligent systems. Rule-based programming uses explicitly defined logic, while machine learning uses data to learn patterns. Deep learning is a subset of ML, generative AI creates content, and LLMs specialize in language. Choosing an approach depends on the engineering problem, available data, evaluation requirements, and consequences of errors.

## 7. Sources

Add the links to the resources you actually consult and explain what each source supports. Suggested starting points:

- Google, Introduction to Machine Learning: https://developers.google.com/machine-learning/intro-to-ml
- IBM, What is Machine Learning?: https://www.ibm.com/think/topics/machine-learning

Verify that the pages support the specific claims for which you cite them.
