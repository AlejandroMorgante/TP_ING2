CREATE TABLE Cliente (

id_cliente INT AUTO_INCREMENT PRIMARY KEY,

nombre VARCHAR(100) NOT NULL,

direccion VARCHAR(200),

telefono VARCHAR(20),

correo VARCHAR(100)

);

CREATE TABLE Pais (

id_pais INT AUTO_INCREMENT PRIMARY KEY,

nombre VARCHAR(100) NOT NULL,

codigo_iso VARCHAR(10),

continente VARCHAR(50)

);

CREATE TABLE Ciudad (

id_ciudad INT AUTO_INCREMENT PRIMARY KEY,

nombre VARCHAR(100) NOT NULL,

codigo_postal VARCHAR(10),

tipo_de_zona VARCHAR(50),

id_pais INT,

FOREIGN KEY (id_pais) REFERENCES pais(id_pais)

);

CREATE TABLE Reserva (

id_reserva INT AUTO_INCREMENT PRIMARY KEY,

id_cliente INT,

fecha_rcreacion DATE,

estado VARCHAR(50),

precio DECIMAL(10,2),

FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)

);

CREATE TABLE Pasajero (

id_pasajero INT AUTO_INCREMENT PRIMARY KEY,

id_reserva INT,

nombre VARCHAR(100),

pasaporte VARCHAR(50),

FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva)

);

CREATE TABLE Vuelo (

id_vuelo INT AUTO_INCREMENT PRIMARY KEY,

numero_vuelo VARCHAR(20),

origen INT,

destino INT,

fecha_hora_salida DATETIME,

fecha_hora_llegada DATETIME,

aerolinea VARCHAR(100),

precio DECIMAL(10,2),

FOREIGN KEY (origen) REFERENCES ciudad(id_ciudad),

FOREIGN KEY (destino) REFERENCES ciudad(id_ciudad)

);

CREATE TABLE Hotel (

id_hotel INT AUTO_INCREMENT PRIMARY KEY,

nombre VARCHAR(100),

estrellas INT,

tipo_habitacion VARCHAR(50),

precio DECIMAL(10,2),

disponibilidad VARCHAR(30),

id_ciudad INT,

FOREIGN KEY (id_ciudad) REFERENCES ciudad(id_ciudad)

);

CREATE TABLE PaqueteTuristico (

id_paquete INT AUTO_INCREMENT PRIMARY KEY,

nombre VARCHAR(100),

descripcion TEXT,

precio_total DECIMAL(10,2)

);

CREATE TABLE Paquete_Vuelo (

id_paquete INT,

id_vuelo INT,

PRIMARY KEY (id_paquete, id_vuelo),

FOREIGN KEY (id_paquete) REFERENCES PaqueteTuristico(id_paquete),

FOREIGN KEY (id_vuelo) REFERENCES vuelo(id_vuelo)

);

CREATE TABLE Paquete_Hotel (

id_paquete INT,

id_hotel INT,

PRIMARY KEY (id_paquete, id_hotel),

FOREIGN KEY (id_paquete) REFERENCES PaqueteTuristico(id_paquete),

FOREIGN KEY (id_hotel) REFERENCES hotel(id_hotel)

);

CREATE TABLE Pago (

id_pago INT AUTO_INCREMENT PRIMARY KEY,

id_reserva INT,

metodo_de_pago VARCHAR(50),

monto DECIMAL(10,2),

fecha DATE,

estado VARCHAR(50),

FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva)

);

CREATE TABLE Reserva_Hotel (

id_reserva INT,

id_hotel INT,

PRIMARY KEY (id_reserva, id_hotel),

FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva),

FOREIGN KEY (id_hotel) REFERENCES Hotel(id_hotel)

);

CREATE TABLE Reserva_Vuelo (

id_reserva INT,

id_vuelo INT,

PRIMARY KEY (id_reserva, id_vuelo),

FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva),

FOREIGN KEY (id_vuelo) REFERENCES Vuelo(id_vuelo)

);

CREATE TABLE Reserva_Paquete (

id_reserva INT,

id_paquete INT,

PRIMARY KEY (id_reserva, id_paquete),

FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva),

FOREIGN KEY (id_paquete) REFERENCES PaqueteTuristico(id_paquete)

);