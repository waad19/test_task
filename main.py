from fastapi import FastAPI
from pydantic import BaseModel


class MyNumber(BaseModel):
    my_number: str


app = FastAPI()


@app.get("/call")
def read_root():
    return {"Hello": "World"}


@app.post("/call_me")
def create_body(body: MyNumber):
    new_body = create_new_body(body.my_number)
    return new_body


def create_new_body(phone_number):
    new_body = {"Patient Last Name": None, "Patient First Name": None, "Patient DOB": None,
                "Patient Phone": phone_number, "Patient Alt Phone": None}
    return new_body
