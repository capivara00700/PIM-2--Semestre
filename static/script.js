if(document.getElementById('container_principal')){ //Codigos para o menu de login
    const container = document.getElementById('container_principal');
    const registerBtn = document.getElementById('register');
    const loginBtn = document.getElementById('login');

    registerBtn.addEventListener('click', () => { // evento de click para animação de troca de tela
        container.classList.add("active");
    });

    loginBtn.addEventListener('click', () => { // evento de click para animação de troca de tela
        container.classList.remove("active");
    });

}

//botão hamburguer
const Btn = document.getElementById('hamburguer')
const Nav = document.getElementById('navbar')
const Bloco_Principal = document.getElementById('Bloco-Principal')
const Menu_lateral = document.getElementById('Menu-lateral')

Btn.addEventListener('click', () => {
    Nav.classList.toggle("active"); // Animação de botâo 

    if(Nav.classList.contains("active")){ // Adaptando o posicionamento dos itens
        Bloco_Principal.style.width = "80%"
        Menu_lateral.style.marginLeft = "0"
    } else {
        Bloco_Principal.style.width = "100%" // Voltando o posicionamento dos itens para o padrão
        Menu_lateral.style.marginLeft = "-20%"
    }
});