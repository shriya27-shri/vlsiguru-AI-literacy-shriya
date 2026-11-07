
# AI Tools Exploration

## 1. Introduction

The purpose of this activity is to explore how different AI tools can support engineering learning, technical research, and problem-solving.

I selected Design for Testability (DFT) as my learning topic because it is related to my VLSI learning track.

## 2. AI Tools Selected

| AI Tool | Purpose |
|---|---|
| ChatGPT | Technical explanations and learning assistance |
| Google Gemini | Comparing technical explanations |
| NotebookLM | Studying information from reference documents |
| Perplexity | Finding technical information and sources |
| Claude | Detailed explanations and analysis |

Note: I will record the tools I actually experiment with and the observations I make.


## 3.Experiment 1: Understanding Scan Insertion Using ChatGPT

### AI Tool
ChatGPT

### Prompt Used
Explain scan insertion in Design for Testability (DFT). What is it, why is it required, and how does it help detect manufacturing defects in an IC? Give a simple example suitable for an ECE graduate who is new to DFT.

### Summary of AI Response
ChatGPT explained scan insertion as a DFT technique in which normal flip-flops are replaced with scan flip-flops and connected into scan chains.

It explained the role of Scan Input (SI), Scan Enable (SE), Scan Output (SO), and the three main scan operations:

1. Shift-in: Load test data into scan flip-flops.
2. Capture: Allow the combinational logic to process the data and capture the response.
3. Shift-out: Shift the captured response out for comparison with the expected result.

It also explained controllability and observability, demonstrated a stuck-at-0 fault example, and introduced the ASIC testing flow involving synthesis, scan insertion, ATPG, and ATE.

### What I Learned
I understood how scan insertion makes internal flip-flops easier to control and observe. I also learned how scan chains help ATPG patterns detect manufacturing defects that cannot easily be tested through normal input and output pins.

### What the AI Did Well
- Explained the concepts in a beginner-friendly manner.
- Used a simple AND-gate example to explain fault detection.
- Clearly separated shift-in, capture, and shift-out operations.
- Included important DFT terminology and interview questions.

### Limitations and Observations
- The response was lengthy and could be more concise for interview revision.
- It did not demonstrate the scan-chain values after each individual shift clock.
- The ASIC flow was simplified and did not cover every implementation and verification stage.
- Some unrelated references appeared without useful context.

### My Verification
I checked the explanation against my understanding of scan flip-flops, scan enable, controllability, observability, and the scan-chain operation. The basic concepts were consistent with what I had studied in DFT.

### Conclusion
ChatGPT was useful for building a beginner-level understanding of scan insertion. However, technical details and examples should still be checked rather than accepted without verification.



## 4.Experiment 2: Comparing Gemini with ChatGPT

### AI Tool
Google Gemini

### Prompt Used
Explain scan insertion in VLSI Design for Testability (DFT) to a beginner. Use a simple example with three scan flip-flops. Show how shift-in, capture, and shift-out work, including the values stored in each flip-flop after every shift clock. Keep the explanation technically accurate and suitable for an ECE graduate preparing for a DFT interview.

### Summary of AI Response
Gemini explained scan insertion using a three-flip-flop scan chain. It demonstrated the values stored in each flip-flop after every shift clock.

It explained:
- Shift-in with SE = 1.
- Capture with SE = 0.
- Shift-out with SE = 1.
- How the captured response reaches the scan-out pin.
- At-speed testing, overlapping shift operations, and hold-time concerns.

### What Gemini Did Well
- Demonstrated the scan-chain operation clock by clock.
- Used a clear three-flip-flop example.
- Explained how scan-out works.
- Included additional interview-level concepts.

### Limitations and Observations
- The capture values were assumed rather than calculated from a specified combinational circuit.
- The explanation could clarify that TCK is a JTAG clock and is not necessarily the scan clock in every design.
- Some advanced concepts were introduced without detailed explanations.

### Comparison with ChatGPT
Both tools explained the fundamental purpose of scan insertion, controllability, observability, and the shift-in, capture, and shift-out process.

