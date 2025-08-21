console.log('JavaScript file loaded successfully');

document.addEventListener('DOMContentLoaded', function () {
    const menu = document.querySelector('.nav__menu');
    const toggle = document.querySelector('.header__toggle');
    const close = document.querySelector('#nav__close');

    if (toggle && menu) {
        toggle.addEventListener('click', function () {
            menu.classList.add('active');
        });
    }

    if (close && menu) {
        close.addEventListener('click', function () {
            menu.classList.remove('active');
        });
    }
});