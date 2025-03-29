document.getElementById("form-senha").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita o reload da página

    let origem = document.getElementById("origem").value;
    let tamanho = parseInt(document.getElementById("tamanho").value);

    fetch('/gerar_senha', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ origem: origem, tamanho: tamanho })
    })
    .then(response => response.json())
    .then(data => {
        alert(`Senha gerada!\nOrigem: ${data.origem}\nSenha: ${data.senha}`);
        carregarSenhas();
    })
    .catch(error => console.error("Erro ao gerar senha:", error));
});

function carregarSenhas() {
    fetch('/listar_senhas')
    .then(response => response.json())
    .then(data => {
        let tabela = document.getElementById("tabela-senhas");
        tabela.innerHTML = ""; // Limpa antes de atualizar

        data.forEach(senha => {
            let row = `<tr><td>${senha.id}</td><td>${senha.origem}</td><td>${senha.senha}</td></tr>`;
            tabela.innerHTML += row;
        });
    })
    .catch(error => console.error("Erro ao carregar senhas:", error));
}
