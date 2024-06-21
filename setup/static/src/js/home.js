const btnsLike = document.querySelectorAll('.btn-like');

btnsLike.forEach(botao => {
    botao.addEventListener('click', function(e){
       let botaoClicado = e.target;

        botaoClicado.innerHTML = `<span class="material-symbols-outlined">
mood
</span>`;
        botaoClicado.style.color = "yellow";


    })
})


let modal = document.getElementById('modal-comentarios');
let btnsComentario = document.querySelectorAll('.btn-coment');

btnsComentario.forEach(botao =>{
    botao.addEventListener('click', function(e){
        let botaoClicado = e.target;

        modal.classList.toggle('ativo');
    })
})

modal.addEventListener('click', ()=>{

})