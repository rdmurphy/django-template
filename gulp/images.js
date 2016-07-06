'use strict'

const gulp = require('gulp')
const imagemin = require('gulp-imagemin')
const size = require('gulp-size')

module.exports = () => {
  return gulp.src('./{{ project_name }}/static_src/images/**/*')
    .pipe(imagemin())
    .pipe(gulp.dest('./{{ project_name }}/static/images/'))
    .pipe(size({title: 'images'}))
}
