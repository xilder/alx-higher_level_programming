#!/usr/bin/node
const $ = window.$;
$('DIV#toggle_header').click(() => {
	$('header').toggleClass('red green')
});
