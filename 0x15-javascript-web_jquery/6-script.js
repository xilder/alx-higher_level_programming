#!/usr/bin/node
const $ = window.$;
$('DIV#update_header').click(() => {
	$('header').text('New Header!!!')
})
