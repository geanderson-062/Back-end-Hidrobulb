from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from endpoints.router import router

app = FastAPI()

app.include_router(router)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
