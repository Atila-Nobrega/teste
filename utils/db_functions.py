from utils.db import execute, fetch

async def db_inserir_camera(camera):
    query = """insert into camera(descricao, latitude, longitude) 
               values(:descricao, :latitude, :longitude)"""

    values = {"descricao": camera.descricao, "latitude": camera.latitude, "longitude": camera.longitude}

    await execute(query, False, values)


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

    await execute(query, False, values)


async def db_atualizar_camera(camera):
    query = """update camera set 
                descricao=:descricao, 
                latitude=:latitude, 
                longitude=:longitude
               where id=:id"""

    values = {"id": camera.id, "descricao": camera.descricao, "latitude": camera.latitude, "longitude": camera.longitude}

    await execute(query, False, values)