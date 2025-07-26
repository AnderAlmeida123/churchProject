document.addEventListener('DOMContentLoaded', function () {
    (function ($) {
        if (typeof $.fn.mask === 'undefined') {
            console.error('jQuery.mask.min.js não carregado!')
            return
        }

        $('.data-mask').mask('00/00/0000');
    })(django.jQuery);
});