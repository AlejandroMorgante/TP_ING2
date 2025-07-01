-- init/mysql/init.sql (con DROP TABLE IF EXISTS agregado)

DROP TABLE IF EXISTS Reserva_Paquete;
DROP TABLE IF EXISTS Reserva_Vuelo;
DROP TABLE IF EXISTS Reserva_Hotel;
DROP TABLE IF EXISTS Pago;
DROP TABLE IF EXISTS Paquete_Hotel;
DROP TABLE IF EXISTS Paquete_Vuelo;
DROP TABLE IF EXISTS PaqueteTuristico;
DROP TABLE IF EXISTS Hotel;
DROP TABLE IF EXISTS Vuelo;
DROP TABLE IF EXISTS Pasajero;
DROP TABLE IF EXISTS Reserva;
DROP TABLE IF EXISTS Ciudad;
DROP TABLE IF EXISTS Pais;
DROP TABLE IF EXISTS Cliente;

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
  FOREIGN KEY (id_pais) REFERENCES Pais(id_pais)
);

CREATE TABLE Reserva (
  id_reserva INT AUTO_INCREMENT PRIMARY KEY,
  id_cliente INT,
  fecha_rcreacion DATE,
  estado VARCHAR(50),
  precio DECIMAL(10,2),
  FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE Pasajero (
  id_pasajero INT AUTO_INCREMENT PRIMARY KEY,
  id_reserva INT,
  nombre VARCHAR(100),
  pasaporte VARCHAR(50),
  FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva)
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
  FOREIGN KEY (origen) REFERENCES Ciudad(id_ciudad),
  FOREIGN KEY (destino) REFERENCES Ciudad(id_ciudad)
);

CREATE TABLE Hotel (
  id_hotel INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  estrellas INT,
  tipo_habitacion VARCHAR(50),
  precio DECIMAL(10,2),
  disponibilidad VARCHAR(30),
  id_ciudad INT,
  FOREIGN KEY (id_ciudad) REFERENCES Ciudad(id_ciudad)
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
  FOREIGN KEY (id_vuelo) REFERENCES Vuelo(id_vuelo)
);

CREATE TABLE Paquete_Hotel (
  id_paquete INT,
  id_hotel INT,
  PRIMARY KEY (id_paquete, id_hotel),
  FOREIGN KEY (id_paquete) REFERENCES PaqueteTuristico(id_paquete),
  FOREIGN KEY (id_hotel) REFERENCES Hotel(id_hotel)
);

CREATE TABLE Pago (
  id_pago INT AUTO_INCREMENT PRIMARY KEY,
  id_reserva INT,
  metodo_de_pago VARCHAR(50),
  monto DECIMAL(10,2),
  fecha DATE,
  estado VARCHAR(50),
  FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva)
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

INSERT INTO Cliente (nombre, direccion, telefono, correo)
VALUES ('Juan Pérez', 'Av. Siempreviva 123', '123456789', 'juan.perez@email.com');

INSERT INTO Pais (nombre, codigo_iso, continente)
VALUES ('México', 'MX', 'América');

INSERT INTO Ciudad (nombre, codigo_postal, tipo_de_zona, id_pais)
VALUES ('Cancún', '77500', 'tropical', 1);

INSERT INTO Reserva (id_cliente, fecha_rcreacion, estado, precio)
VALUES (1, '2024-07-01', 'confirmada', 2000.00);

INSERT INTO Pasajero (id_reserva, nombre, pasaporte)
VALUES (1, 'Luis Gómez', 'AB123456');

INSERT INTO Vuelo (numero_vuelo, origen, destino, fecha_hora_salida, fecha_hora_llegada, aerolinea, precio)
VALUES ('AR123', 1, 1, '2024-07-01 08:00:00', '2024-07-01 12:00:00', 'Aerolíneas Argentinas', 600.00);

INSERT INTO Hotel (nombre, estrellas, tipo_habitacion, precio, disponibilidad, id_ciudad)
VALUES ('Hotel Paraíso', 5, 'suite', 90.00, 'disponible', 1);

INSERT INTO PaqueteTuristico (nombre, descripcion, precio_total)
VALUES ('Paquete Caribe', '7 días all inclusive', 2000.00);

INSERT INTO Paquete_Vuelo (id_paquete, id_vuelo)
VALUES (1, 1);

INSERT INTO Paquete_Hotel (id_paquete, id_hotel)
VALUES (1, 1);

INSERT INTO Pago (id_reserva, metodo_de_pago, monto, fecha, estado)
VALUES (1, 'tarjeta', 2000.00, '2024-07-01', 'aprobado');

INSERT INTO Reserva_Hotel (id_reserva, id_hotel)
VALUES (1, 1);

INSERT INTO Reserva_Vuelo (id_reserva, id_vuelo)
VALUES (1, 1);

INSERT INTO Reserva_Paquete (id_reserva, id_paquete)
VALUES (1, 1);