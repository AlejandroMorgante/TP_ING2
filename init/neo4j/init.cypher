// Limpiar todo el grafo antes de crear nodos y relaciones (solo en desarrollo)
MATCH (n) DETACH DELETE n;

// Nodos
CREATE (:Cliente {id: 1, nombre: "Juan Pérez", email: "juan@gmail.com", telefono: "12345678"});
CREATE (:Reserva {id: 100, fecha: date("2024-07-01"), estado: "confirmada"});
CREATE (:Persona {nombre: "Luis Gómez", pasaporte: "AB123456"});
CREATE (:Hotel {id: 201, nombre: "Hotel Paraíso", direccion: "Av. Playa 123", estrellas: 5, precio_noche: 90, zona: "centro"});
CREATE (:Ciudad {nombre: "Cancún", codigo_postal: "77500", tropical: true});
CREATE (:Pais {nombre: "México", codigo: "MX", continente: "América"});
CREATE (:Pago {id: 500, metodo: "tarjeta", monto: 1200, fecha: date("2024-07-01"), estado: "aprobado"});
CREATE (:Vuelo {id: 301, nroVuelo: "AR123", origen: "Buenos Aires", destino: "Cancún", fecha: date("2024-07-01"), precio: 600, aerolinea: "Aerolíneas Argentinas"});
CREATE (:Paquete {id: 401, nombre: "Paquete Caribe", descripcion: "7 días all inclusive", precio_total: 2000});

// Relaciones
MATCH (c:Cliente {id: 1}), (r:Reserva {id: 100})
CREATE (c)-[:REALIZO]->(r);

MATCH (r:Reserva {id: 100}), (p:Persona {pasaporte: "AB123456"})
CREATE (r)-[:INCLUYE_PERSONA]->(p);

MATCH (r:Reserva {id: 100}), (h:Hotel {id: 201}), (v:Vuelo {id: 301})
CREATE (r)-[:INCLUYE_HOTEL]->(h),
       (r)-[:INCLUYE_VUELO]->(v);

MATCH (r:Reserva {id: 100}), (pa:Pago {id: 500})
CREATE (r)-[:TIENE_PAGO]->(pa);

MATCH (h:Hotel {id: 201}), (ci:Ciudad {nombre: "Cancún"})
CREATE (h)-[:UBICADO_EN]->(ci);

MATCH (ci:Ciudad {nombre: "Cancún"}), (p:Pais {nombre: "México"})
CREATE (ci)-[:PERTENECE_A]->(p);

MATCH (paquete:Paquete {id: 401}), (h:Hotel {id: 201}), (v:Vuelo {id: 301})
CREATE (paquete)-[:INCLUYE_HOTEL]->(h),
       (paquete)-[:INCLUYE_VUELO]->(v);

MATCH (r:Reserva {id: 100}), (paquete:Paquete {id: 401})
CREATE (r)-[:INCLUYE_PAQUETE]->(paquete);

// Consultas
MATCH (r:Reserva)-[:INCLUYE_HOTEL]->(h:Hotel)-[:UBICADO_EN]->(c:Ciudad)
WHERE h.estrellas > 4 AND c.tropical = true
RETURN count(DISTINCT r) AS reservas_tropicales_con_mas_de_4_estrellas;

MATCH (r:Reserva)-[:INCLUYE_HOTEL]->(h:Hotel)-[:UBICADO_EN]->(c:Ciudad)
WHERE h.estrellas > 4 AND c.tropical = true
RETURN r,h,c;