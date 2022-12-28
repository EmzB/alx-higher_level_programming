// get character name from URL and display it on a DIV 
// Uses the jQuery API

$.getJSON('https://swapi.co/api/people/5/?format=json', function (data) {
    $('DIV#character').html(data['name']);
});
