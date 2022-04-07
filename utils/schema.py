from typing import List
from ninja import Schema

class ErrorMessage(Schema):
    name: str
    reason: str

class ErrorOut(Schema):
    """
        Error Schema based on https://datatracker.ietf.org/doc/html/rfc7807
    """
    status: int
    title: str
    detail: str = None
    type: str = None
    errors: List[ErrorMessage]= []