ChatGPT provided a broader beginner-level overview, including a stuck-at fault example and the simplified ASIC flow.

Gemini provided a more detailed three-flip-flop example and showed the values after each shift clock. This made the scan-chain operation easier to visualize.

### My Conclusion
Both AI tools were useful for learning DFT concepts. ChatGPT was better for a broad introduction, while Gemini was more useful for understanding the clock-by-clock operation of a scan chain. Comparing their answers helped me identify differences in explanation depth and technical detail.

## 5.Experiment 3: Understanding ATPG and Fault Coverage Using ChatGPT

### AI Tool
ChatGPT

### Prompt Used
Explain ATPG (Automatic Test Pattern Generation) and fault coverage in VLSI DFT to a beginner. Use a simple digital circuit example to explain how ATPG detects stuck-at-0 and stuck-at-1 faults. Also explain what fault coverage percentage means, why 100% coverage may not always be possible, and the difference between fault detection and fault diagnosis. Use an example suitable for an ECE graduate preparing for a DFT interview.

### Summary of AI Response
ChatGPT explained ATPG as a process that automatically generates test patterns to detect modeled manufacturing faults in a digital circuit.

It used a circuit with two cascaded AND gates:

X = A AND B
Y = X AND C

It demonstrated:
- SA0 detection at X using the pattern ABC = 111.
- SA1 detection at X using the pattern ABC = 011.
- Fault activation, fault propagation, and fault observation.
- Fault coverage calculation using detected faults divided by total modeled faults.
- Reasons why 100% fault coverage may not be achievable.
- The difference between fault detection and fault diagnosis.

### What the AI Did Well
- Used a simple circuit to demonstrate ATPG.
- Explained how to activate and propagate stuck-at faults.
- Showed the expected and faulty output values.
- Explained fault coverage with a numerical example.
- Distinguished fault detection from fault diagnosis.
- Included interview questions and a sample interview answer.

### Limitations and Observations
- The explanation was lengthy and could be divided into shorter learning sections.
- Some advanced terms, such as redundant faults and ATPG algorithms, were introduced without detailed examples.
- The fault coverage formula was presented in a simplified form; actual tool reports may distinguish detected, untestable, aborted, and other fault categories.
- The response could have explained more clearly how scan chains help ATPG control and observe internal sequential logic.

### My Verification
I checked the stuck-at fault examples.

For SA0 at X:
- A = 1, B = 1, C = 1.
- Good circuit output = 1.
- Faulty circuit output = 0.

For SA1 at X:
- A = 0, B = 1, C = 1.
- Good circuit output = 0.
- Faulty circuit output = 1.

Both examples correctly demonstrate fault activation and propagation through the second AND gate.

### What I Learned
I learned that ATPG generates test patterns by activating a fault, propagating its effect, and observing the difference at an output.

I also understood that fault coverage represents the percentage of modeled faults detected, not the percentage of the chip that is working.

Fault detection identifies whether a fault exists, whereas fault diagnosis helps identify its likely location.

### Conclusion
ChatGPT provided a useful explanation of ATPG and fault coverage using simple digital logic. The numerical examples helped me understand how test patterns detect stuck-at faults. I also learned that AI-generated technical explanations should be checked using circuit logic and independent verification.

## 6.Experiment 4: Scan-Chain Debugging Using Claude

### AI Tool
Claude

### Prompt Used
A scan chain contains 4 scan flip-flops connected in series. During scan testing, the expected output pattern is 1011, but the observed output pattern is 1001.

Explain how a DFT engineer would investigate this scan-chain failure.

Include:
1. Possible reasons for the mismatch.
2. How to check scan-chain connectivity.
3. How to identify whether the problem is in the scan chain, scan enable, clock, or scan flip-flop.
4. How scan-chain diagnosis helps locate the faulty element.

Explain step by step at a beginner-friendly level suitable for an ECE graduate learning DFT.

### Summary of AI Response
Claude explained how a DFT engineer could investigate a scan-chain mismatch.

