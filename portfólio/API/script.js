let botaoBuscar = document.getElementById("buscarUsuario");
botaoBuscar.addEventListener("click", function() {
    let id = document.getElementById("idUsuario").Value;
    let url = `https://jsonplaceholder.typicode.com/users/${id}`;

    fetch(url)
        .then(response => response.json())
        .then(dados => {
            console.log(dados);
            document.getElementById("nome").textContent = dados.name;
            document.getElementById("email").textContent = dados.email;
            document.getElementById("cidade").textContent = dados.addres.city;  
        });

});

