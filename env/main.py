from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello World"} 

# @app.get("/Kp/")
# async def get_books():
#     return kp_db

RFS_db = [
    {
        "Kp" : "0.7",
    },
    {
        "R" : "99",
    },
    {
        "Dst" : "4",
    },
    {
        "ap" : "3",
    },
    {
        "F107" : "113.9",
    },
    {
        "RFS" : "No",
    },
]

@app.get("/RFS_db /")
async def root():
    return RFS_db 