CREATE TABLE camera (
	id int,
	descricao varchar(80) NOT NULL,
	latitude double precision NOT NULL,
	longitude double precision NOT NULL,
	streamurl text,
	CONSTRAINT camera_pk PRIMARY KEY (id)
);