# Lecture 4: Introduction to LangGraph

This lecture focuses on stateful LLM workflows built as graphs. It covers graph state, nodes and transitions, persistence, interrupts, streaming, tool execution, and a basic Gradio chat interface.

## Learning Outcomes

After this lecture, participants will be able to:

- model stateful LLM applications as LangGraph graphs;
- implement nodes, transitions, conditional routing, and tool execution;
- use checkpointing and interrupts for persistent human-in-the-loop workflows;
- stream graph and model events to a client interface;
- connect a LangGraph application to a Gradio chat UI.

## Materials

- [Presentation: Introduction to LangGraph](langgraph_introduction.pdf)
- [Seminar notebook](seminar_4.ipynb)
- [Homework](hw_3.ipynb)

Some seminar examples expect a local `tokens.py` module containing an API key. Keep this file local; it is excluded by `.gitignore`.
