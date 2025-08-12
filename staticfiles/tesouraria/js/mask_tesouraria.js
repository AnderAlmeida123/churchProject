document.addEventListener('DOMContentLoaded', () => {
    (function ($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jQuery.mask.min.js não carregado!');
            return;
        }

        $('.valor-mask').each(function () {
            const input = $(this);
            if (input.attr('id') === 'id_valor') {
                input.mask('000.000.000,00', {reverse: true});
            }
        })

        $('.data_movimentacao-mask').each(function () {
            const input = $(this);
            if (input.attr('id') === 'id_data_movimentacao') {
                input.mask('00/00/00')
            }
        })
    })(django.jQuery);
})