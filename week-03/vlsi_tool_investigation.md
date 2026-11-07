
# Open-Source VLSI Tool Investigation

## 1. Tool Selected

**Tool Name:** Fault

**Category:** Design for Testability (DFT)

**Official Documentation:** https://fault.readthedocs.io/en/latest/

## 2. Introduction

Fault is an open-source Design for Testability tool used for testing digital hardware designs.

It provides features related to automatic test pattern generation (ATPG), scan stitching, test-vector compaction, and JTAG insertion.

I selected this tool because it is directly related to my VLSI DFT learning track.

## 3. What Problem Does the Tool Solve?

Testing an integrated circuit after manufacturing is important because manufacturing defects can affect its functionality.

Fault provides features that help generate test patterns and perform fault simulation to identify potential manufacturing defects.

It supports testing using the stuck-at fault model.

## 4. Main Features

1. **Synthesis:** Uses a Yosys-based synthesis script to process Verilog RTL.
2. **Scan Stitching:** Supports connecting flip-flops into scan chains.
3. **ATPG:** Generates test patterns for detecting faults.
4. **Fault Simulation:** Supports stuck-at fault simulation.
5. **Test Vector Compaction:** Supports reducing test-vector sets.
6. **JTAG Insertion:** Provides JTAG-related test functionality.

## 5. Main Inputs and Outputs

**Inputs:**
- Verilog RTL design
- Synthesized netlist
- Standard-cell library information where required
- Test configuration and fault-model information

**Outputs:**
- Synthesized netlist
- Scan-related design information
- Generated test vectors
- Fault simulation results

## 6. Basic Workflow

1. Start with a Verilog RTL design.
2. Synthesize the design into a netlist.
3. Prepare the design for scan testing.
4. Generate test patterns using ATPG.
5. Perform fault simulation.
6. Analyse the test results.

Note: This is a simplified conceptual workflow, not a complete installation or execution record.

## 7. What I Explored

I studied the official documentation to understand the purpose and main features of Fault.

I learned that it combines multiple DFT-related functions, including scan stitching, ATPG, and fault simulation.

**Practical experiment:**


## Installation and Dependencies

According to the official Fault documentation, the tool requires several supporting EDA utilities.

| Dependency | Purpose |
|---|---|
| Python 3.8+ | Runs the Fault Python package/interface |
| Yosys | Synthesizes Verilog RTL into a netlist |
| Icarus Verilog | Supports simulation and fault verification |
| Swift 5.6+ | Required when building Fault from source |
| Quaigh | Optional but recommended ATPG utility |

Fault can be installed using its Python package or through Nix. Other EDA dependencies must also be installed separately when using the manual installation route.

## Basic Fault Workflow

1. **Synth:** Converts Verilog RTL into a flattened netlist using Yosys.
2. **Cut:** Handles sequential elements in the netlist to prepare it for fault simulation.
3. **ATPG:** Generates test vectors and performs fault simulation using a stuck-at fault model.
4. **Compact:** Reduces the number of test vectors while preserving test effectiveness.
5. **Chain:** Performs scan-chain stitching.
6. **Verification:** Checks the generated test and scan-related outputs.

## Relevance to DFT

Fault is relevant to DFT because it provides an open-source environment for exploring ATPG, fault simulation, scan-chain stitching, and test-vector compaction.

**Installation reference:** https://fault.readthedocs.io/en/latest/installation.html

**Workflow reference:** https://fault.readthedocs.io/en/latest/index.html


## 8. Where Can AI or ML Help?

AI and ML could potentially assist DFT engineers in:

- Analysing large fault simulation reports.
- Identifying patterns in test failures.
- Helping engineers understand ATPG results.
- Suggesting possible test-pattern optimisations.
- Analysing historical test data.

These are potential applications and should not be confused with confirmed built-in features of Fault.

## 9. Learning Outcome

This investigation helped me understand how open-source tools can support DFT activities and how ATPG, scan stitching, and fault simulation are connected in the testing process.
