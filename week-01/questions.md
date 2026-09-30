# Week 01 Questions

## Q1 - AI → ML → Deep Learning → Generative AI → Agents


### Answer

#### 1. Artificial Intelligence (AI)

Artificial Intelligence (AI) refers to the area of developing machine-based
systems capable of executing tasks that require capabilities such as learning,
reasoning, perception, planning, communication, and decision-making. AI systems
can be created to make predictions, recommendations or decisions based on predefined
objectives.

**Example from everyday life:** Navigation system that evaluates roads, traffic,
destination, and suggests the best route.

---

#### 2. Machine Learning (ML)

Machine Learning is a subset of Artificial Intelligence where algorithms
learn patterns from the provided data and use those patterns to make predictions
or decisions about new data. In contrast to traditional programming where all rules
must be explicitly specified, machine learning algorithms can learn useful patterns
from the examples.

**Example from everyday life:** Email spam filtering system that learns from
previous emails and makes prediction about whether the new email is spam or not.

---

#### 3. Deep Learning (DL)

Deep Learning is a subset of Machine Learning that uses multilayered
artificial neural networks to learn complex patterns from data.
During training, the model adjusts parameters such as weights and
biases to improve its outputs.

**Everyday example:** A smartphone's image recognition system that
can identify objects or recognize faces in photographs.

---

#### 4. Generative AI

Generative AI is a type of Artificial Intelligence that can create
new content such as text, images, audio, video, or software code in
response to a user's prompt. It commonly uses machine learning and
deep learning models that learn patterns from large amounts of data.

**Everyday example:** ChatGPT generating an explanation, story, or
piece of computer code from a user's prompt.

---

#### 5. AI Agent

An AI agent is a system that can autonomously perform tasks by
planning or designing workflows and using available tools. It can
understand a user's goal, make decisions, interact with external
systems, and take actions to complete a task.

**Everyday example:** An AI travel assistant that searches for
flights and hotels, compares available options, creates an itinerary,
and uses external services to perform actions requested by the user.

---

### Relationship between AI, ML, DL, Generative AI and AI Agents

A simplified relationship can be represented as:

                    ARTIFICIAL INTELLIGENCE
                             |
              +--------------+--------------+
              |                             |
              v                             v
      MACHINE LEARNING              Other AI approaches
              |
              v
       DEEP LEARNING
              |
              | supports many
              v
       GENERATIVE AI
              |
              | can be used as a component of
              v
          AI AGENTS
              |
       +------+------+
       |             |
    Tools         Actions
       |
    External
    systems

AI is the broadest concept. Machine Learning is a subset of AI, and
Deep Learning is a subset of Machine Learning. Many modern Generative
AI systems use deep learning models. AI agents can use Generative AI
models, such as large language models, as part of a larger system that
can plan tasks, use tools, and take actions.

The diagram is a simplified representation and should not be interpreted
as saying that all AI systems are machine-learning systems, that all
deep-learning systems are generative AI systems, or that all AI agents
are generative AI systems.

---

### Generative AI vs AI Agent

Generative AI and AI agents are related but are not the same.

A Generative AI model primarily produces content in response to an
input or prompt. For example, a generative AI model can write an email,
generate an image, summarize a document, or produce computer code.

An AI agent is designed to accomplish a goal or task. It can use an AI
model as part of its system, but it can also plan steps, call external
tools or applications, observe results, make decisions, and perform
actions.

In simple terms:

**Generative AI:** "Create something for me."

**AI Agent:** "Complete this task for me."

Therefore, Generative AI can be a component of an AI agent, but a
Generative AI model by itself is not necessarily an AI agent.

---

### Evidence / Sources

1. National Institute of Standards and Technology (NIST), CSRC
   Glossary — Artificial Intelligence:
   https://csrc.nist.gov/glossary/term/artificial_intelligence

2. IBM Think — What is Machine Learning?
   https://www.ibm.com/think/topics/machine-learning

3. IBM Think — What is Deep Learning?
   https://www.ibm.com/think/topics/deep-learning

4. IBM Think — What is Generative AI?
   https://www.ibm.com/think/topics/generative-ai

5. IBM Think — What are AI Agents?
   https://www.ibm.com/think/topics/ai-agents

These sources were compared to verify the definitions and the
relationships between the concepts.

---

### Verification

I verified the definitions using NIST and IBM technical resources
rather than relying on a single AI-generated explanation.

The sources consistently describe Machine Learning as a subset of AI
and Deep Learning as a subset of Machine Learning. They also describe
Generative AI as systems that can create new content and AI agents as
systems that can perform tasks using workflows, tools, and actions.

