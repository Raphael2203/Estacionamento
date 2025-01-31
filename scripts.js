async function entrarVeiculo() {
    const placa = document.getElementById('placa').value;
    const response = await fetch('/entrar', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({placa: placa})
    });
    const data = await response.json();
    alert(data.message);
}

async function sairVeiculo() {
    const placa = document.getElementById('placa').value;
    const response = await fetch ('/sair', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({placa: placa})
    });
    const data = await response.json();
    alert(data.message);
}

async function mostrarVagas() {
    const response = await fetch('/vagas');
    const data = await response.json();
    document.getElementById('vagas').innerText = `Vagas disponiveis: ${data.vagas_disponiveis}`;
}

async function listarVeiculos() {
    const response = await fetch('/listar');
    const veiculos = await response.json();

    const listarVeiculos = document.getElementById('lista-veiculos');
    listarVeiculos.innerHTML = '';

    veiculos.forEach(veiculo => {
        const item = document.createElement('li');
        item.textContent = `Placa: ${veiculo.placa}, Hora de Entrada: ${veiculo.hora_entrada}`;
        listarVeiculos.appendChild(item);
    });
}