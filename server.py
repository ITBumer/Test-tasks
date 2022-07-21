import json
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from web import html

app = FastAPI()


@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    number = 0
    while True:
        data = json.dumps(await websocket.receive_text(),ensure_ascii=False)
        number +=1
        data2 = ("\n".join(f"{i+number}) "+j for i,j in enumerate(data.split())))
        await websocket.send_text(f"{data2}")