const div_trocar_fotos = document.getElementById('trocar_foto');
const span = document.getElementById('span_troca_foto');
const body = document.body
const header = document.querySelector('header')
const main = document.querySelector('main')
const footer = document.querySelector('footer')
const fechar_span = document.getElementById('fechar_span');


div_trocar_fotos.addEventListener('click', () => {
    // Alterna entre mostrar e esconder o span
    if (span.style.display === 'none') {
        span.style.display = 'block';
        header.classList.add('body_span');
        main.classList.add('body_span');
        footer.classList.add('body_span');
        span.style.pointerEvents ='auto'
    } else {
        span.style.display = 'none'

    }
}); 

fechar_span.addEventListener('click', () => {
    header.classList.remove('body_span');
    main.classList.remove('body_span');
    footer.classList.remove('body_span');
    span.style.display = 'none';

});

function enviar_form(id){
    document.getElementById(id).form.submit()
}


function exibir_nav(id){
    
    document.getElementById('posts_usuario').style.display='none';
    document.getElementById('sobre_usuario').style.display='none';
    document.getElementById('comentarios_usuario').style.display='none';
    document.getElementById('compartilhamentos_usuario').style.display='none';
    document.getElementById(id).style.display='block';

}

function adjustTextarea(textarea) {
    // Redefine a altura para recalcular
    textarea.style.height = 'auto';
    // Ajusta a altura com base no conteúdo
    textarea.style.height = `${textarea.scrollHeight}px`;
  }