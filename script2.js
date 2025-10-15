//botão hamburguer
const Btn = document.getElementById('hamburguer')
const Nav = document.getElementById('navbar')
const Bloco_Principal = document.getElementById('Bloco-Principal')
const Menu_lateral = document.getElementById('Menu-lateral')

Btn.addEventListener('click', () => {
    Nav.classList.toggle("active");

    if(Nav.classList.contains("active")){
        Bloco_Principal.style.width = "80%"
        Menu_lateral.style.marginLeft = "0"
    } else {
        Bloco_Principal.style.width = "100%"
        Menu_lateral.style.marginLeft = "-20%"
    }
});