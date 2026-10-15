from typing import Literal, Optional
from pydantic import BaseModel, Field

Channel = Literal["instagram", "x", "telegram", "linkedin", "seo", "email"]

class ProjectBrief(BaseModel):
    name: str
    offer: str
    audience: str
    goal: str = "qualified_customers"
    regions: list[str] = ["global"]
    languages: list[str] = ["en"]
    channels: list[Channel] = ["instagram", "x", "telegram", "seo"]

class ContentRequest(BaseModel):
    project: ProjectBrief
    theme: str
    count: int = Field(default=5, ge=1, le=25)

class Lead(BaseModel):
    source: str
    handle: Optional[str] = None
    company: Optional[str] = None
    intent_signal: str = ""
    fit_signal: str = ""
    engagement_score: int = Field(default=0, ge=0, le=100)

class OutreachRequest(BaseModel):
    project: ProjectBrief
    lead: Lead
    objective: Literal["conversation", "demo", "signup", "purchase"] = "conversation"

class FunnelMetrics(BaseModel):
    impressions: int = 0
    clicks: int = 0
    signups: int = 0
    activated: int = 0
    qualified_leads: int = 0
    customers: int = 0
    spend: float = 0.0
