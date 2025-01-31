import sqlite3

def database():
    conn = sqlite3.connect('estacionamento.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS veiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        placa TEXT NOT NULL,
        hora_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        hora_saida TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    database()