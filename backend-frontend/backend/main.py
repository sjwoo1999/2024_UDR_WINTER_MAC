from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
db = []


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.get('/pastes')
def get_pastes():
    return db


@app.get('/paste/{paste_id}')
def get_paste(paste_id: int):
    if paste_id < len(db):
        return {'paste_id': paste_id,
                'paste': db[paste_id]}
    else:
        return {'paste_id': paste_id,
                'paste': None}
    
    
class Paste(BaseModel):
    content: str


@app.post('/paste/')
def post_paste(paste: Paste):
    db.append(paste)
    paste_id = len(db)-1
    return {'paste_id': paste_id,
            'paste': db[paste_id]}


@app.put('/paste/{paste_id}')
def put_paste(paste_id: int, paste: Paste):
    if paste_id >= len(db):
        for i in range(len(db), paste_id+1, 1):
            db.append({'paste_id': i,
                       'paste': None})
    db[paste_id] = paste
    return {'paste_id': paste_id, 
            'paste': paste}


@app.delete('/paste/{paste_id}')
def delete_paste(paste_id:int):
    if paste_id < len(db):
        db[paste_id] = None
        return {'paste_id': paste_id,
                'paste': db[paste_id]}
    else:
        return {'paste_id': paste_id,
                'paste': None}
