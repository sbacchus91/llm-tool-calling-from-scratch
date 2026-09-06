# LLM Tool Request Handshake

A minimal, framework-free demonstration of how large language models request external function calls using the OpenAI-compatible Chat Completions protocol with Google's Gemini models (`gemini-3.6-flash`).

This script isolates the exact moment an LLM stops text generation and delegates execution to local client code.

---

## Core Concepts Demonstrated

* **The Execution Boundary:** LLMs cannot execute code or access external systems directly. They are remote token generators that delegate actions via structured text.
* **Declarative Routing:** Instead of fragile `if/else` logic, the model evaluates natural language against a declarative tool schema and selects the relevant function.
* **The "Pause and Pass" Handshake:** When external data is needed, the model halts generation:
  * `finish_reason='tool_calls'`
  * `content=None`
  * `tool_calls=[...]` containing the function name, arguments (`{}`), and a tracking `id`.

