#!/usr/bin/node
const $ = window.$;
$('DIV#red_header').click(() => {
	$('header').addClass('red');
});
