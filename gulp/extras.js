'use strict'

const gulp = require('gulp')
const size = require('gulp-size')

module.exports = () => {
  return gulp.src(['./{{ project_name }}/static_src/favicon.ico', './{{ project_name }}/static_src/robots.txt'])
    .pipe(gulp.dest('./{{ project_name }}/static'))
    .pipe(size({title: 'extras'}))
}
