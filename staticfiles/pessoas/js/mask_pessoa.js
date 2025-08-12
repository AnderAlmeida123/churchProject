document.addEventListener("DOMContentLoaded", function () {
    (function ($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jQuery.mask.min.js não carregado !')
            return
        }

        $('.cpf-mask').each(function () {
            const input = $(this);
            if (input.attr('id') === 'id_cpf') {
                input.mask('000.000.000-00')
            }
        });

        $('.data_nascimento-mask').each(function () {
            const input = $(this);
            if (input.attr('id') === 'id_data_nascimento') {
                input.mask('00/00/0000');
            }
        });
    })(django.jQuery);
});


