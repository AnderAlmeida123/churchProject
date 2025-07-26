document.addEventListener('DOMContentLoaded', function () {
    (function($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jquery.mask.min.js não carregado!');
            return;
        }

        $('#id_data_hora').mask('00/00/0000 00:00');
    })(django.jQuery);
});
