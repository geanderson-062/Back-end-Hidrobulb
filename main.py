from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from endpoints.router import router

app = FastAPI(
    title="API de Comportamento do Solo",
    description="A API fornece endpoints para acessar diferentes aspectos do comportamento do solo, incluindo suas propriedades, condições iniciais, condições de contorno, parâmetros climáticos, geometria do domínio, intervalo de tempo e condições de saturação e drenagem.",
)

app.include_router(router)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
