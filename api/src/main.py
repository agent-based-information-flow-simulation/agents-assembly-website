from typing import List

import uvicorn
from aasm import PanicException, __version__, get_spade_code
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.settings import app_settings


class AgentsAssemblyCode(BaseModel):
    code_lines: List[str]


class SpadeCode(BaseModel):
    translator_version: str
    code_lines: List[str]


app = FastAPI(root_path="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[app_settings.client_cors_domain],
    allow_methods=["POST"],
)


@app.exception_handler(PanicException)
async def PanicExceptionHandler(request: Request, exception: PanicException):
    return JSONResponse(
        status_code=400,
        content={
            "translator_version": __version__,
            "place": exception.place,
            "reason": exception.reason,
            "suggestion": exception.suggestion,
        },
    )


@app.post("/code/spade", response_model=SpadeCode)
async def post_aasm_code(agent_assembly_code: AgentsAssemblyCode):
    return {
        "translator_version": __version__,
        "code_lines": get_spade_code(agent_assembly_code.code_lines),
    }


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=app_settings.port,
        reload=app_settings.enable_reload,
    )
