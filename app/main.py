from fastapi import FastAPI, HTTPException

app = FastAPI(title="Demo API", version="1.0.0")


@app.get("/health")
async def health_check():
    """Health check endpoint returning status ok."""
    return {"status": "ok"}


@app.post("/echo")
async def echo_message(body: dict):
    """Echo back a JSON message.

    Expects: {"message": "string"}
    Returns: {"message": "string"}
    """
    if "message" not in body:
        raise HTTPException(status_code=400, detail="Missing required field: message")
    return {"message": body["message"]}
