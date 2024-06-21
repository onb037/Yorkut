let botao = document.getElementById('botao-noturno');
let body = document.querySelector('body');
let icon = document.getElementById('icon-mode');

botao.addEventListener('click', ()=>{
    body.classList.toggle("light");

    if(body.classList.contains('light')){
        icon.innerHTML = 'dark_mode';
        icon.style.color = '#000';
    } else {
        icon.innerHTML = 'light_mode';
        icon.style.color = '#ffbb00';
    }
})