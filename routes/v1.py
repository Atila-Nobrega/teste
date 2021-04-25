from fastapi import FastAPI, Body, APIRouter
from utils.db import execute, fetch
from models.camera import Camera
from models.registro import Registro
from utils.db_functions import (
    db_inserir_camera,
    db_pegar_camera,
    db_pegar_todas_cameras,
    db_remover_camera,
    db_atualizar_camera
)

app_v1 = APIRouter()


@app_v1.post("/camera")
async def post_camera(camera: Camera):
	await db_inserir_camera(camera)
	return {"Resultado": "Camera criada"}


@app_v1.get("/camera/{id}")
async def get_camera(id: int):
	camera = await db_pegar_camera(id)

	if camera is not None:
		return {"camera": camera}
	else:
		return {"Resultado": "Sem camera com tal id"}


@app_v1.get("/cameras")
async def get_cameras():
	cameras = await db_pegar_todas_cameras()

	if cameras is not None:
		return {"cameras": cameras}
	else:
		return {"Resultado": "Nenhuma camera existente"}


@app_v1.delete("/camera")
async def delete_camera(id: int = Body(..., embed=True)):
	await db_remover_camera(id)
	return {"Resultado": "Camera removida"}


@app_v1.put("/camera")
async def put_camera(camera: Camera):
	if camera.id is not None:
		await db_atualizar_camera(camera)
		
		return {"Resultado": "Camera atualizada"}
	else:
		return {"Resultado": "É preciso inserir um id"}
		
