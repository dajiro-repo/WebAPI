from sqlalchemy.orm import Session, aliased
from sqlalchemy import or_, and_
from create_db import *
from schemas import *

def get_tanuki(db_session: Session):
    return db_session.query(Tanuki).all()
