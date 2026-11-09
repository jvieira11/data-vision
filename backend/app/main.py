from fastapi import FastAPI

app = FastAPI(title="DataVision API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "funcionando"}
