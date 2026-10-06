import sqlite3

conexao = sqlite3.connect("mesafartai.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('DOADOR','ONG')) NOT NULL,
    cep TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    telefone TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS doacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doador_id INTEGER,
    descricao_alimento TEXT NOT NULL,
    quantidade_kg REAL,
    data_validade TEXT,
    status TEXT DEFAULT 'DISPONIVEL',
    FOREIGN KEY (doador_id) REFERENCES usuarios(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doacao_id INTEGER,
    ong_id INTEGER,
    distancia_km REAL,
    data_match TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (doacao_id) REFERENCES doacoes(id),
    FOREIGN KEY (ong_id) REFERENCES usuarios(id)
)
""")

dados = [
    ("ONG Prato Quente", "ONG", "06700-000", -23.612, -46.781, "11999990001"),
    ("Abrigo Esperanca", "ONG", "06705-000", -23.625, -46.795, "11999990002"),
    ("Supermercado Silva", "DOADOR", "06701-000", -23.615, -46.785, "11999990003"),
    ("Restaurante Sabor", "DOADOR", "06703-000", -23.618, -46.789, "11999990004")
]

cursor.executemany("""
INSERT INTO usuarios
(nome, tipo, cep, latitude, longitude, telefone)
VALUES (?, ?, ?, ?, ?, ?)
""", dados)

conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")
