from fastapi import FastAPI
from pydantic import BaseModel

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_output
from pipeline.repair_engine import repair_output
from pipeline.runtime_simulator import simulate_runtime

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI App Compiler API Running"}


class UserPrompt(BaseModel):
    prompt: str


@app.post("/generate")
def generate_app(data: UserPrompt):

    try:

        # Stage 1
        intent = extract_intent(data.prompt)

        # Stage 2
        architecture = design_system(intent)

        # Stage 3
        generated_schema = generate_schema(architecture)

        # Stage 4
        validation_result = validate_output(
            generated_schema
        )

        # Stage 5
        if not validation_result["valid"]:
            generated_schema = repair_output(
                generated_schema,
                validation_result["errors"]
            )

        # Stage 6
        runtime_result = simulate_runtime(
            generated_schema
        )

        return {
            "success": True,
            "intent": intent,
            "architecture": architecture,
            "schema": generated_schema,
            "runtime": runtime_result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }