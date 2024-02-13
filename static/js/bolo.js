$(function(){
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

        })
    })
})