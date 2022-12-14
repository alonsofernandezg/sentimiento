from multiprocessing import context
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd

from pysentimiento import create_analyzer
analyzer = create_analyzer(task="sentiment", lang="es")


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/index/', response_class=HTMLResponse)
def index(request: Request):
    result = "Type a text"
    context = {'request': request, 'result':result}
    return templates.TemplateResponse("index.html",context)


@app.post('/index/',response_class=HTMLResponse)
def index(request: Request, texto: str = Form()):
    result = analyzer.predict(texto)
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


  

@app.get('/files/', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("files.html",context)

@app.post("/files/")
async def upload_file(  
    fileup: UploadFile = File(...)):
    print(fileup.filename)
    contenido = pd.read_csv(fileup.file)
    comentarios=contenido.values.tolist()
    sentiment = analyzer.predict(comentarios)
    df=pd.DataFrame(sentiment, columns=['Sentimiento'])
    datos= pd.concat([contenido,df],axis=1)
    datos.to_csv('resultados.csv')
    return FileResponse('resultados.csv', media_type='text/csv', filename='resultados.csv')
    
    
    