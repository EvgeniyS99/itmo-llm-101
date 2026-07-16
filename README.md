# ITMO LLM 101

**Designed and authored by [EvgeniyS99](https://github.com/EvgeniyS99).**

Course materials for **ITMO LLM 101 — Fall 2025**. This advanced practical course covers the engineering of LLM-powered services, from transformer inference and local model serving to stateful applications built with LangChain, LangGraph, FastAPI, and Gradio.

## Target Audience

This course is designed for advanced ML students, Python developers, ML engineers, and technical specialists with prior industry or hands-on development experience.

It is intended for learners who want not only to use LLM tools, but also to understand how to design, debug, deploy, and maintain LLM services.

## Key Topics

- GPT-like model architecture and transformer inference;
- KV cache, batching, quantization, latency, throughput, and cost;
- vLLM, TGI, Ollama, and different approaches to LLM serving;
- LangChain, LangGraph, tool calling, and structured output;
- asynchronous FastAPI backends and multi-user applications;
- user interfaces built with Gradio and Jinja templates;
- observability, tracing, and debugging with Langfuse.

## Learning Outcomes

By the end of the course, participants will be able to:

- explain how GPT-like models perform autoregressive transformer inference;
- reason about KV-cache usage, batching, quantization, and inference trade-offs;
- evaluate LLM services using latency, throughput, quality, memory, and cost metrics;
- serve local and open-source models with vLLM, TGI, and Ollama;
- build structured LLM workflows with LangChain and LangGraph;
- implement tool calling, structured output, streaming, persistence, and human-in-the-loop interactions;
- design asynchronous, multi-user LLM backends with FastAPI;
- build user-facing interfaces with Gradio and Jinja templates;
- trace and debug LLM applications with Langfuse.

## Course Structure

| Lecture | Topic | Materials |
| --- | --- | --- |
| 1 | Introduction to large language models | [Open lecture](lecture_1/) |
| 2 | LLM serving and quantization | [Open lecture](lecture_2/) |
| 3 | LangChain fundamentals and tool calling | [Open lecture](lecture_3/) |
| 4 | Stateful applications with LangGraph | [Open lecture](lecture_4/) |
| 5–6 | FastAPI, Gradio, and the final project | [Open lecture](lecture_5-6/) |

Each lecture directory contains a short overview, presentation slides, and the available seminar and homework materials.

Some assignments reference a separate capstone application repository. That project is maintained independently and is not part of this course repository.

## Setup

Create a virtual environment and install the shared Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Some exercises require additional system-level tools or services, including Ollama, vLLM, Docker, and access to a GPU. Notebooks that use external model providers also require locally configured credentials. Never commit API keys or access tokens to the repository.

## Repository Layout

```text
.
├── lecture_1/
├── lecture_2/
├── lecture_3/
├── lecture_4/
├── lecture_5-6/
└── requirements.txt
```
