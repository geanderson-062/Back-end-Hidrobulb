from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from routers.router import router

app = FastAPI(
    title="API de simulação do Bulbo em camada superficial",
    description="Esta api fornece informações sobre os dados necessários para configurar uma simulação da camada superficial do bulbo úmido no software HYDRUS 3D. Ele descreve as propriedades do solo, as condições iniciais, as condições de contorno, os parâmetros climáticos, a geometria do domínio, o intervalo de tempo e as condições de saturação e drenagem.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
