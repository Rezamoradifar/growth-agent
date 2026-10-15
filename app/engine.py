from __future__ import annotations
from .models import ProjectBrief, ContentRequest, Lead, OutreachRequest, FunnelMetrics

class GrowthEngine:
    def plan(self, p: ProjectBrief) -> dict:
        experiments = []
        for ch in p.channels:
            experiments.append({
                "channel": ch,
                "hypothesis": f"A high-signal {ch} campaign can attract {p.audience}",
                "primary_kpi": "activated_users" if ch != "email" else "qualified_replies",
                "budget_rule": "start_small_then_scale_winners",
            })
        return {
            "project": p.name,
            "north_star": "qualified_customers",
            "daily_loop": ["research", "create", "distribute", "capture", "qualify", "follow_up", "analyze"],
            "experiments": experiments,
            "guardrails": ["no_fake_engagement", "no_mass_unsolicited_dm", "official_apis_only", "approval_for_outbound"],
        }

    def content(self, req: ContentRequest) -> list[dict]:
        hooks = [
            "The costly mistake most people make before choosing this solution",
            "What changed after we simplified the process",
            "3 things buyers should check before they commit",
            "A 30-second demonstration of the core value",
            "Myth vs reality: what actually matters",
        ]
        items = []
        i = 0
        for channel in req.project.channels:
            if i >= req.count: break
            items.append({
                "channel": channel,
                "hook": hooks[i % len(hooks)],
                "theme": req.theme,
                "format": "short_video" if channel == "instagram" else "native_post",
                "cta": "Reply or visit the landing page for the next step",
                "test": f"creative_{i+1}",
            })
            i += 1
        while len(items) < req.count:
            idx = len(items)
            ch = req.project.channels[idx % len(req.project.channels)]
            items.append({"channel": ch, "hook": hooks[idx % len(hooks)], "theme": req.theme, "format": "variant", "cta": "Learn more", "test": f"creative_{idx+1}"})
        return items

    def score_lead(self, lead: Lead) -> dict:
        score = lead.engagement_score
        text = (lead.intent_signal + " " + lead.fit_signal).lower()
        for kw, pts in [("price",12),("demo",18),("buy",22),("need",12),("looking",10),("budget",12),("urgent",12)]:
            if kw in text: score += pts
        score = min(score, 100)
        band = "hot" if score >= 75 else "warm" if score >= 45 else "cold"
        return {"score": score, "band": band, "next_action": "personal_follow_up" if band != "cold" else "nurture"}

    def outreach(self, req: OutreachRequest) -> dict:
        lead = req.lead
        personalization = lead.intent_signal.strip() or lead.fit_signal.strip() or "your recent interest"
        body = (
            f"Hi — I noticed {personalization}. We’re working on {req.project.offer} for {req.project.audience}. "
            f"If it’s relevant, I can send a concise overview tailored to what you’re trying to achieve."
        )
        return {"draft": body, "requires_approval": True, "objective": req.objective}

    def decide(self, m: FunnelMetrics) -> dict:
        ctr = m.clicks / m.impressions if m.impressions else 0
        activation = m.activated / m.signups if m.signups else 0
        conversion = m.customers / m.qualified_leads if m.qualified_leads else 0
        cac = m.spend / m.customers if m.customers else None
        if m.impressions >= 1000 and ctr < 0.005:
            action = "KILL_OR_REWORK_CREATIVE"
        elif m.signups >= 30 and activation < 0.15:
            action = "FIX_ONBOARDING"
        elif m.qualified_leads >= 10 and conversion >= 0.2:
            action = "SCALE"
        else:
            action = "ITERATE"
        return {"action": action, "ctr": round(ctr,4), "activation_rate": round(activation,4), "lead_to_customer": round(conversion,4), "cac": cac}
