from pydantic import BaseModel
from typing import Optional, Dict, Any


class ComposeInput(BaseModel):
    category: Dict[str, Any]
    merchant: Dict[str, Any]
    trigger: Dict[str, Any]
    customer: Optional[Dict[str, Any]] = None