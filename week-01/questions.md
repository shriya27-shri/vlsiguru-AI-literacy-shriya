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

## Q3. What Happens When You Ask an LLM a Question?

### What Happens After a User Submits a Prompt?

When a user asks a question to a Large Language Model (LLM), the
question is first treated as a prompt. The prompt is converted into
smaller units called tokens. The model processes these tokens together
with the available context and uses patterns learned during training
to predict what token is likely to come next.

The model does not generate the entire answer at once. It repeatedly
predicts and selects the next token, adds that token to the generated
sequence, and then uses the updated context to predict the following
token. This process continues until the response is complete.

---

### Key Terms

#### 1. Prompt

A prompt is the input provided by the user to the language model. It
can be a question, instruction, request, or other text that tells the
model what the user wants.

**Example:**

"What is a transistor?"

This complete question is the user's prompt.

#### 2. Token

A token is a unit of text that the language model processes. A token
may represent a whole word, part of a word, punctuation, or another
piece of text, depending on the tokenizer.

For example, a sentence such as:

"AI is useful."

may be divided into several tokens rather than being treated as one
single piece of text.

#### 3. Context

Context is the information available to the model while generating a
response. It can include the user's prompt and, in a conversation,
relevant earlier messages.

The context helps the model determine what the current response should
be about and how the generated text should relate to the input.

#### 4. Probability

The model assigns probabilities to possible next tokens. These
probabilities represent how likely different tokens are to follow the
tokens that have already been processed.

The model then uses these probabilities to select a token according to
the generation method being used.

#### 5. Next-Token Prediction

Next-token prediction is the basic generation process used by
autoregressive language models. Given the current sequence of tokens,
the model predicts which token is likely to come next.

After a token is selected, it becomes part of the sequence and the
model predicts the next token again.

This process is repeated until the response is complete.

#### 6. Generated Response

The generated response is the sequence of tokens produced by the
model during the generation process. The tokens are converted back
into readable text and presented to the user.

---

### Simple Flow Diagram

```text
User Prompt
     |
     v
  Tokenization
     |
     v
    Tokens
     |
     v
Model processes tokens + context
     |
     v
Probability distribution
for possible next tokens
     |
     v
Next-token selection
     |
     v
Selected token added to context
     |
     +--------------------+
     |                    |
     |  Predict next token|
     +---------<----------+
              |
              v
    Generated Response

```

## Q4. Hallucination Experiment: Can AI Sound Confident and Still Be Wrong?

### Experiment Question

**In scan-based DFT, what is the difference between the shift operation and the capture operation? Explain the roles of Scan In (SI), Scan Out (SO), the scan clock, and the capture clock, and describe what happens to the test data during each operation.**

I asked the same question to two different AI assistants and compared their responses with independent DFT references.

### AI Response Comparison

| Model  | Response Summary                                                                                                                                                                                                               | Verified Claim                                                                                                                                          | Evidence                           | Result         |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------------- |
| Gemini | Explained scan flip-flops, SI/SO, scan clock, scan enable, shift, capture, and the shift-in/capture/shift-out sequence.                                                                                                        | The core description of shifting test data through a scan chain and capturing the circuit response is supported by DFT references.                      | Cadence and Synopsys DFT resources | Mostly correct |
| Claude | Explained scan flip-flops using a scan multiplexer, SE-controlled shift/capture modes, SI/SO, scan clock, capture clock, and the shift-in/capture/shift-out sequence. It also discussed stuck-at and transition-fault testing. | The core scan-chain and shift/capture explanation is supported. Some additional timing claims go beyond the question and require separate verification. | Cadence and Synopsys DFT resources | Mostly correct |

### Verification of Important Claims

#### 1. Shift operation

Both AI responses correctly explained that the scan chain allows test data to be shifted serially through scan flip-flops. SI provides the serial scan data input and SO provides the serial scan output. During shifting, clock pulses move data from one scan cell to the next.

Synopsys describes traditional scan architectures as using a scan clock for shifting tester data through internal scan chains. Cadence documentation also identifies SI and SO as scan inputs and outputs and SE as the scan-enable signal.

#### 2. Capture operation

