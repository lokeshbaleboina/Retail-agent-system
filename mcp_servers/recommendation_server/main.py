from fastapi import FastAPI
from pydantic import BaseModel
from .tools.getRecommendations import get_recommendations

app = FastAPI()


class RecommendationRequest(BaseModel):
    occasion: str = "general"


@app.get("/")
def health():
    return {"status": "Recommendation MCP Server running"}


@app.post("/getRecommendations")
def recommend(req: RecommendationRequest):
    return get_recommendations(req.occasion)
