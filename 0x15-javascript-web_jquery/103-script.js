$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      translate();
    }
  });

  function translate () {
    const languageCode = $('INPUT#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;
    $.get(apiUrl, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
});
