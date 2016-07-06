'use strict'

const gulp = require('gulp')

/*
Main tasks
 */
gulp.task('images', require('./gulp/images'))
gulp.task('extras', require('./gulp/extras'))
gulp.task('scripts', require('./gulp/scripts'))
gulp.task('styles', require('./gulp/styles'))

/*
Utility tasks
 */
gulp.task('serve', ['extras', 'styles'], require('./gulp/serve'))

/*
Build tasks
 */
gulp.task('build', ['images', 'extras', 'scripts', 'styles'])

gulp.task('default', ['build'])
