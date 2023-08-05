from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Return(BaseModel):
    transaction_id: int
    title: str