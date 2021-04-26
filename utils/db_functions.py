from utils.db import execute, fetch

async def db_inserir_camera(camera):
	query = """insert into camera(id, descricao, latitude, longitude, streamurl) 
			   values(:id, :descricao, :latitude, :longitude, :streamurl)"""

	values = {"id": camera.id, "descricao": camera.descricao, "latitude": camera.latitude, "longitude": camera.longitude, "streamurl": camera.streamurl}
	
	if await fetch("""SELECT id FROM camera WHERE id=:id""", True, {"id": camera.id}) is None:
		await execute(query, False, values)
		return True
	else:
		return False


async def db_pegar_camera(id):
	query = """select * from camera where id=:id"""
	values = {"id": id}

	camera = await fetch(query, True, values)
	
	return camera


async def db_pegar_todas_cameras():
	query = """select * from camera"""
	values = dict()

	cameras = await fetch(query, False, values)
	
	return cameras


async def db_remover_camera(id):
	query = """delete from camera where id=:id"""
	values = {"id": id}

	if await fetch("""SELECT id FROM camera WHERE id=:id""", True, values) is None:
		return False
	else:
		await execute(query, False, values)
		return True


async def db_atualizar_camera(camera):
	query = """update camera set 
				descricao=:descricao, 
				latitude=:latitude, 
				longitude=:longitude,
				streamurl=:streamurl
			   where id=:id"""

	values = {"id": camera.id, "descricao": camera.descricao, "latitude": camera.latitude, "longitude": camera.longitude, "streamurl": camera.streamurl}

	await execute(query, False, values)