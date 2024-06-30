document.querySelectorAll('.btn-serAmigo').forEach(button => {
    button.addEventListener('click', function (e) {
        e.preventDefault();

        if (this.classList.contains('seguindo')) {
            this.classList.remove('seguindo');
            this.innerHTML = `<span class="material-symbols-outlined">person_add</span>`;
        } else {
            this.classList.add('seguindo');
            this.innerHTML = `<span class="material-symbols-outlined">person_check</span>`;
        }
    });
});
