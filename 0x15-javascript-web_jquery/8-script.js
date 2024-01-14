#!/usr/bin/node
const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json'
$.get(url, (data) => {
	const results = data.results;
	$.get(results, (id, value) => {
		$('UL#list_movies').append('<li>' + value.title + '</li>');
	});
});
