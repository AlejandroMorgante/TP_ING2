// init/mongo/init.js

// Colección: propiedades
const propiedades = [
  { nombre: "Hostel Centro", precio: 80, zona: "centro", fecha_agregado: new Date() },
  { nombre: "Cabaña Norte", precio: 120, zona: "rural", fecha_agregado: new Date(new Date().setDate(new Date().getDate() - 40)) },
  { nombre: "Suite Vista Mar", precio: 200, zona: "tropical", fecha_agregado: new Date() },
  { nombre: "Depto Económico", precio: 65, zona: "centro", fecha_agregado: new Date() },
];

// Colección: reservas
const reservas = [
  {
    fecha_creacion: "2024-06-01",
    vuelo: { destino: "Brasil" },
    hotel: { tipo_habitacion: "doble", zona: "tropical" }
  },
  {
    fecha_creacion: "2024-06-01",
    vuelo: { destino: "Brasil" },
    hotel: { tipo_habitacion: "suite", zona: "centro" }
  },
  {
    fecha_creacion: "2024-06-02",
    vuelo: { destino: "Chile" },
    hotel: { tipo_habitacion: "estándar", zona: "sur" }
  },
  {
    fecha_creacion: "2024-06-03",
    vuelo: { destino: "Argentina" },
    paquete: { hotel: { tipo_habitacion: "doble" } },
    hotel: { tipo_habitacion: null, zona: "centro" }
  }
];

db.createCollection("propiedades");
db.createCollection("reservas");

db.propiedades.insertMany(propiedades);
db.reservas.insertMany(reservas);