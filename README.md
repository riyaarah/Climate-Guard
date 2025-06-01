

# 🌍 ClimateGuard — AI-Powered Climate Awareness Agent

**ClimateGuard** is an AI agent built with Fetch.ai’s `uAgents` framework and powered by the ASI\:One (`asi1-mini`) large language model. It engages users in natural conversations about climate change, carbon footprint reduction, sustainable living, and environmental policies — delivering personalized, science-based, and actionable advice.

This repository contains the agent implementation for ClimateGuard to be deployed on the decentralized Fetch.ai `Agentverse` platform or locally for testing.

---

##  Quick Start

### Prerequisites

* Python 3.9 or higher
* Fetch.ai `uagents` framework
* OpenAI Python SDK compatible with ASI\:One API

### Setup

1. Clone this repo:

```bash
git clone https://github.com/your-username/climateguard.git
cd climateguard
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Replace the OpenAI API key placeholder in `agent.py` with your ASI\:One API key:

```python
api_key='sk_67703b522cef404ba12cdb5c9b9e152e9aa86fa175d44ac79944a03e588ea3c3'
```

4. Run the agent:

```bash
python agent.py
```

The agent will start on `http://127.0.0.1:8000/submit` and listen for chat messages.

---

##  Agent Overview

* **Agent name:** `climate_guard`
* **Port:** 8000
* **Seed phrase:** `climate_guard_secret_phrase`
* **Protocol:** Chat protocol based on Fetch.ai uAgents `chat_protocol_spec`
* **LLM:** ASI\:One `asi1-mini` model
* **Key features:**

  * Handles conversational queries about climate science, carbon footprint, sustainability
  * Responds with practical, science-based advice
  * Acknowledges incoming messages and sends chat responses
  * Handles errors gracefully and informs the user

---

##  Technical Details

* Uses `uagents` to manage the agent lifecycle and messaging
* Uses OpenAI Python SDK with a custom base URL to connect to ASI\:One LLM
* Implements message handlers for:

  * `ChatMessage` — receives user queries, calls LLM, returns answers
  * `ChatAcknowledgement` — no-op in this implementation
* Maintains conversational context by processing message contents

---

##  Environment Variables

For security, consider setting your API key as an environment variable and reading it in `agent.py` instead of hardcoding.

Example:

```python
import os
api_key = os.getenv("sk_67703b522cef404ba12cdb5c9b9e152e9aa86fa175d44ac79944a03e588ea3c3")
```

---

## Future Improvements

* Add persistent user context for multi-turn personalized conversations
* Integrate localized climate data sources for more tailored responses
* Enable voice interaction support
* Implement analytics dashboard for user engagement insights

---

## License

This project is licensed under the MIT License.

---




