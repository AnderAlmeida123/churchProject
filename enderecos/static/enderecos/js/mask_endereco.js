document.addEventListener("DOMContentLoaded", function () {
    (function ($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jQuery.mask.min.js não carregado!');
            return;
        }

        $('.contato-mask').each(function () {
            const input = $(this);
            if (input.attr('id') === 'id_cep') {
                input.mask('00000-000')
            }
        })

    })(django.jQuery);
});