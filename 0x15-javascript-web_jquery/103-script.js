#!/usr/bin/node
const $ = window.$;
const url =  'https://www.fourtonfish.com/hellosalut/?';
$('INPUT#language_code'.click(() => {
	$.get(url + $.param({ lang: $('INPUT#language_code').val() }), (data) => {
		$('DIV#hello').html(data.hello);
	});
});
