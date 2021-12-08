from typing import List
from fastapi.encoders import jsonable_encoder

import uvicorn
from aasm import PanicException, __version__, get_spade_code
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse


class AgentsAssemblyCode(BaseModel):
    code_lines: List[str]


class SpadeCode(BaseModel):
    translator_version: str
    code_lines: List[str]


app = FastAPI()
cors_origins = ["http://localhost:3000"]
cors_methods = ["POST"]
app.add_middleware(
    CORSMiddleware, allow_origins=cors_origins, allow_methods=cors_methods
)


@app.exception_handler(PanicException)
async def MyCustomExceptionHandler(request: Request, exception: PanicException):
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
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
