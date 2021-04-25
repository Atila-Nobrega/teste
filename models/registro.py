from pydantic import BaseModel
from models.camera import Camera

class Registro(BaseModel):
	id: int = None
	placa: str
	horario: int
	camera: Camera