# 🌍 AI Multi-Agent Travel Planner

An AI-powered travel planning application built with **Python**, **Google Agent Development Kit (ADK)**, and **Gemini 2.5 Flash**. The application leverages a **multi-agent architecture** to research, validate, and generate personalized travel guides while integrating with a **custom MCP (Model Context Protocol) Server** for reusable travel services such as weather and date retrieval.

---

## ✨ Features

- 🤖 **Multi-Agent Architecture** – Specialized AI agents collaborate to generate, validate, and refine travel plans.
- 🧠 **Loop-Based Validation** – Automatically retries travel plan generation until validation succeeds or the retry limit is reached.
- 🗺️ **Personalized Trip Planning** – Generates itineraries based on destination, budget, travel duration, and user preferences.
- 🔍 **Google Search Integration** – Retrieves up-to-date information about destinations and attractions.
- 🔌 **MCP (Model Context Protocol) Integration** – Connects to an external MCP Server to dynamically discover and invoke travel tools.
- 🌤️ **Live Weather Information** – Fetches current weather for the destination through the MCP Server.
- 📅 **Current Date Generation** – Automatically includes today's date using the MCP Server.
- 📝 **Professional Markdown Guides** – Produces well-structured travel guides with tables, emojis, and organized sections.
- 💾 **Automatic File Export** – Saves every generated travel guide as a Markdown file.
- 🧩 **Extensible Tool Architecture** – Easily add new travel services (Hotels, Flights, Currency, Visa, etc.) without changing the ADK agents.

---

# 🏗️ Architecture

```text
                        User
                          │
                          ▼
                 Travel Coordinator
                          │
                          ▼
          Travel Plan Generator (LoopAgent)
                │                     │
                ▼                     ▼
          Trip Planner         Trip Validator
                │
                ▼
         Google Search Tool
                │
                ▼
        MCP Client (ADK Tool)
                │
────────────────────────────────────────────
                │
           Travel MCP Server
                │
      ┌─────────┴─────────┐
      ▼                   ▼
 Weather Tool       Current Date Tool
                │
                ▼
       Markdown Travel Guide
                │
                ▼
      Save Travel Plan Tool
```

---

## 🧰 MCP Server

The application communicates with a dedicated **Travel MCP Server**, allowing the AI agents to discover and invoke travel-related tools dynamically without directly importing them.

### Current MCP Tools

| Tool | Description |
|------|-------------|
| 🌤️ `get_weather` | Retrieves live weather information for the destination |
| 📅 `get_current_date` | Returns today's date in a human-readable format |

> More MCP tools such as **Hotel Search**, **Flight Search**, **Currency Converter**, **Visa Information**, and **Country Information** can be added without modifying the ADK agents.

---

## 🛠️ ADK Tools

| Tool | Purpose |
|------|---------|
| 🔍 Google Search | Researches destinations and attractions |
| 💾 Save Travel Plan | Saves the final travel guide as a Markdown document |

---

## 🚀 Running the Project

Install dependencies:

```bash
uv sync
```

Start the ADK application:

```bash
uv run adk web .
```

---

## 🧪 Example Prompt

```text
Plan a 7-day trip to Japan.

Starting from Hyderabad.

Budget: ₹4,50,000.

I want to visit Tokyo, Kyoto, and Osaka.

I enjoy anime, temples, street food, and photography.

Include the current weather, today's date, travel tips, and a day-by-day itinerary.
```

---

## 📄 Sample Output

Every generated travel guide is automatically saved as a Markdown document.

```text
travel_agent/
└── saved_trips/
    ├── tokyo_travel_plan.md
    ├── london_travel_plan.md
    └── switzerland_travel_plan.md
```

### Every guide includes

| Section | Description |
|---------|-------------|
| 🇯🇵 Destination | Destination and country information |
| 📅 Generated Date | Current date |
| 🌤️ Live Weather | Current destination weather |
| 📋 Trip Summary | Budget, duration, destination |
| 🗓️ Daily Itinerary | Day-by-day travel schedule |
| 💰 Budget Estimate | Estimated expenses |
| 🎒 Packing Checklist | Recommended items |
| 💡 Travel Tips | Local recommendations |
| ⚠️ Important Notes | Essential travel information |

---

## 🧰 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Language** | Python |
| **AI Framework** | Google Agent Development Kit (ADK) |
| **LLM** | Gemini 2.5 Flash / Gemini 2.5 Flash Lite |
| **Protocol** | Model Context Protocol (MCP) |
| **MCP SDK** | Python MCP SDK |
| **Search** | Google Search (ADK Tool) |
| **Weather API** | Open-Meteo API |
| **Package Manager** | uv |
| **Output** | Markdown |

---

## 🔗 Related Project

This project integrates with a dedicated **Travel MCP Server** that exposes reusable travel tools via the Model Context Protocol.

**Repository:** `travel-mcp-server` *(https://github.com/jranjan01/travel-mcp-server)*

```
AI Travel Planner (ADK Client)
            │
            ▼
     Travel MCP Server
            │
      Weather Tool
      Date Tool
```