Both AI responses correctly explained that after a test pattern has been shifted into the scan chain, the circuit is placed in the appropriate capture mode so that the response of the functional logic can be captured in the scan flip-flops.

This is consistent with the scan test sequence described by Synopsys: after scan data is shifted in, functional clocks are applied to the design, after which the flip-flops return to shift mode so the captured results can be shifted out.

#### 3. Scan Enable

Claude explicitly explained the role of the scan-enable signal and described the common convention of SE=1 for shift and SE=0 for capture.

This is a common active-high implementation, but the polarity should not be treated as universal because the exact test configuration can vary between designs.

#### 4. A subtle difference between the answers

Gemini described the scan chain as being "temporarily disabled" during capture. This wording is an oversimplification. A more precise description is that the scan flip-flops remain part of the scan architecture, while the scan-enable control selects the functional data path rather than the serial scan path during capture.

Claude's explanation using the scan multiplexer provides a more structurally precise description of this behavior.

### Result

Neither AI produced a completely incorrect answer. Both correctly described the fundamental difference between shift and capture operations.

However, the experiment identified an important issue: an answer can be broadly correct while still using imprecise wording or adding technical claims that require additional verification.

The Gemini response used the phrase "scan chain is temporarily disabled," which can be misleading if interpreted literally. Claude gave a more detailed explanation of the scan multiplexer and scan-enable behavior.

Claude also introduced additional claims about stuck-at testing, transition faults, and at-speed capture. These claims were not necessary to answer the original question, so they should be treated as separate technical claims rather than automatically accepted.

### Reflection

This experiment showed me that hallucination testing does not always mean finding an obviously wrong answer. Both AI systems produced technically reasonable explanations, but comparing them with independent DFT references revealed differences in precision and scope.

The main lesson is that an AI answer can sound confident and technically detailed while still containing wording that needs clarification. In engineering, I should therefore verify important technical claims instead of judging an answer only by how clear or confident it sounds.

For DFT topics, this is especially important because small differences in terms such as scan enable, shift mode, capture mode, and clock behavior can affect how the actual test operation is understood.

---

## Q5. Comparing AI, Web Search, and an Authoritative Reference

### Technical Question

**Why is scan compression used in DFT, and how does it reduce test data volume compared with an uncompressed scan architecture?**

I used the same technical question with AI assistants and then compared their explanations with information available from semiconductor EDA companies and DFT documentation.

### 1. AI Assistant Response

The AI explanations described scan compression as a technique used to reduce the amount of test data and test time required for large designs.

The main idea was that a small number of external tester channels can feed a larger number of internal scan chains through a **decompressor**, while a **compactor** combines responses from multiple internal scan chains before sending them back through a smaller number of tester channels.

This allows the internal scan chains to be shorter and reduces the amount of data that must be transferred between the tester and the chip.

### 2. Web Search Findings

Web searches for scan compression from established semiconductor EDA companies supported the main explanation.

Synopsys describes DFT compression as addressing increasing **test data volume, test time, and the number of test pins** required for testing complex designs. Its TestMAX DFT solution includes scan chains and compression as part of its DFT flow.

Cadence describes a DFT architecture containing **compressor/decompressor logic and scan chains**. Its Modus DFT solution includes scan compression and ATPG capabilities.

### 3. Authoritative Reference

A Synopsys DFTMAX compression document explains that compression architectures use codec/compression logic to reduce **test application time and test data volume**, while working with a limited number of test I/O channels. It also explains that compression ratios affect scan-chain length and test-time reduction.

Therefore, the authoritative reference supports the main AI explanation that scan compression trades additional on-chip DFT logic for reduced test-data volume, shorter effective scan chains, and reduced test time.

### 4. Comparison

| Method                          | Accuracy                                                        | Explanation                                          | Traceability                                                      | Ease of Verification                                                    |
| ------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------- |
| AI assistant                    | Good for the basic concept, but individual claims need checking | Very easy to understand and gives intuitive examples | Lower unless sources are provided                                 | Easy for basic concepts, but important claims need independent checking |
| Web search                      | Depends on the sources selected                                 | Provides multiple explanations and viewpoints        | Better because the original webpages can be identified            | Good when reliable technical sources are selected                       |
| Authoritative/primary reference | Strong for documented technical claims                          | May be more detailed and less beginner-friendly      | High because the original organization/document can be identified | Best for verifying specific engineering claims                          |

