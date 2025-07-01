db.propiedades.drop();

db.propiedades.insertMany([
  {
    nombre: "Hotel Paraiso",
    tipoAlojamiento: "estándar",
    ubicacion: { ciudad: "Cartagena", pais: "Colombia" },
    fechaAlta: ISODate("2025-06-10T12:00:00Z"),
    estrellas: 4,
    precioNoche: 150
  },
  {
    nombre: "Depto Centro Madrid",
    tipoAlojamiento: "estándar",
    ubicacion: { ciudad: "Madrid", pais: "España" },
    fechaAlta: ISODate("2025-06-15T09:30:00Z"),
    estrellas: null,
    precioNoche: 80
  },
  {
    nombre: "Hostal Andino",
    tipoAlojamiento: "doble",
    ubicacion: { ciudad: "Cusco", pais: "Perú" },
    fechaAlta: ISODate("2025-06-18T17:45:00Z"),
    estrellas: 2,
    precioNoche: 25
  },
  {
    nombre: "Hostal Viejo",
    tipoAlojamiento: "suite",
    ubicacion: { ciudad: "Cusco", pais: "Perú" },
    fechaAlta: ISODate("2010-06-18T17:45:00Z"),
    estrellas: 2,
    precioNoche: 25
  }
]);

db.propiedades.createIndex({ fechaAlta: -1 });


db.reservas.drop();
db.reservas.insertMany([
  {
    numero_reserva: "R001",
    fecha_creacion: ISODate("2025-06-01T00:00:00Z"),
    estado: "confirmada",
    precio: 1200,
    cliente: {
      nombre: "Carlos Martínez",
      correo: "carlos.martinez@email.com"
    },
    pasajeros: [
      {
        nombre: "Carlos Martínez",
        pasaporte: "MX1234567"
      }
    ],
    paquete: {
      descripcion: "Vacaciones en Cancún",
      precio_total: 1200,
      hotel: {
        nombre: "Hotel Caribe Azul",
        tipo_habitacion: "doble",
        zona: "centro",
        estrellas: 5,
        precio: 150
      },
      vuelo: {
        origen: "Ciudad de México",
        destino: "Cancún",
        aerolinea: "Volaris",
        fecha_hora: ISODate("2025-07-15T09:00:00Z")
      }
    }
  },
  {
    numero_reserva: "R002",
    fecha_creacion: ISODate("2025-06-10T00:00:00Z"),
    estado: "pendiente",
    precio: 500,
    cliente: {
      nombre: "Lucía Gómez",
      correo: "lucia.gomez@email.com"
    },
    pasajeros: [
      {
        nombre: "Lucía Gómez",
        pasaporte: "AR9876543"
      }
    ],
    vuelo: {
      origen: "Buenos Aires",
      destino: "Bariloche",
      aerolinea: "Aerolineas Argentinas",
      fecha_hora: ISODate("2025-07-10T13:00:00Z")
    }
  },
  {
    numero_reserva: "R003",
    fecha_creacion: ISODate("2025-06-12T00:00:00Z"),
    estado: "cancelada",
    precio: 700,
    cliente: {
      nombre: "Pedro López",
      correo: "pedro.lopez@email.com"
    },
    pasajeros: [
      {
        nombre: "Pedro López",
        pasaporte: "CL4567890"
      }
    ],
    hotel: {
      nombre: "Hotel del Lago",
      tipo_habitacion: "suite",
      zona: "playa",
      estrellas: 4,
      precio: 200
    }
  },
  {
    numero_reserva: "R004",
    fecha_creacion: ISODate("2025-06-01T00:00:00Z"),
    estado: "confirmada",
    precio: 1300,
    cliente: {
      nombre: "Ana Torres",
      correo: "ana.torres@email.com"
    },
    pasajeros: [
      { nombre: "Ana Torres", pasaporte: "UY1122334" }
    ],
    paquete: {
      descripcion: "Playa y descanso",
      precio_total: 1300,
      hotel: {
        nombre: "Resort Playa Sol",
        tipo_habitacion: "estándar",
        zona: "playa",
        estrellas: 4,
        precio: 180
      },
      vuelo: {
        origen: "Lima",
        destino: "Cancún",
        aerolinea: "LATAM",
        fecha_hora: ISODate("2025-07-20T10:30:00Z")
      }
    }
  },
  {
    numero_reserva: "R005",
    fecha_creacion: ISODate("2025-06-02T00:00:00Z"),
    estado: "confirmada",
    precio: 800,
    cliente: {
      nombre: "Mario Fernández",
      correo: "mario.fernandez@email.com"
    },
    pasajeros: [
      { nombre: "Mario Fernández", pasaporte: "PE7788990" }
    ],
    paquete: {
      descripcion: "Montaña y aventura",
      precio_total: 800,
      hotel: {
        nombre: "Hotel Cumbres",
        tipo_habitacion: "doble",
        zona: "montaña",
        estrellas: 3,
        precio: 100
      },
      vuelo: {
        origen: "Santiago",
        destino: "Bariloche",
        aerolinea: "Sky",
        fecha_hora: ISODate("2025-07-18T08:00:00Z")
      }
    }
  },
  {
    numero_reserva: "R006",
    fecha_creacion: ISODate("2025-06-02T00:00:00Z"),
    estado: "pendiente",
    precio: 600,
    cliente: {
      nombre: "Sofía Ramírez",
      correo: "sofia.ramirez@email.com"
    },
    pasajeros: [
      { nombre: "Sofía Ramírez", pasaporte: "BR6655443" }
    ],
    vuelo: {
      origen: "São Paulo",
      destino: "Bariloche",
      aerolinea: "GOL",
      fecha_hora: ISODate("2025-07-12T07:00:00Z")
    }
  },
  {
    numero_reserva: "R007",
    fecha_creacion: ISODate("2025-06-01T00:00:00Z"),
    estado: "confirmada",
    precio: 1000,
    cliente: {
      nombre: "Laura Pérez",
      correo: "laura.perez@email.com"
    },
    pasajeros: [
      { nombre: "Laura Pérez", pasaporte: "MX9988776" }
    ],
    paquete: {
      descripcion: "Vacaciones familiares en Cancún",
      precio_total: 1000,
      hotel: {
        nombre: "Hotel Sol Caribe",
        tipo_habitacion: "estándar",
        zona: "centro",
        estrellas: 4,
        precio: 160
      },
      vuelo: {
        origen: "Ciudad de México",
        destino: "Cancún",
        aerolinea: "Aeroméxico",
        fecha_hora: ISODate("2025-07-22T11:00:00Z")
      }
    }
  }
]);