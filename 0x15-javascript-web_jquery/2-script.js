#!/usr/bin/node
const $ = window.$;
$('DIV#red_header').click(() => {
  $('header').css('color', '#FF0000');
});
