from fastapi import FastAPI, Request
from host.app.graph import run_graph


app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "MCP Host running"}


@app.post("/webhook")
async def webhook(request: Request):
    """
    Entry point for all channels:
    - Web
    - Mobile App
    - WhatsApp
    - In-store Kiosk
    """

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

    # Optional: user message (chat-based flow)
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
