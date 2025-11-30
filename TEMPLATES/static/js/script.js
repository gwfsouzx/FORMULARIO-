document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("formCadastro");

    form.addEventListener("submit", function(event) {

        const username = document.getElementById("username").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (!username || !email || !password) {
            alert("Todos os campos devem ser preenchidos.");
            event.preventDefault();
            return;
        }

        const emailValido = /\S+@\S+\.\S+/.test(email);
        if (!emailValido) {
            alert("O e-mail informado não é válido.");
            event.preventDefault();
            return;
        }
    });
});
