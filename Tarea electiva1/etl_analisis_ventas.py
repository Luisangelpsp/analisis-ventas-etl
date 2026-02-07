import os
import pandas as pd
from sqlalchemy import create_engine

#Creando la conexion con mysql

engine = create_engine(
    "mysql+mysqlconnector://root:152315@localhost/analisis_ventas"
)

base_dir = os.path.dirname(os.path.abspath(__file__))

fuentes = pd.read_csv("fuentes_datos.csv")
clientes = pd.read_csv("clientes.csv")
productos = pd.read_csv("productos.csv")
ventas = pd.read_csv("ventas.csv")

# LIMPIEZA DE DATOS
fuentes.drop_duplicates(inplace=True)
clientes.drop_duplicates(inplace=True)
productos.drop_duplicates(inplace=True)
ventas.drop_duplicates(inplace=True)

fuentes.dropna(inplace=True)
clientes.dropna(inplace=True)
productos.dropna(inplace=True)
ventas.dropna(inplace=True)

#Normalizacion de datos

clientes["nombre"] = clientes["nombre"].str.title()
productos["categoria"] = productos["categoria"].str.upper()

ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"])

productos["precio"] = productos["precio"].astype(float)

#Calculo del campo derivado

ventas = ventas.merge(
    productos[["id_producto", "precio"]],
    on="id_producto",
    how="left"
)

ventas["total"] = ventas["cantidad"] * ventas["precio"]

# CARGA DE DATOS EN MySQL

fuentes.to_sql(
    "fuentes_datos",
    engine,
    if_exists="append",
    index=False
)

clientes.to_sql(
    "clientes",
    engine,
    if_exists="append",
    index=False
)

productos.to_sql(
    "productos",
    engine,
    if_exists="append",
    index=False
)

ventas[[
    "id_venta",
    "id_cliente",
    "id_producto",
    "cantidad",
    "fecha_venta",
    "total"
]].to_sql(
    "ventas",
    engine,
    if_exists="append",
    index=False
)

