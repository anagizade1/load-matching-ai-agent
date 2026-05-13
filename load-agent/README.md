# 🚛 Load Matching AI Agent

<<<<<<< HEAD
An AI agent that automatically finds suitable freight loads for truck 
drivers and sends SMS notifications via Twilio.

## How It Works
1. Reads active drivers from Google Sheets (location + truck type)
2. AI agent matches drivers to available loads
3. Sends SMS notification to each matched driver

## Tech Stack
- Python
- Claude AI — Anthropic (agentic tool use pattern)
- Google Sheets (driver data)
- Twilio (SMS notifications)

## Project Structure
- `src/sheets_client.py` — reads driver data from Google Sheets
- `src/load_provider.py` — load board data
- `src/sms_client.py` — Twilio SMS sender
- `agent_test.py` — AI agent loop (tool use pattern)

## Setup
1. Clone the repo
2. pip install -r requirements.txt
3. Copy .env.example to .env and fill in your keys
4. python agent_test.py

## Note
Currently runs with mock AI responses to demonstrate the agentic 
loop pattern. Plug in an Anthropic API key to enable real Claude AI.
=======
An AI agent that automatically finds suitable freight loads for truck drivers based on their location and truck type, then sends SMS notifications via Twilio.

## 🎯 How It Works

1. Reads active drivers from Google Sheets (name, location, truck type)
2. AI agent finds matching loads for each driver
3. Sends SMS notification to matched drivers automatically

## 🛠️ Tech Stack

- **Python** — core language
- **Claude AI** (Anthropic) — agentic tool use pattern
- **Google Sheets** — driver data storage
- **Twilio** — SMS notifications

## 📁 Project Structure
load-agent/
├── agent_test.py        # AI agent loop (tool use pattern)
├── src/
│   ├── sheets_client.py # Reads driver data from Google Sheets
│   ├── load_provider.py # Load board data
│   └── sms_client.py    # Twilio SMS sender
├── .env.example         # Environment variables template
└── requirements.txt

## ⚙️ Setup

1. Clone the repo
```bash
git clone https://github.com/yourusername/load-matching-ai-agent
cd load-matching-ai-agent
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
```bash
cp .env.example .env
# Fill in your API keys in .env
```

4. Run the agent
```bash
python agent_test.py
```

## 🔑 Environment Variables
GOOGLE_SHEET_ID=your_google_sheet_id
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM_NUMBER=your_twilio_number
ANTHROPIC_API_KEY=your_anthropic_key

## 📋 Google Sheets Format

| name | phone | city | state | lat | lon | truck_type | active |
|------|-------|------|-------|-----|-----|------------|--------|
| John Smith | +15551234567 | Dallas | TX | 32.7767 | -96.7970 | dry_van | yes |

## 📱 SMS Example
Hi John Smith! 🚛 New load match:
📍 Dallas, TX → Chicago, IL
💰 Rate: $3,200
📅 Pickup: 2025-05-10
Reply YES to accept or call dispatch.

## 📝 Note

Currently runs with mock AI responses to demonstrate the agentic loop pattern. Add an Anthropic API key to `.env` to enable real Claude AI.

## 👤 Author

Built as a learning project to explore AI agents, API integrations, and automation.
>>>>>>> 9fca93fed153d0451ad9b38a734a7d5a2a941474
