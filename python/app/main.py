from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import paho.mqtt.client as mqtt
import pika

app = FastAPI(title="Python Service API & WebSocket")

@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "Python FastAPI Service Running Successfully!",
        "services": ["REST API", "WebSocket", "MQTT Client", "RabbitMQ Client"]
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Terhubung ke Python WebSocket Server!")
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Pesan diterima via WebSocket: {data}")
    except WebSocketDisconnect:
        print("Client terputus dari WebSocket")