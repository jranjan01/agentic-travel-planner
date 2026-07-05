# 🌍 AI Multi-Agent Travel Planner

An AI-powered travel planning application built with **Python** and **Google Agent Development Kit (ADK)**. The application uses a **multi-agent architecture** to research, plan, validate, and generate travel guides.

---

## ✨ Features

- 🤖 **Multi-Agent Architecture** – Specialized AI agents collaborate to research, validate, and generate travel guides.
- 🗺️ **Personalized Trip Planning** – Creates customized itineraries based on destination, budget, duration, and user preferences.
- 🔍 **Google Search Integration** – Retrieves up-to-date destination and attraction information.
- 🌤️ **Live Weather Information** – Includes current weather conditions for the primary destination.
- 📅 **Automatic Date Generation** – Adds the current date to every travel guide.
- ✅ **Validation & Retry Loop** – Automatically validates generated plans and retries when improvements are needed.
- 📝 **Professional Markdown Guides** – Generates well-structured travel guides with tables, emojis, and organized sections.
- 💾 **Automatic File Export** – Saves each travel guide as a Markdown file for easy sharing and future reference.

----


## 🏗️ Architecture

```text
User
   │
   ▼
Travel Coordinator
   │
   ▼
Validated Trip Planner (LoopAgent)
   │
   ├── Trip Planner
   │      └── Google Search
   │
   └── Trip Validator
   │
   ▼
Travel Plan Generator
   │
   ├── Current Date Tool
   ├── Weather Tool
   └── Save Travel Plan Tool
   │
   ▼
Markdown Travel Guide
```

---


## 🛠️ Tools

| Tool | Purpose |
|------|---------|
| 🌤️ Weather Tool | Retrieves the latest weather for the destination |
| 📅 Current Date Tool | Adds today's date to the travel guide |
| 💾 Save Travel Plan Tool | Saves the generated guide as a Markdown file |
| 🔍 Google Search | Researches destinations and attractions |

---

## 🚀 Running the Project

```bash
uv sync
```

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

Each generated travel guide is saved as a beautifully formatted Markdown document under the `travel_plans/` directory.

```text
travel_plans/
├── tokyo_travel_guide.md
├── switzerland_travel_guide.md
└── london_travel_guide.md
```

### Every travel guide includes:

| Section | Description |
|---------|-------------|
| 🇯🇵 Destination | Country flag and destination details |
| 📅 Generated Date | Automatically includes today's date |
| 🌤️ Current Weather | Live weather for the primary destination |
| 📋 Trip Summary | Duration, budget, travelers, destination |
| 🗓️ Day-by-Day Itinerary | Daily travel schedule and activities |
| 💰 Budget Estimate | Estimated travel expenses |
| 🎒 Packing Checklist | Suggested items to pack |
| 💡 Travel Tips | Local recommendations and useful advice |
| ⚠️ Important Notes | Essential travel information and reminders |
---

## 🧰 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Language** | Python |
| **AI Framework** | Google Agent Development Kit (ADK) |
| **LLM** | Gemini 2.5 Flash / Gemini 2.5 Flash Lite |
| **Search** | Google Search (ADK Tool) |
| **Weather API** | Open-Meteo API |
| **Package Manager** | uv |
| **Output Format** | Markdown |