### 5. What I Learned

The three methods serve different purposes.

**AI assistants** are useful for quickly understanding a difficult DFT concept and getting a beginner-friendly explanation. However, an AI-generated explanation should not automatically be treated as authoritative.

**Web search** is useful for finding multiple sources and locating documentation, application notes, technical articles, and explanations from semiconductor companies.

**Authoritative references** are particularly useful when I need to verify an engineering claim. For this question, Synopsys and Cadence documentation provided direct evidence that scan compression is used to reduce test-data volume and test time and to work with limited test I/O.

### Conclusion

For learning a new DFT concept, I found AI useful for producing a quick and understandable explanation. However, for confirming whether a technical statement is actually supported, an authoritative reference is more traceable.

This experiment showed that the most reliable workflow is not necessarily to choose only one method. AI can help explain the concept, web search can help locate relevant sources, and authoritative documentation can be used to verify the important technical claims.

### Sources Used

1. Synopsys — TestMAX DFT: Design-for-Test Implementation.
2. Synopsys — DFTMAX Compression Shared I/O.
3. Cadence — Modus DFT Software Solution.
4. Cadence — Modus DFT Software Solution product information.


---

## Q6. What Is an AI Agent?

### 1. Five Key Concepts

**Large Language Model (LLM):**  
An LLM is a type of AI model trained on large amounts of text to understand and generate human-like language. It generates responses by predicting suitable next tokens based on the input and context.

**LLM Application:**  
An LLM application is a complete software application that uses an LLM as one of its components. It may add a user interface, instructions, application logic, memory, or other features around the model.

**RAG System:**  
RAG stands for **Retrieval-Augmented Generation**. A RAG system retrieves relevant information from an external knowledge source and provides that information to the LLM so that the model can generate a response using the retrieved context.

**Tool-Using Assistant:**  
A tool-using assistant is an AI system that can use external tools to perform tasks that the language model cannot reliably perform by itself. Examples include search engines, calculators, databases, APIs, or other software tools.

**AI Agent:**  
An AI agent is a system designed to work toward a goal through multiple steps. It can determine what actions or information are needed, use available tools, inspect their results, and continue the workflow before producing a final response.

### 2. AI Agent Architecture

```text
                 USER REQUEST
                      |
                      v
              +---------------+
              |   AI Agent    |
              |   / LLM       |
              +---------------+
                      |
                      v
              Understand Goal
                      |
                      v
              Decide Next Step
                      |
              +-------+-------+
              |               |
              v               v
        Need Information?   Need Tool?
              |               |
              v               v
        Retrieve Data      Call Tool/API
              |               |
              +-------+-------+
                      |
                      v
                 Tool Result
                      |
                      v
               Evaluate Result
                      |
              +-------+-------+
              |               |
              v               v
        More steps needed?   Goal completed
              |               |
              v               v
          Repeat          Final Response
          Workflow
```
### 3. Agent vs Simple Chatbot

A simple chatbot mainly receives a user's message and generates a response. It is generally reactive and depends on the user's prompts to continue the interaction.

An AI agent is designed to work toward a specific goal through multiple steps. It can plan actions, use available tools, obtain information from external sources, evaluate results, and continue the workflow with less continuous user direction.

| Feature | Simple Chatbot | AI Agent |
|---|---|---|
| Main purpose | Conversation and response generation | Goal-oriented task completion |
| Interaction | Mainly responds to user prompts | Can take multiple steps toward a goal |
| Planning | Usually limited | Can plan and break a task into subtasks |
| Tool use | May have limited or predefined tool access | Can select and use available tools as part of a workflow |
| Workflow | Usually prompt → response | Goal → plan → action/tool use → result → next action |
| Autonomy | More dependent on continuous user input | Can operate more independently within defined permissions |

For example, a chatbot can answer **"What are some good hotels in Singapore?"** by generating a response. An AI agent could take the goal **"Plan my three-day Singapore trip within my budget,"** gather relevant information using available tools, compare options, and create an itinerary.

