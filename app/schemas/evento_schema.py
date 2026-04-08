from pydantic import BaseModel

class Evento(BaseModel):
    titulo: str
    descricao: str
    data: str
    local: str
