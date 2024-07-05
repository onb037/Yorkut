
let itensBloqueados = document.querySelectorAll('.side-item.bloqueado');


itensBloqueados.forEach(item => {
    item.addEventListener('click', (event) => {
        event.preventDefault(); 
        alert('Este item está em manutenção e não está disponível no momento.');
    });
});
