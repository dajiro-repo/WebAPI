import io
from typing import Optional, List, Tuple
import pandas as pd

from sqlalchemy.orm import Session, sessionmaker, aliased

from fastapi import Depends, FastAPI, Response
from fastapi.openapi.utils import get_openapi
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

from starlette.requests import Request
from starlette.templating import Jinja2Templates

from crud import *
from dump import *
from create_db import *
from setting import ENGINE

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


"""
tanuki API
"""
@app.get("/v1/tanuki/", tags=["Tanuki"])
async def read_tanuki(db:Session = Depends(get_db)):
        tanuki = get_tanuki(db)
        df = dumpTanuki(tanuki)
    
        stream = io.StringIO()
        df.to_csv(stream, index = False)
        response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
        
        response.headers["Content-Disposition"] = "attachment; filename=export.csv"

        return response

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env

async def table(request: Request, db:Session = Depends(get_db)):
        tanuki = get_tanuki(db)
        return templates.TemplateResponse('index.html',
	    			      {'request': request, "tanuki": tanuki})
app.add_api_route('/table', table)

"""
setting
"""
def setting_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Tanuki API",
        version="v1",
        description="Tanuki family",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = setting_openapi
