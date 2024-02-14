$(function(){
  // get do formulario
  $('.js-create').click(function(){
      $.ajax({
        url: 'js/criar',
        type:'get',
        dataType: 'json',
        beforeSend:function(){
          $('#modal-bolo').modal('show');
        },
        success:function(data){
          $('#modal-bolo .modal-content').html(data.html_form);
        }

      });
  });

  // essa função é chamada quando clicar em um termo submit do formulario da classe js-create-bolo
  $("#modal-bolo").on('submit', '.js-create-bolo', function(){
    var form = $(this);
    $.ajax({
      url: form.attr('action'), //busca o atributo de action do formulario
      data: form.serialize(),  // pegar todos os dados de um formulário HTML e transformá-los em uma única string.
      type: form.attr('method'),
      dataType: 'json',
      success: function(data){
        if(data.form_is_valid){
          alert('Bolo adcionado'); // por enquanto retorna este alert
        }
        else{
          $('#modal-bolo .modal-content').html(data.html_form)
        }
      }

    });
    // retorna falsa para indicar que a pagina nao precisa ser atualizada
    return false
  });
})