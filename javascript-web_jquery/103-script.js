$(document).ready(function() {
  function fetchGreeting() {
    const langCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function(data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchGreeting);

  $('#language_code').keypress(function(event) {
    if (event.which === 13) { // Enter key is pressed
      fetchGreeting();
    }
  });
});
