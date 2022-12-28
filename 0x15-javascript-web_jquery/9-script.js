//Fetching the value of "hello" from URL and displaying it inside a DIV

$(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, textStatus) => {
    if (textStatus === 'success') {
      $('div#hello').text(data.hello);
    }
  });
});
