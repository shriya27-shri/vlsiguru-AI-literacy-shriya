# Mission 1 — AI and ML Mental Map

## Concept Map

```mermaid
flowchart TD
    AI["Artificial Intelligence (AI)<br/>Broad field of intelligent systems"]

    RULE["Rule-Based Programming<br/>Explicitly written rules"]
    ML["Machine Learning (ML)<br/>Learns patterns from data"]

    DL["Deep Learning<br/>Multilayer neural networks"]
    GEN["Generative AI<br/>Creates text, images, audio or code"]
    LLM["Large Language Models (LLMs)<br/>Process and generate language"]

    AUTO["Automation<br/>Executes predefined tasks"]

    AI --> RULE
    AI --> ML
    ML --> DL
    DL -. "Often used to build" .-> GEN
    GEN -. "Includes language-generating systems such as" .-> LLM

    AUTO -. "Can work with or without AI" .-> AI

    RULE --> R1["Developer defines conditions"]
    ML --> R2["Model learns from training data"]

    classDef ai fill:#dbeafe,stroke:#2563eb,color:#111827
    classDef learning fill:#dcfce7,stroke:#16a34a,color:#111827
    classDef generation fill:#fef3c7,stroke:#d97706,color:#111827
    classDef other fill:#f3e8ff,stroke:#9333ea,color:#111827

    class AI,ML ai
    class RULE,DL learning
    class GEN,LLM generation
    class AUTO,R1,R2 other
```

## Key Takeaways

1. AI is the broad field; ML is one approach within AI.
2. Rule-based programming follows explicitly written conditions.
3. ML learns patterns from data.
4. Deep learning is a subset of ML that uses multilayer neural networks.
5. Generative AI creates new content.
6. LLMs focus on processing and generating language.
7. Automation does not necessarily require AI or ML.

## Engineering Example

- **Rule-based:** Flag a chip timing violation when delay exceeds a specified limit.
- **Machine learning:** Predict timing pass/fail from historical design measurements.
- **Generative AI:** Generate a natural-language explanation of a Verilog module.

## Important Note

This is a simplified conceptual map. Generative AI is a capability, while deep learning is a learning approach and LLMs are language-focused models. They should not be treated as separate categories at exactly the same level.