Therefore, the main difference is not simply that an agent uses a more advanced language model. The difference is in the **overall system behavior**: an agent can pursue a goal through a multi-step workflow and use tools or external information to complete that goal.

### 4. Non-VLSI Example: Travel-Planning Agent

Consider an AI agent given the request:

> **"Plan a three-day trip to Singapore within my budget."**

The agent could:

1. Understand the user's destination, dates, and budget.
2. Retrieve relevant travel information.
3. Search for suitable transportation.
4. Find hotels within the budget.
5. Search for suitable activities.
6. Compare the collected information.
7. Create a three-day itinerary.
8. Present the final plan to the user.

This is different from a simple chatbot because the system can perform several connected steps and use external information or tools to work toward the user's goal.

### 5. Verification

The explanation was checked against the VLSIGuru Week 1 assessment requirements and reliable technical sources about AI agents and retrieval-augmented systems.

The VLSIGuru assessment emphasizes understanding the underlying system behavior rather than relying on vendor-specific definitions. It specifically distinguishes a model that generates text from a system that can use tools and act through a workflow.

The explanation is consistent with the general concept that an AI agent can work toward a goal through multiple steps and interact with external tools or information when required.

### Reflection

This question helped me distinguish between an **LLM and a larger AI system built around an LLM**. An LLM mainly provides language generation, while an LLM application can add instructions, application logic, retrieval, tools, or other capabilities.

A RAG system adds external information retrieval to provide relevant context to the model. A tool-using assistant can interact with external tools to perform specific tasks. An AI agent can combine these capabilities and use them as part of a multi-step workflow toward a goal.

The main lesson is that **not every application using an LLM is an AI agent**. The important factor is how the overall system behaves and whether it can use tools and carry out a goal-directed workflow.

### Sources
1. IBM Think — AI Agents
2. IBM Think — Retrieval-Augmented Generation (RAG)
3. VLSIGuru — AI Literacy Layer, Week 1 Student Assessment
---

## Question 7: Human Oversight of AI Systems

AI systems can produce useful outputs, but human review is important when an incorrect or biased output could cause significant harm or when the decision affects people's rights, safety, money, or opportunities.

### 1. Situations Where Humans Should Inspect or Approve AI Output

| Situation | Why Human Review Is Needed | Possible Risk |
|---|---|---|
| Medical diagnosis or treatment suggestions | Medical decisions can directly affect a person's health | Incorrect diagnosis or treatment |
| Loan or credit decisions | Financial decisions can significantly affect a person's access to money | Unfair or incorrect decisions |
| Hiring or candidate screening | AI may influence a person's employment opportunity | Bias or rejection based on inappropriate factors |
| Legal or compliance decisions | Legal decisions can have serious consequences | Incorrect interpretation of laws or evidence |
| Safety-critical systems | Errors can cause physical harm or equipment failure | Unsafe actions or incorrect decisions |

### 2. Why Human Oversight Matters

AI systems can make mistakes, produce incomplete information, or reflect limitations in their training data and design. Human review provides an opportunity to check whether the output is appropriate before an important decision or action is taken.

Human oversight is especially important when:
- The consequences of an error are serious.
- The decision affects a person's rights or opportunities.
- The AI output cannot be easily verified.
- The system is operating in an unfamiliar or unusual situation.
- Sensitive or personal information is involved.

### 3. Evidence and Verification

The need for human oversight is consistent with responsible AI principles that emphasize human involvement, transparency, accountability, and the ability to review AI-supported decisions.

For important decisions, AI output should not automatically be treated as the final answer. A qualified person should be able to inspect the evidence, question the result, and approve or reject the proposed action.

### 4. Responsible AI Rule

> **AI can assist with decisions, but humans should remain responsible for reviewing and approving high-impact decisions.**

This means that AI output should be treated as assistance rather than unquestionable authority. The level of human review should depend on the potential impact and risk of the decision.

### 5. Reflection

This question helped me understand that using AI responsibly is not only about getting an accurate answer. It is also about considering what could happen if the answer is wrong.

For low-risk tasks, AI output may only need a basic check. For high-impact situations such as healthcare, employment, finance, law, or safety, human review becomes much more important.

The main lesson I learned is that **human oversight should increase as the potential impact of an AI error increases.**


