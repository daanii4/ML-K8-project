from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Define the structure of the input request
class AdPrompt(BaseModel):
    brand_name: str
    ad_goal: str

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Ad Campaign Generator"}

# Endpoint to handle the ad prompt and generate content
@app.post("/generate_ad/")
def generate_ad(prompt: AdPrompt):
    # Example output format
    return {
        "brand_name": prompt.brand_name,
        "ad_goal": prompt.ad_goal,
        "image": generate_image(prompt.brand_name),
        "video": generate_video(prompt.brand_name),
        "ad_copy": generate_ad_copy(prompt.ad_goal)
    }

