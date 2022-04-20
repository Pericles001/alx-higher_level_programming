$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data)=>{
    $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
