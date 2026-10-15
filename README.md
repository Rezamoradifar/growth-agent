# Autonomous Growth Agent

A production-oriented starter for a multi-channel growth agent.

## What it does
- Builds daily growth experiments
- Generates content briefs for Instagram / X / Telegram / LinkedIn / SEO
- Scores leads and prioritizes high-intent prospects
- Creates compliant personalized outreach drafts (no spam blasts)
- Tracks funnel metrics and recommends SCALE / ITERATE / KILL
- Keeps all outbound actions behind an approval gate by default

## Quick start
```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8787
```

Open `http://localhost:8787/docs`.

## Core endpoints
- `POST /campaigns/plan` — build a daily campaign plan
- `POST /content/generate` — create channel-specific content briefs
- `POST /leads/score` — score incoming leads
- `POST /outreach/draft` — create personalized outreach copy
- `POST /analytics/decision` — SCALE / ITERATE / KILL decision
- `GET /health` — service health

## Safe growth rules
This starter intentionally blocks mass unsolicited DMs, fake engagement, follow/unfollow automation, credential scraping, and deceptive growth. Use official platform APIs and consent-based or contextually relevant outreach.

## Connecting real channels
Fill `.env` with official API credentials, then implement/enable the corresponding adapter under `connectors/`.

Recommended first integrations:
1. Meta Graph API (Instagram business account)
2. Telegram Bot API
3. X API
4. CRM / Google Sheets
5. Analytics (GA4 / PostHog)
6. Ads APIs after organic creatives have winners

## Growth operating model
Research → Content → Distribution → Lead capture → Qualification → Follow-up → Conversion → Referral → Analysis → Repeat

The KPI engine optimizes for activated users and customers, not vanity followers.
