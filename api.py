from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import datetime
import pytz

app = Flask(__name__, static_folder='.', static_url_path='')

def db_connection():
    conn = sqlite3.connect('estacionamento.db')
    return conn

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/scripts.js')
def scripts():
    return send_from_directory('.', 'scripts.js')

@app.route('/entrar', methods=['POST'])
def entrar():
    placa = request.json['placa']
    conn = db_connection()
    cursor = conn.cursor()
    fuso_horario = pytz.timezone('America/Sao_Paulo')
    agora = datetime.datetime.now(fuso_horario).strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO veiculos (placa, hora_entrada) VALUES (?, ?)", (placa, agora))
    conn.commit()
    conn.close()
    return jsonify({"message": "Veículo Registrado com Sucesso!."}), 201

@app.route('/sair', methods=['POST'])
def sair():
    placa = request.json['placa']
    conn = db_connection()
    cursor = conn.cursor()

    fuso_horario = pytz.timezone('America/Sao_Paulo')
    agora = datetime.datetime.now(fuso_horario).strftime("%Y-%m-%d %H:%M:%S.%f")
    cursor.execute("UPDATE veiculos SET hora_saida = ? WHERE placa = ? AND hora_saida IS NULL", (agora, placa))
    conn.commit()

    cursor.execute("SELECT hora_entrada, hora_saida FROM veiculos WHERE placa = ? ORDER BY id DESC LIMIT 1", (placa,))
    result = cursor.fetchone()
    conn.close()

    if result:
        hora_entrada_str, hora_saida_str = result
        print(f"DEBUG: hora_entrada_str={hora_entrada_str}, hora_saida_str{hora_saida_str}")
        hora_entrada = datetime.datetime.strptime(hora_entrada_str, "%Y-%m-%d %H:%M:%S")
        hora_entrada = fuso_horario.localize(hora_entrada)
        hora_saida = datetime.datetime.strptime(hora_saida_str, "%Y-%m-%d %H:%M:%S.%f")
        hora_saida = fuso_horario.localize(hora_saida)

        if hora_saida < hora_entrada:
            print("DEBUG: Corrigindo hora_saida para hora atual.")
            hora_saida = datetime.datetime.now(fuso_horario)

        tempo_total = hora_saida - hora_entrada
        horas = tempo_total.total_seconds() / 3600
        preco = round(horas * 10, 2)
        return jsonify({"message": f"Veículo saiu. Tempo: {horas:.2f} horas. Valor: R$ {preco:.2f}"}), 200
    else:
        return jsonify({"message": "Veículo não encontrado."}), 404

@app.route('/vagas', methods=['GET'])
def vagas():
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM veiculos WHERE hora_saida IS NULL")
        vagas_ocupadas = cursor.fetchone()[0]
        vagas_totais = 5
        vagas_disponiveis = vagas_totais - vagas_ocupadas
        conn.close()
        return jsonify({"vagas_disponiveis": vagas_disponiveis})
    except Exception as e:
        print("Erro na rota /vagas:", e)
        return jsonify({"error": "Internal Server Error"}), 500
    
@app.route('/listar', methods=['GET'])
def listar():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT placa, hora_entrada FROM veiculos WHERE hora_saida IS NULL")
    veiculos = cursor.fetchall()
    conn.close()

    veiculos_lista = [{"placa": v[0], "hora_entrada": v[1]} for v in veiculos]
    return jsonify(veiculos_lista)

if __name__ == '__main__':
    app.run(debug=True)