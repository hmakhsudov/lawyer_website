
$(".btn_modal").fancybox({
    'padding': 0
});

// Scroll
$(".btn_scroll").click(function (e) {
    e.preventDefault();

    var str = $(this).attr('href');
    $([document.documentElement, document.body]).animate({
        scrollTop: $(str).offset().top
    }, 500);
});


var comments = new Swiper('.comments__slider', {
    slidesPerView: 1,
    spaceBetween: 0,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.comments__nav_next',
        prevEl: '.comments__nav_prev',
    },
    breakpoints: {
        992: {
            slidesPerView: 2
        },
        1200: {
            slidesPerView: 2
        }
    }
});

var comments = new Swiper('.comments__slider-2', {
    slidesPerView: 1,
    spaceBetween: 0,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.comments__nav_next',
        prevEl: '.comments__nav_prev',
    },
    breakpoints: {
        992: {
            slidesPerView: 1
        },
        1200: {
            slidesPerView: 1
        }
    }
});

(function () {

    $('.questions__item_title').on('click touchstart', function (e) {
        e.preventDefault();
        var question = $(this).closest('.questions__item');
        var is_open = question.hasClass('open');

        if (is_open) {
            question.removeClass('open');
            question.find('.questions__item_text').slideUp('fast');
        }
        else {
            $('.questions__list').find('.questions__item').removeClass('open');
            $('.questions__list').find('.questions__item_text').slideUp('fast');

            question.addClass('open');
            question.find('.questions__item_text').slideDown('fast');
        }
    });

}());


/* 
    - - - - - - -
    CUSTOM BLOCK
    - - - - - - -
*/

//Phone mask
$(".form input[name='phone']").mask("+7 (999) 999-99-99");


//Yandex Metrika Webvisor


