from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Backend Python na Azure"}

@app.get("/dados")
async def get_dados():
    return {"dados": "Exemplo de resposta JSON"}
