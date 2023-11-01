$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, statusCode) {
  const dataPool = data.results;
  for (const pool of dataPool) {
    $('UL#list_movies').append(`<li>${pool.title}</li>`);
  }
});
