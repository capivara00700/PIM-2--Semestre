//botão hamburguer
const Btn = document.getElementById('hamburguer')
const Nav = document.getElementById('navbar')

Btn.addEventListener('click', () => {
    console.log("foi")
    Nav.classList.toggle("active");
});