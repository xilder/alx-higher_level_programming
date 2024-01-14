#!/usr/bin/node
const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'

$.get(url, (data) => {
	const hello = data.hello
	$('DIV#hello').text(hello)
});

