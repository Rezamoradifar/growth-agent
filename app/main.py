from fastapi import FastAPI
from .models import ProjectBrief, ContentRequest, Lead, OutreachRequest, FunnelMetrics
from .engine import GrowthEngine

app = FastAPI(title="Autonomous Growth Agent", version="0.1.0")
engine = GrowthEngine()

@app.get("/health")
def health():
    return {"ok": True, "agent": "growth-agent", "version": "0.1.0"}

@app.post("/campaigns/plan")
def campaign_plan(project: ProjectBrief):
    return engine.plan(project)

@app.post("/content/generate")
def content_generate(req: ContentRequest):
    return {"items": engine.content(req)}

@app.post("/leads/score")
def leads_score(lead: Lead):
    return engine.score_lead(lead)

@app.post("/outreach/draft")
def outreach_draft(req: OutreachRequest):
    return engine.outreach(req)

@app.post("/analytics/decision")
def analytics_decision(metrics: FunnelMetrics):
    return engine.decide(metrics)
