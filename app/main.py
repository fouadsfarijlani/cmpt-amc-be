from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def test_fast_api():
    return {"message": "hello world"}