---

## Question 8: AI/ML in Everyday Systems

AI and machine learning are used in many everyday systems. However, not every automated system necessarily requires AI or machine learning.

### 1. Everyday Systems

| Everyday System | AI/ML Involvement | Task Type | Evidence / Reason | Uncertainty | Simpler Rule-Based Alternative |
|---|---|---|---|---|---|
| Email spam filter | Machine Learning | Classification | Learns patterns from examples of spam and normal emails | A message may be incorrectly classified | A manually maintained list of blocked senders or keywords |
| Voice assistant | AI / Machine Learning | Speech recognition + language understanding | Converts spoken language into text and interprets the request | May misunderstand accents, pronunciation, or unclear speech | Fixed voice commands with predefined phrases |
| YouTube/Netflix recommendations | Machine Learning | Recommendation | Uses information about viewing behavior and content to suggest items | Recommendations may not match the user's actual interests | Fixed categories or manually selected preferences |
| Google Maps route/ETA prediction | Machine Learning + traditional algorithms | Prediction + optimization | Uses traffic and historical travel information to estimate travel time and routes | Traffic conditions can change unexpectedly | Fixed routes based only on distance or predefined rules |
| Smartphone face unlock | Machine Learning / Computer Vision | Recognition | Analyzes facial features to determine whether the face matches the enrolled user | Lighting, pose, or appearance changes can affect recognition | PIN, password, or pattern lock |

### 2. Why AI/ML Is Used

AI or machine learning is useful when the system needs to recognize patterns, make predictions, understand complex inputs, or adapt to data.

For example, a spam filter cannot rely only on a small fixed list of words because spam messages can change their wording. A machine-learning model can learn patterns from examples and use them to classify new messages.

### 3. Where Uncertainty Comes From

Unlike a simple rule-based system, many AI/ML systems operate with some degree of uncertainty.

For example:

- A voice assistant may misunderstand speech.
- A recommendation system may suggest something the user does not like.
- A navigation system may underestimate travel time because traffic changes.
- A face-recognition system may perform differently under different conditions.

Therefore, an AI output should not always be treated as certain or guaranteed.

### 4. Could AI Be Replaced by Rules?

In some cases, yes.

If a task has simple, predictable, and clearly defined conditions, a rule-based system may be sufficient.

For example:

```text
IF temperature > 40°C
    THEN display "High Temperature Warning"
```
This does not require machine learning because the condition and result are explicitly defined.

However, tasks involving complex patterns, large amounts of data, or changing inputs may be more difficult to handle using only fixed rules.

###5. Reflection

This question helped me understand that automation and AI are not the same thing. A system can perform an automated task using simple predefined rules without using machine learning.

AI/ML becomes more useful when the system needs to learn patterns from data, recognize complex inputs, or make predictions where the exact rules are difficult to define manually.

The main lesson I learned is that AI should be used when it provides a meaningful advantage over simpler approaches, rather than assuming every automated system needs AI.
---

## Question 9: Prediction, Classification, and Generation

These are three broad types of tasks commonly used in AI and machine-learning systems.

### 1. Classification of Examples

| Example | Task Type | Explanation |
|---|---|---|
| A. Predicting house prices | Prediction | The system estimates a numerical value, such as the future or expected price of a house. |
| B. Detecting whether an image contains a cat | Classification | The system assigns the image to a category such as "cat" or "not cat." |
| C. Writing an email from a short instruction | Generation | The system creates new text based on the user's instruction. |
| D. Predicting whether a customer will cancel a subscription | Prediction | The system estimates the likelihood of a future event based on available information. |
| E. Summarizing a research paper | Generation | The system generates a shorter version of the original content. |
| F. Identifying whether a transaction is fraudulent | Classification | The system classifies the transaction into categories such as "fraudulent" or "not fraudulent." |
| G. Generating an image from a text description | Generation | The system creates new visual content based on the text prompt. |
| H. Predicting the next word/token in a sentence | Prediction | The model estimates which token is most likely to come next based on the previous context. |

### 2. Understanding the Three Task Types

#### Prediction

Prediction means estimating a value, outcome, or future event based on available information.

