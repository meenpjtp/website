$(document).on('submit', '#create-book-form', function(e){
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/create/',
        data: {
            title:$('#title').val(),
            author:$('#author').val(),
            country:$('#country').val(),
            language:$('#language').val(),
            link:$('#link').val(),
            pages:$('#pages').val(),
            year:$('#year').val(),
            image_link:$('#image_link').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
     success:function(){
        document.getElementById("create-book-form").reset();
        update();
        },

     error:function(){
         alert("This book entry already exists!");
         document.getElementById("create-book-form").reset();
         update();
       }
     });
});

function update() {
    $.ajax({
        type: "POST",
        url: '/update/',
        data: {
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        }
    })
    .done(function(response) {
        $('#list-body').html(response);
        filter();
    });
}