One important point I verified is that Generative AI and AI agents
should not be treated as identical concepts. A generative model can
produce content without independently carrying out a multi-step task,
whereas an AI agent can use models and external tools to work toward
a goal.

---

### Reflection

Before researching this topic, I understood AI, Machine Learning,
Deep Learning, and Generative AI as closely related terms but did not
clearly understand how they differ.

The main distinction I learned is that AI is the broad field, Machine
Learning is one approach within AI, and Deep Learning is a machine
learning approach based on multilayered neural networks. Generative AI
focuses on creating new content, while an AI agent focuses more on
achieving a goal by planning steps, using tools, and taking actions.

This helped me understand why simply calling every modern AI system
"Generative AI" is not technically accurate.

## Q2. Is Everything That Looks Intelligent Actually AI?

### Classification

| Case | Scenario | Classification | Reason |
|---|---|---|---|
| A | A calculator produces 25 × 16 = 400. | Deterministic / Traditional Software | The calculator follows explicitly programmed arithmetic rules. It does not learn from data or generate a response based on learned patterns. |
| B | A rule-based program says: If temperature > 80°C, display WARNING. | Deterministic / Traditional Software | The behavior is directly specified by an explicit rule. Whenever the condition is satisfied, the program produces the predefined output. |
| C | An email system identifies a message as spam based on patterns learned from previous email data. | Machine-Learning-Based AI | The system learns patterns from previous data and uses those learned patterns to classify new emails as spam or not spam. |
| D | An AI assistant writes a summary of a document. | Generative AI | The system generates new text based on the content of the document and the user's request. |
| E | A navigation application predicts estimated arrival time using traffic and historical data. | Machine-Learning-Based AI | The system can use traffic and historical data to identify patterns and predict an estimated arrival time for a new journey. |

---

### Reasoning for Each Case

#### A. Calculator

A calculator is an example of deterministic or traditional software. When the user enters `25 × 16`, the calculator applies programmed arithmetic operations and produces `400`. It does not need to learn from previous examples.

#### B. Rule-Based Temperature Warning

This is also deterministic software. The program has an explicitly defined rule:

**If temperature > 80°C → display WARNING**

The same input condition leads to the predefined action. There is no learning from data involved.

#### C. Spam Detection

This is machine-learning-based AI when the spam detector has learned patterns from previous email data. Instead of relying only on manually written rules, the model uses patterns learned during training to classify new messages.

#### D. AI Document Summary

This is generative AI because the system produces new text in response to a request. The assistant processes the document and generates a summary rather than simply following one fixed output rule.

#### E. Navigation Estimated Arrival Time

This can be classified as machine-learning-based AI when the application uses traffic and historical data to predict travel time. The system uses patterns in data to estimate an outcome for a new journey.

---

### What Makes AI Different From Explicitly Programmed Software?

A traditional program can produce intelligent-looking behavior by following rules that humans explicitly specify. This does not automatically make the system an AI system.

A machine-learning-based AI system can learn patterns from data and use those patterns to make predictions, classifications, or decisions for new inputs. Generative AI systems can additionally generate new content based on learned patterns.

Therefore, a system should not be called AI simply because its output appears intelligent. We should consider **how the system produces that output**, particularly whether it uses learned patterns or generative models rather than only explicitly programmed instructions.

---

### Key Takeaway

**Looks intelligent ≠ necessarily AI.**

A calculator and a rule-based warning system can behave predictably and appear useful without using AI. Machine-learning systems learn patterns from data, while generative AI systems can create new content based on learned patterns.

---

## Q3 - What Happens When You Ask an LLM a Question?

### A - Answer

### E - Evidence

### V - Verification

### R - Reflection

---

## Q4 - Hallucination Experiment

### A - Answer

### E - Evidence

### V - Verification

### R - Reflection

---

## Q5 - AI Assistant vs Search vs Authoritative Reference

### A - Answer

### E - Evidence

### V - Verification

### R - Reflection

---

## Q6 - What Is an AI Agent?

### A - Answer

### E - Evidence

### V - Verification

### R - Reflection

---

## Q7 - Where Should Humans Still Make the Decision?

### A - Answer

### E - Evidence

### V - Verification

### R - Reflection

---

## Q8 - Find AI Around You

### A - Answer

### E - Evidence

### V - Verification

### R - Reflection

---

## Q9 - Prediction, Classification, and Generation

### A - Answer

### E - Evidence

### V - Verification

### R - Reflection

---

## Q10 - Personal AI Verification Protocol

### A - Answer

### E - Evidence

### V - Verification

### R - Reflection
