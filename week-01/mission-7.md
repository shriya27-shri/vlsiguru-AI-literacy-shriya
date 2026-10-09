# Mission 7 — What Actually Runs AI?

## 1. CPU

A CPU is a general-purpose processor that handles varied tasks, program control and sequential operations. It can also execute AI computations.

## 2. GPU

A GPU can perform many computations in parallel, making it useful for the matrix and vector operations common in AI models.

## 3. NPU / AI Accelerator

An NPU or AI accelerator is specialised hardware designed to execute supported AI workloads efficiently, often with improved performance per watt.

## 4. Parallel Computation

Parallel computation means performing multiple calculations at the same time instead of executing every operation one after another.

## 5. Compute and Memory

AI models need compute resources to perform mathematical operations and memory to store model parameters, input data and intermediate results. Moving data between memory and processors can affect performance and energy consumption.

## 6. Training vs Inference

Training uses data to adjust a model's parameters. Inference uses the trained model to generate a response or prediction. Training often requires repeated computation over large datasets, while inference performs computations for new inputs.

## 7. AI Hardware Workflow

AI Application → AI Model → Software / Framework → CPU / GPU / AI Accelerator → Memory

This is a simplified conceptual view. Real systems may use multiple processors and memory types.

## 8. Real AI Workload: LLM Response Generation

When an LLM generates a response, it performs many mathematical operations using its learned parameters. A GPU can accelerate parallel computations, while high-bandwidth memory supplies model weights and intermediate data. A CPU may coordinate other application tasks.

The exact hardware depends on the deployment. I should not assume which processor a cloud AI service uses unless reliable information is available.

## Conclusion

I learned that AI is not only software. The model relies on computation, memory and hardware to process inputs and generate outputs. Understanding this connection helps explain why processor architecture, parallelism, memory bandwidth and energy efficiency matter for AI systems.
