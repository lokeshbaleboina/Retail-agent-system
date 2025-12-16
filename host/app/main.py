from fastapi import FastAPI, Request
from host.app.graph import run_graph

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "MCP Host running"}


@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()

    # -------------------------------
    # STEP 1: Build initial STATE
    # -------------------------------
    state = {
        "user": payload.get("user", {}),
        "cart": payload.get("cart", {}),
        "channel": payload.get("channel", "web"),
        "intent": None,
        "messages": []
    }

    # ✅ MERGE OPTIONAL CONTEXT
    if "recommended_products" in payload:
        state["recommended_products"] = payload["recommended_products"]

    # Optional: user message
    if "message" in payload:
        state["messages"].append(payload["message"])

    # -------------------------------
    # STEP 2: Run Agentic Workflow
    # -------------------------------
    final_state = run_graph(state)

    # -------------------------------
    # STEP 3: Return final response
    # -------------------------------
    return {
        "reply": final_state["messages"][-1] if final_state["messages"] else "",
        "state": final_state
    }
