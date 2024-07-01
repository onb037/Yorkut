document.querySelector('.btn-config').addEventListener('click', function (e) {
    e.preventDefault();
    const modal = document.querySelector('.modal-config');
    const btn = document.querySelector('.fechar-modal');
    modal.classList.add('ativo');

    btn.addEventListener('click',()=>{
        modal.classList.remove('ativo');
    })
});

document.getElementById('editar-foto').addEventListener('change', function (event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            const imgElement = document.getElementById('imagem-preview');
            imgElement.src = e.target.result;
            imgElement.style.display = 'block';
        };

        reader.readAsDataURL(file);
    }
});