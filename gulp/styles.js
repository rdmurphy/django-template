'use strict'

const cleancss = require('gulp-clean-css')
const gulp = require('gulp')
const gulpIf = require('gulp-if')
const postcss = require('gulp-postcss')
const sass = require('gulp-sass')
const size = require('gulp-size')

const autoprefixer = require('autoprefixer')

const bs = require('./browsersync')

const IS_PRODUCTION = process.env.NODE_ENV === 'production'

module.exports = () => {
  return gulp.src('./{{ project_name }}/static_src/scss/*.scss')
    .pipe(sass({
      includePaths: ['node_modules'],
      precision: 10
    }).on('error', sass.logError))
    .pipe(gulpIf(IS_PRODUCTION, postcss([ autoprefixer({ browsers: ['last 2 versions'] }) ])))
    .pipe(gulpIf(IS_PRODUCTION, cleancss()))
    .pipe(gulp.dest('./{{ project_name }}/static/styles/'))
    .pipe(bs.stream({match: '**/*.css'}))
    .pipe(size({title: 'styles'}))
}
