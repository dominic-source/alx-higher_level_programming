$(function () {
  const elem = '<li>Item</li>';
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append(elem);
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list li').remove();
  });
});
