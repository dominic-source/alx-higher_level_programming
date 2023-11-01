$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
    const { hello } = data;
    $('DIV#hello').append(hello);
  });
});
