$(document).ready(function() {

    $('a').css('cursor', 'pointer');

    $('#portuguese').on('click', function() {
        if ($(location).attr('href').indexOf('intro_pt') < 0) {
            $(location).attr('href', $(location).attr('href').replace('intro', 'intro_pt'));
        }
    });

    $('#english').on('click', function() {
        if ($(location).attr('href').indexOf('intro_pt') > 0) {
            $(location).attr('href', $(location).attr('href').replace('_pt', ''));
        }
    });

});