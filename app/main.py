from routes.produto_routes import router as produto_router
from routes.setor_routes import router as setor_router
from routes.usuario_routes import router as usuario_router
from fastapi import FastAPI
app = FastAPI()
@app.get('/health-check') 
def health_check():
    return True
app.include_router(setor_router, tags=["Setores"])
app.include_router(produto_router, tags=["Produtos"])
app.include_router(usuario_router, tags=["Usuarios"])


if __name__ == "__main__":
    import uvicorn
#                  #nomearquivo#nomeAppMain   
    uvicorn.run("main:app", host="127.0.0.1", port=8003, reload=True)