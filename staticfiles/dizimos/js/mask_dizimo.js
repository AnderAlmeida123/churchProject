// Aplica a máscara de valor monetário
document.addEventListener('DOMContentLoaded', function () {
    (function ($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jquery.mask.min.js não carregado!');
            return;
        }

        $('#id_valor').mask('#.##0,00', {reverse: true});
    })(django.jQuery);
});
