$('DIV#add_item').on('click', function () {
  const item = '<li>Item</li>';
  $('UL.my_list').append(item);
});
