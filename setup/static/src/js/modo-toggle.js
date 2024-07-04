let botao = document.getElementById('botao-noturno');
let body = document.querySelector('body');
let icon = document.getElementById('icon-mode');


if (localStorage.getItem('modoNoturno') === 'true') {
    body.classList.add('light');
    icon.innerHTML = 'dark_mode';
    icon.style.color = '#000';
} else {
    body.classList.remove('light');
    icon.innerHTML = 'light_mode';
    icon.style.color = '#ffbb00';
}

botao.addEventListener('click', () => {
    body.classList.toggle("light");

    if (body.classList.contains('light')) {
        icon.innerHTML = 'dark_mode';
        icon.style.color = '#000';
        localStorage.setItem('modoNoturno', 'true');
    } else {
        icon.innerHTML = 'light_mode';
        icon.style.color = '#ffbb00';
        localStorage.setItem('modoNoturno', 'false');
    }
});