Examples:
- Predicting house prices
- Predicting customer cancellation
- Predicting the next token in a sentence

The output can be a numerical value, probability, or another predicted outcome.

#### Classification

Classification means assigning an input to one or more predefined categories.

Examples:
- Cat vs. not cat
- Fraudulent vs. legitimate transaction
- Spam vs. normal email

The system chooses a category based on patterns in the input.

#### Generation

Generation means producing new content based on an input, instruction, or context.

Examples:
- Writing an email
- Summarizing a research paper
- Generating an image from a text description

The output is newly generated content rather than simply selecting one predefined category.

### 3. Important Observation

Some real-world AI systems can combine multiple task types.

For example, an AI system might first classify an input, then make a prediction, and finally generate a response for the user.

Therefore, the categories are useful for understanding the primary task being performed, but they do not mean that every complete AI application performs only one type of task.

### 4. Evidence and Verification

I classified the examples according to the primary purpose of the task:

- Estimating an amount or future outcome → Prediction
- Assigning an input to a category → Classification
- Creating new content → Generation

This classification also matches the Week 1 assessment's distinction between prediction, classification, and generation as broad AI task types.

### 5. Reflection

This question helped me understand that AI systems can perform different kinds of tasks. Prediction focuses on estimating an outcome, classification focuses on assigning categories, and generation focuses on creating new content.

Understanding these differences will help me recognize what an AI or machine-learning system is actually doing instead of simply calling every intelligent-looking system "AI."

### Sources
NIST — Artificial Intelligence Risk Management Framework (AI RMF)

---

## Q10 - Personal AI Verification Protocol

### A - Answer

My personal AI verification protocol is a simple process I can follow whenever I use AI for technical or important work:

1. **Define the task clearly** — Understand what I am trying to find out or accomplish.
2. **Ask the AI** — Use a clear prompt and provide the necessary context.
3. **Inspect the response** — Check the answer for assumptions, missing information, unsupported claims, and possible errors.
4. **Verify important claims** — Check important technical or factual information using reliable sources such as official documentation, standards, research papers, or other authoritative references.
5. **Compare evidence** — If sources disagree, investigate the disagreement instead of automatically accepting the AI response.
6. **Conclude carefully** — Decide what is supported by the available evidence and clearly state any remaining uncertainty.
7. **Document and reflect** — Record important sources and consider what could still go wrong.

### E - Evidence

The Week 1 assessment recommends the A-E-V-R method:

- **A — Answer:** What is my answer to the question?
- **E — Evidence:** What evidence supports the answer?
- **V — Verification:** How did I check that the answer is reliable?
- **R — Reflection:** What did I learn, and what could still go wrong?

The assessment also recommends a broader workflow:

```text
DEFINE
   ↓
ASK / INVESTIGATE
   ↓
INSPECT
   ↓
VERIFY
   ↓
CONCLUDE
   ↓
DOCUMENT
   ↓
REFLECT

```
For important claims, I should prefer authoritative or primary sources first, followed by high-quality secondary sources. AI assistants can help with explanation, brainstorming, comparison, and finding possible references, but the AI-generated answer itself should not be treated as the final authority.

###V - Verification

I verified my protocol against the VLSIGuru Week 1 Student Assessment and its recommended A-E-V-R workflow and source hierarchy.

The assessment specifically emphasizes that AI output should be inspected and important factual or technical claims should be verified before submission. It also states that if a claim cannot be verified, I should document that limitation rather than pretend to be certain.

Therefore, my protocol is:

Define → Ask → Inspect → Verify → Conclude → Document → Reflect

This process helps make my AI-assisted work more traceable and reduces the risk of accepting an AI-generated answer simply because it sounds convincing.

###R - Reflection

This question helped me understand that using AI responsibly is not just about writing a good prompt. I also need to check what the AI produces.

My main takeaway is that AI is a useful assistant, but verification is my responsibility. For technical work, I should check important claims against reliable sources and record the evidence I used.

I also learned that uncertainty is acceptable. If I cannot verify a claim, it is better to clearly state that it could not be verified than to present an unsupported answer as a fact.

Going forward, I will use the following personal rule:

####Ask AI for assistance, inspect the output, verify important claims, document the evidence, and make the final judgment myself.
