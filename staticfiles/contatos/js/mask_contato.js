document.addEventListener('DOMContentLoaded', function () {
    (function($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jquery.mask.min.js não carregado corretamente.');
            return;
        }

        $('.contato-mask').each(function () {
            const input = $(this);
            if (input.attr('id') === 'id_celular') {
                input.mask('(00) 00000-0000');
            } else if (input.attr('id') === 'id_telContato') {
                input.mask('(00) 0000-0000');
            }
        });
    })(django.jQuery);
});
