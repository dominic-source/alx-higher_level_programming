$(function () {
  $('INPUT#btn_translate').on('click', function () {
    const val = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${val}`, function (data, status) {
      const { hello } = data;
      $('DIV#hello').html(hello);
    });
  });
});
