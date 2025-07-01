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