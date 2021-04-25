from pydantic import BaseModel

class Camera(BaseModel):
	id: int = None
	descricao: str
	latitude: float
	longitude: float