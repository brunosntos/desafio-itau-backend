document.getElementById("efetuar-transacao").addEventListener("click", async function(e){
    valor = prompt("Valor da transação:")

    const resposta = await fetch("/transacao", {
        method: "POST",
        headers: {"Content-type": "application/json"},
        body: JSON.stringify(valor)
    })

    const dados = await resposta.json()

    alert(`Status: ${resposta.status} - ${dados.mensagem}`)
})