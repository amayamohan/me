from fastapi import FastAPI,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from database import insert_data

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name ="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", "r",encoding="utf-8") as file:  
        return file.read()
    
@app.post("/", response_class=HTMLResponse)
async def save_contact(name: str = Form(...),email: str = Form(...),message: str = Form(...)):
    insert_data(name, email, message)
    
    return "Contact information submitted succesfully"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
