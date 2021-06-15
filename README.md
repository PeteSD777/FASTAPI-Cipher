# Fastapi-cipher
Made with FASTAPI, that allows for operations of encoding and decoding phrases

Fastapi-cipher has been created to encode and decode phrases by calling FastAPI docs route and by calling endpoints inside the browser.
Fastapi-cipher uses python FastAPI framework to provide endpoints for requests. This project also uses python cryptography library, to ensure more security when encoding.
To begin using this project, a new user is asked to enter credentials inside FastAPI BasicAuth popup. After completing this step, user is able to start using functions 
provided by this project. The credentials for the BasicAuth are: username:admin password:admin.Starting the encryption with the modified version od Caesar's cipher that additionally uses numbers, I was able to pre-encode phrases which later are
treated with the second, stronger encryption, Fernet cipher. Mixing both of those algorithms, I was able to ensure a double check for secure encoding. Starting encoding begins
with the post method used in FastAPI docs route. After creating the first instance of the phrase, user is able to decode and encode his phrase, by calling endpoints from address
bar of a browser or by using FastAPI docs route.




How to use Fastapi-cipher?
To begin using Fastapi-cipher, we need to install 2 dependencies, with commands:
1. FastAPI, installed with command:
pip install fastapi[all]
2. Cryptography library, installed with command:
pip install cryptography
After installation, we are ready to use Fastapi-cipher

Inside command line, enter the route of this downloaded project.
Run uvicorn main:app --reload
Go to the address provided inside command line
the address should be http://127.0.0.1:8000/
Entering this address, we are asked about credentials for FastAPI Basic Auth. username: admin password:admin
Nowm we are redirected to the docs route. 
To explore phrases, we need to head to the post /phrase in the UI. In here, we are should insert our phrase by using try it out button confirm changes.
Phrase is added to the list, serving as local db.
New phrase will have an id of 1, id's of every next phrase will have an incremental value of id

To see the phrase, head to /phrases/1 endpoint, or use /phrases/{phrases_id} in FastAPI docs route

To decode the phrase, head to /decode/1 endpoint, or use /decode/{phrases_id} in FastAPI docs route

To encode the phrase again, head to /encode/1 endpoint, or use /encode/{phrases_id} in FastAPI docs route

To delete the phrase, use /delete/{phrases_id} in Fastapi docs route

To get the list of all the phrases head to /phrases/ endpoint or use /phrases/ in FastAPI docs route

Remember, once entered proper credentials, are stored in the browser. Use fresh incognito mode to perform BasicAuth Again
