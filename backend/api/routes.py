from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from api.models import User, AgnoResult
from api.agno_handler import process_agno
from pydantic import BaseModel
from typing import List

router = APIRouter()

class AgnoRequest(BaseModel):
    input_text: str

@router.post("/process-agno", response_model=dict)
def process_agno_request(request: AgnoRequest, db: Session = Depends(get_db)):
    """
    Menerima input text dari user, memproses dengan Agno, dan menyimpan hasilnya.
    """
    try:
        result = process_agno(request.input_text)
        db_result = AgnoResult(input_text=request.input_text, output_result=result)
        db.add(db_result)
        db.commit()
        return {"input": request.input_text, "output": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
