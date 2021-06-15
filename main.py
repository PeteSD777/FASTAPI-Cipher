from fastapi import FastAPI, Depends, status, HTTPException, Form
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from crypto import encodeFunction, decodeFunction
import secrets
from fastapi.responses import RedirectResponse
# local db is created at the beggining
db = []
# instance of FastAPI class is created
app = FastAPI()
# security for Basic Auth from FASTAPI is created
security = HTTPBasic()

# function get_current_user is responsible for checking if credential provided by completely fresh user are equal to those set in here


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    # sets the username to admin
    your_username = secrets.compare_digest(credentials.username, "admin")
    # sets the password to admin
    your_password = secrets.compare_digest(credentials.password, 'admin')
    # if credentials are invalid raises an error and asks for credentials again
    if not(your_username and your_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# data model for the phrases


class Phrase(BaseModel):
    phrase: str

# function redirects to the /docs endpoint of FASTAPI after successful log-in


@app.get("/login")
def check_current_user(username: str = Depends(get_current_user)):
    return RedirectResponse("/docs")

# basic root that will redirect to the login


@app.get("/")
async def root():
    return RedirectResponse("/login")

# endpoint for all the phrases


@app.get('/phrases')
def get_phrases():

    return db

# this function allows for making a POST request inside /docs.
# then it creates a new phrase and encodes in local db - "db"


@app.post('/phrase')
def write_phrase(phrase: Phrase):
    value = encodeFunction(phrase.phrase)
    db_decoded = value.decode("utf-8")
    db.append(db_decoded)

    return db

# after calling, this endpoint will encode the word again


@app.get('/encode/{phrase_id}')
def encode_phrase(phrase_id: int):
    value = encodeFunction(db[phrase_id-1])
    db[phrase_id-1] = value.decode("utf-8")

    return db[phrase_id-1]

# calling this endpoint in the browser, will decode the phrase


@app.get('/decode/{phrase_id}')
async def decode_phrase(phrase_id: int):
    value = decodeFunction(bytes(db[phrase_id-1], "utf-8"))
    db[phrase_id-1] = value

    return db[phrase_id-1]

# using it in fastapi docs route allows for decoding after inserting an id of a phrase


@ app.put('/decode/{phrase_id}')
async def decode_phrase(phrase_id: int):
    value = decodeFunction(bytes(db[phrase_id-1], "utf-8"))
    db[phrase_id-1] = value

    return db[phrase_id-1]

# using it in fastapi docs route allows for deleting a phrase by passing it's id


@ app.delete('/delete/{phrase_id}')
def delete_city(phrase_id: int):
    del db[phrase_id-1]
    return {}

# calling this endpoint in either docs or browser and passing id of a phrase, will show the phrase with passed id


@ app.get('/phrases/{phrase_id}')
def get_phrase_by_id(phrase_id: int):
    return db[phrase_id-1]
