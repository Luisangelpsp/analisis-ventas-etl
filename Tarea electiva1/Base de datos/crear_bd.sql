CREATE DATABASE analisis_ventas;
USE analisis_ventas;

CREATE TABLE fuentes_datos (
    id_fuente INT AUTO_INCREMENT PRIMARY KEY,
    nombre_fuente VARCHAR(100),
    tipo_fuente VARCHAR(50)
);

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    pais VARCHAR(50),
    id_fuente INT,
    FOREIGN KEY (id_fuente) REFERENCES fuentes_datos(id_fuente)
);

CREATE TABLE productos (
    id_producto INT PRIMARY KEY,
    nombre_producto VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10,2),
    id_fuente INT,
    FOREIGN KEY (id_fuente) REFERENCES fuentes_datos(id_fuente)
);

CREATE TABLE ventas (
    id_venta INT PRIMARY KEY,
    id_cliente INT,
    id_producto INT,
    cantidad INT,
    fecha_venta DATE,
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE facturas (
    id_factura INT PRIMARY KEY,
    id_venta INT,
    fecha_factura DATE,
    monto_total DECIMAL(10,2),
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta)
    
);

