# Mission 8 — Does This Problem Actually Need ML?

## 1. Define the engineering problem

Consider a semiconductor physical-design team that wants to identify chip designs that are likely to fail timing requirements before the full design process is complete.

The goal is to identify timing risk early enough for engineers to investigate and improve the design.

## 2. Option A — Rule-Based Solution

A rule-based system follows explicit conditions written by engineers.

For example:
- If a completed timing report shows negative slack, flag a timing violation.
- If a design exceeds a defined congestion threshold, raise a warning.
- If a required input report is missing, ask the engineer to provide it.

**Advantages:**
- The rules are easy to understand and audit.
- No historical training dataset is required.
- The system behaves predictably when the rules and inputs are fixed.

**Limitations:**
- Engineers must define and maintain the rules.
- Simple thresholds may not capture complicated relationships between design features.
- Rules may not predict problems accurately when detailed timing reports are not yet available.

## 3. Option B — Possible ML Solution

A machine learning model could use historical chip-design data to predict whether a new design is at risk of failing timing requirements.

Possible input features include:
- Clock frequency target
- Cell area
- Estimated routing congestion
- Early timing estimates
- Design characteristics from previous stages

The target could be a label indicating whether the completed design passed or failed timing.

**Advantages:**
- The model may learn relationships among multiple design features.
- It could estimate risk before the final timing report is available.
- It could help engineers prioritise designs that need further investigation.

**Limitations:**
- It needs suitable historical data with reliable labels.
- Predictions may be inaccurate for new designs or unfamiliar technology conditions.
- Engineers need to evaluate and monitor performance.
- A risk prediction is not proof that a design will fail.

## 4. Comparison

| Consideration | Rule-based solution | ML solution |
|---|---|---|
| Data requirements | Requires defined rules and relevant inputs | Requires representative historical data for training and evaluation |
| Explainability | Usually straightforward to trace to a rule | May be harder to explain, depending on the model |
| Adaptability | Rules need manual updates | Can be retrained with suitable new data |
| Predicting unseen outcomes | Limited to what the rules can infer | May learn useful patterns from past examples |
| Failure mode | Rules may miss cases or use unsuitable thresholds | Poor data, bias, leakage or changing conditions may harm predictions |
| Best use | Clear, stable requirements | Complex patterns where data can support useful predictions |

## 5. How would success be measured?

The team should evaluate the system on designs not used for training or rule development.

For an ML model, useful measures could include:
- Recall: how many actual timing failures are detected.
- Precision: how many designs flagged as risky really fail timing.
- False negatives: timing failures that the model misses.
- False positives: designs flagged as risky that ultimately pass.

The team should also compare the ML model with a simple baseline and consider the cost of missed timing failures and unnecessary investigations.

## 6. Which solution should be chosen?

A rule-based system is a sensible starting point when explicit engineering constraints already provide reliable answers.

ML may be useful when the goal is to predict timing risk early and historical data contains patterns that are difficult to capture with fixed rules.

A combined approach may be appropriate: use established engineering rules for mandatory checks and an ML model to estimate risk earlier in the workflow. Engineers should validate the predictions before relying on them.

## 7. Conclusion

Machine learning is not automatically the best solution to every engineering problem. The choice depends on the problem, available data, required accuracy, explainability, cost of errors and whether a simpler method already performs adequately.

## 8. Sources to consult

- Google for Developers — Introduction to Machine Learning: https://developers.google.com/machine-learning/intro-to-ml
- Google for Developers — Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course

I will consult the relevant material, verify the concepts and revise this draft in my own words before submission.
