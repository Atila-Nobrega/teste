CREATE TABLE camera (
	id serial NOT NULL,
	descricao varchar(80) NOT NULL,
	latitude double precision NOT NULL,
	longitude double precision NOT NULL,
	CONSTRAINT camera_pk PRIMARY KEY (id)
);