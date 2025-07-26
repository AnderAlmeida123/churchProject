// Aplica a máscara de data e hora no campo "data_hora"
document.addEventListener('DOMContentLoaded', function () {
    (function($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jquery.mask.min.js não carregado!');
            return;
        }

        // Máscara: 00/00/0000 00:00 (formato brasileiro)
        $('#id_data_hora').mask('00/00/0000 00:00');
    })(django.jQuery);
});
