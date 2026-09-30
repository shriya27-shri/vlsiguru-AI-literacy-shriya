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
