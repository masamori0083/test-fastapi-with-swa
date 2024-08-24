from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()



class Item(BaseModel):
    message: str


@app.get("/api")
async def read_root():
    return {"message": "Hello World"}


@app.post('/api/echo')
async def echo(item: Item = Body(...)):
    print(f"received message: {item.message}")
    return {"receive": item.message}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

