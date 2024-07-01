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

const modalMessage = document.querySelector('.modal-message');

modalMessage.querySelector('.fechar-modal').addEventListener('click', ()=>{
  modalMessage.style.display = 'none';
})
