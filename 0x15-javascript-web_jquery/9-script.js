$(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    sucess: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
