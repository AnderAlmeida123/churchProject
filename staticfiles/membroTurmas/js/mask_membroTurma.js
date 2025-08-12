document.addEventListener('DOMContentLoaded', function () {
    (function ($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jQuery.mask.min.js não carregado!')
            return
        }

        $('.data-mask').each(function () {
            const input = $(this);
            if (input.attr('id') === 'id_data_entrada') {
                input.mask('00/00/0000');
            } else if (input.attr('id') === 'id_data_saida') {
                input.mask('00/00/0000');
            }
        });

    })(django.jQuery);
});