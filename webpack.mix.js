let mix = require('laravel-mix');

mix.js('front/src/js/app.js', 'static')
    .sass('front/src/scss/app.scss', 'static');