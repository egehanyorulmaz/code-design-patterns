
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from validation.onboard_item_validator import OnboardItemValidator
from onboard import ExampleTriggerFactory

APP_NAME = "demo-pattern"
app = FastAPI(
    title="Fast-API airflow trigger",
    description="Snippet to explain dp with real world DE example, API to triggers airflow jobs",
    version=0.1,
)

@app.post(
    "/{tpa_shortcut}/trigger_inital",
    summary="Triggers initial run {tpa_shortcut}",
    description="Triggers the initial run and sets a daily schedule for incoming jobs. There are a total of 10 jobs, with the number increasing each day.",
)
async def trigger_historical(onboard_payload: dict, tpa_shortcut: str):
    # Determine and validate onboard item
    validator = OnboardItemValidator(tpa_shortcut)
    onboard_item = validator.validate_and_get_item(onboard_payload)

    # 
    handler = ExampleTriggerFactory.get_handler(onboard_item)
    airflow_response = handler.handle_trigger()


    return JSONResponse(
        status_code=status.HTTP_200_OK, content=({"detail": airflow_response})
    )