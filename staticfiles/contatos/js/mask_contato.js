document.addEventListener('DOMContentLoaded', function () {
    (function($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jquery.mask.min.js não foi carregado corretamente.');
            return;
        }

        $('#id_celular').mask('(00) 00000-0000');
        $('#id_telContato').mask('(00) 0000-0000');
    })(django.jQuery);
});
