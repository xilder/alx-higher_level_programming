#!/usr/bin/node
const $ = window.$
$('DIV#add_item') .click(() => {
	$('UL.my_list').append('<li>Item</li>');
});
$('DIV#remove_item') .click(() => {
        $('UL.my_list').remove();
});
$('DIV#remove_list') .click(() => {
        $('UL.my_list').remove();
});
