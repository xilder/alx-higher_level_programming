#!/usr/bin/node
const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
$.get(url, (data) => {
	const name = data.name
	$('DIV#character').text(name);
});