It discussed:
- Possible stuck-at faults and broken scan connections.
- Hold-time violations and scan-enable problems.
- Clock skew, missing clock edges, and scan flip-flop defects.
- Flush testing to check scan-chain integrity.
- Changing test patterns and clock conditions to isolate failures.
- Using scan-chain diagnosis to identify possible faulty cells or connections.

### What the AI Did Well
- Used a practical scan-chain failure example.
- Explained several possible causes instead of assuming one fault.
- Introduced flush testing and chain-integrity checks.
- Explained how failure positions can help identify possible faulty scan elements.
- Described a systematic debugging approach.

### Limitations and Observations
- A single incorrect output bit cannot conclusively identify a faulty flip-flop.
- The exact scan-chain orientation and bit ordering must be known before mapping a failing bit to a particular flip-flop.
- Slowing the clock does not generally resolve a hold-time violation.
- Some diagnosis steps require EDA tools, timing reports, simulation, or physical failure analysis.

### What I Learned
I learned that scan-chain debugging involves more than checking whether the expected and observed patterns match.

A DFT engineer must investigate scan connectivity, scan enable, clock behavior, scan flip-flops, and timing problems.

I also learned about flush testing as a way to check scan-chain integrity and how diagnosis can narrow down possible fault locations.

### Comparison with Previous AI Tools
ChatGPT provided a beginner-level explanation of scan insertion and ATPG. Gemini demonstrated scan-chain shifting clock by clock. Claude focused on practical scan-chain debugging.

Each tool approached the DFT topic differently and provided a different type of learning experience.

### Conclusion
Claude was useful for understanding how a DFT engineer approaches scan-chain failures. However, its suggested causes and diagnosis methods must be checked against actual scan-chain architecture, timing reports, and EDA tool results.


## 7.Experiment 5: Researching Scan-Chain Hold-Time Violations Using Perplexity

**AI Tool:** Perplexity AI

**Topic:** Scan-chain hold-time violations in VLSI DFT

### Prompt Used
Research scan-chain hold-time violations in VLSI DFT. Explain their causes, effects on scan testing, physical-design solutions, and the difference between hold-time and setup-time violations. Use reliable technical sources and distinguish verified facts from assumptions.

### Summary of AI Response
Perplexity explained that a scan-chain hold-time violation occurs when scan data changes too soon after the active clock edge, violating the receiving flip-flop's hold requirement.

It identified several causes:
- Clock skew between adjacent scan flip-flops.
- Very short scan data paths.
- Scan-chain ordering that does not consider physical placement and clock arrival times.
- Incorrect scan-mode timing constraints.

It discussed the following possible solutions:
- Clock-aware scan-chain reordering.
- Hold-fix buffers or delay cells.
- Lockup latch insertion.
- Clock-tree adjustment.
- Correct scan-mode static timing analysis (STA).

It also explained that slowing the scan clock may help setup timing but does not generally fix a true hold-time violation.

### What the AI Did Well
- Connected scan-chain timing problems with practical DFT implementation.
- Explained the difference between setup and hold violations.
- Provided a useful list of physical-design solutions.
- Included references to technical documentation and educational material.

### Limitations and Verification
- The timing equation was simplified and should not replace a proper STA calculation.
- Some explanations, such as a bit skipping a scan stage, are simplified illustrations of a timing race.
- Not every listed solution applies to every scan-chain architecture.
- The sources needed independent checking before accepting all the claims.

I checked the Synopsys TestMAX DFT documentation and University of Michigan DFT material. These supported the discussion of scan-chain ordering, scan insertion, and timing considerations.

### What I Learned
I learned that scan-chain failures are not always caused by incorrect logical connections. Clock skew and insufficient data-path delay can also corrupt scan shifting.

I also understood that DFT engineers and physical-design engineers work together to identify and resolve scan timing problems.

### Conclusion
Perplexity was useful for researching a technical DFT topic and finding supporting references. However, AI-generated explanations and citations must be verified using reliable technical documentation.

## 8. Overall Learning

Through these experiments, I explored how AI tools can support technical learning, improve the quality of prompts, compare explanations, and assist in checking engineering information.

I also understood that AI-generated answers should be verified using reliable technical documentation rather than accepted blindly.
