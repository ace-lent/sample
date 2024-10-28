from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

class Calculation(BaseModel):
    operation: str
    num1: float
    num2: float

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate(calc: Calculation):
    if calc.operation == "add":
        result = calc.num1 + calc.num2
    elif calc.operation == "subtract":
        result = calc.num1 - calc.num2
    elif calc.operation == "multiply":
        result = calc.num1 * calc.num2
    elif calc.operation == "divide":
        result = calc.num1 / calc.num2 if calc.num2 != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operation"
    return {"result": result}
