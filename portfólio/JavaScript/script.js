let produtos = [
    {nome: "Mouse", quantidade: 10},
    {nome: "Teclado", quantidade: 5},
    {nome: "Monitor", quantidade: 2}
];

document.getElementById("botao-cadastrar").addEventListener("click", function(){
    let nome = document.getElementById("nome-produto").value;
    let quantidade = document.getElementById("quantidade-produto").value;
    produtos.push({
        nome : nome,
        quantidade : quantidade
    });
    document.getElementById("total-produtos").textContent = produtos.length;
});

document.getElementById("buscar-produto").addEventListener("click", function(){
    let nomePesquisado = document.getElementById("pesquisa-produto").value;
    let produtoEncontrado = produtos.find(function(produto) {
        return produto.nome.toLowerCase() === nomePesquisado.toLowerCase();
    });
    

if (produtoEncontrado) {

    document.getElementById("resultado").textContent = `produto: ${produtoEncontrado.nome} | Estoque: ${produtoEncontrado.quantidade}`;
} else {

    document.getElementById("resultado").textContent = "Produto Nao Encontrado";
}
});
