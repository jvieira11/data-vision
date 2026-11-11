from fastapi import FastAPI

app = FastAPI(title="DataVision API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "funcionando"}


@app.get("/version")
def version_check() -> dict[str, str]:
    return {"version": "0.1.0"}
