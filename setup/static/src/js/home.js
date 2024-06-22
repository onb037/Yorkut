const botoesLike = document.querySelectorAll('.btn-like'); 

botoesLike.forEach(botao => { 
  botao.addEventListener('click', function(event) {
    const iconeLike = this.querySelector('.icon-like'); 
    
    if (iconeLike.textContent === 'sentiment_neutral') { 
      // Curtida
      iconeLike.textContent = 'mood';
      iconeLike.style.color = 'yellow';
      this.title = "Descurtir"; 
    } else {
      // Descurtida
      iconeLike.textContent = 'sentiment_neutral';
      this.title = "Curtir"; 
      iconeLike.style.color = '#004aad';
    }
  });
});


const modal = document.getElementById('modal-comentarios');
const btnsComentario = document.querySelectorAll('.btn-coment');

btnsComentario.forEach(botaob =>{
    botaob.addEventListener('click', function(e){
        let botaoClicado = e.target;
        modal.classList.toggle('ativo');

        const fecharBtn = document.querySelector('.fechar-modal-comentario');

        fecharBtn.addEventListener('click', ()=>{
            modal.classList.remove('ativo');
        })
    })
})