from fastapi import FastAPI
from analyzer import analyze_log
app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI DevOps Log Analyzer API Running"}

@app.post("/analyze")
def analyze(log: str):
    result = analyze_log(log)
    return {"analysis": result}
