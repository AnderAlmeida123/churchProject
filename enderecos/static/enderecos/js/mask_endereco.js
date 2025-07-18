document.addEventListener("DOMContentLoaded", function () {
    (function ($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jQuery.mask.min.js não carregado!');
            return;
        }

        $('#id_cep').mask('00000-000');
    })(django.jQuery);
});