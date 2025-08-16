document.addEventListener("DOMContentLoaded", carregar_transacoes)

document.getElementById("efetuar-transacao").addEventListener("click", async function(e){
    valor = prompt("Valor da transação:")
    
    const resposta = await fetch("/transacao", {
        method: "POST",
        headers: {"Content-type": "application/json"},
        body: JSON.stringify(valor)
    })
    
    const dados = await resposta.json()
    carregar_transacoes()
    
    alert(`Status: ${resposta.status} - ${dados.mensagem}`)
})

document.getElementById("limpar-transacoes").addEventListener("click", async function(e){
    const resposta = await fetch("/transacao", {
        method: "DELETE"
    })
    
    const dados = await resposta.json()
    alert(`Status: ${resposta.status} - ${dados.mensagem}`)
    carregar_transacoes()
})

async function carregar_transacoes() {
    const resposta = await fetch("/transacao")
    const dados = await resposta.json()

    const transacoes = document.getElementById("transacoes")
    transacoes.innerHTML = ""
    
    let conteudo = ""
    dados.dados.forEach(dado => {
       conteudo += `${dado.dataHora}: R$${dado.valor}<br>`

    });
    transacoes.innerHTML = conteudo
}
