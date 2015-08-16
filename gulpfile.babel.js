/* global -$ */
'use strict';

import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';

import autoprefixer from 'autoprefixer-core';
import browserSync from 'browser-sync';
import del from 'del';
import buffer from 'vinyl-buffer';
import runSequence from 'run-sequence';
import source from 'vinyl-source-stream';
import yargs from 'yargs';

import browserify from 'browserify';
import babelify from 'babelify';
import watchify from 'watchify';

const $ = gulpLoadPlugins();
const args = yargs.argv;
const bs = browserSync.create();
const reload = bs.reload;
const stream = bs.stream;

function browserifyScripts(shouldWatch) {
  let bundler = browserify('./{{ project_name }}/static_src/scripts/main.js', {
    debug: true,
  });

  bundler.transform(babelify);

  function bundle() {
    return bundler.bundle()
      .pipe(source('bundle.js'))
      .pipe(buffer())
      .pipe($.sourcemaps.init({loadMaps: true}))
      .pipe($.if(args.production, $.uglify()))
      .pipe($.sourcemaps.write(args.production ? '.' : undefined))
      .pipe(gulp.dest('./{{ project_name }}/static/scripts/'))
      .pipe(reload({stream: true}))
      .pipe($.size({title: 'scripts'}));
  }

  if (shouldWatch) {
    bundler = watchify(bundler);
    bundler.on('update', bundle);
    bundler.on('log', $.util.log);
  }

  return bundle();
}

gulp.task('scripts', () => {
  return browserifyScripts();
});

gulp.task('watchify', () => {
  return browserifyScripts(true);
});

gulp.task('styles', () => {
  return gulp.src('./{{ project_name }}/static_src/scss/*.scss')
    .pipe($.sourcemaps.init())
    .pipe($.sass({
      includePaths: ['node_modules'],
      precision: 10
    }).on('error', $.sass.logError))
    .pipe($.postcss([
      autoprefixer({
        browsers: ['last 2 versions']
      })
    ]))
    .pipe($.if(args.production, $.minifyCss({
      keepSpecialComments: 0
    })))
    .pipe($.sourcemaps.write(args.production ? '.' : undefined))
    .pipe(gulp.dest('./{{ project_name }}/static/styles/'))
    .pipe(stream({
      match: '**/*.css'
    }))
    .pipe($.size({title: 'styles'}));
});

gulp.task('serve', ['styles', 'watchify'], () => {
  bs.init({
    logPrefix: '{{ project_name }}'.toUpperCase(),
    notify: false,
    open: false,
    proxy: 'localhost:8000'
  });

  gulp.watch(['./{{ project_name }}/static_src/scss/**/*.scss'], ['styles']);
  gulp.watch(['./{{ project_name }}/templates/**/*.html']).on('change', reload);
});

gulp.task('clean', (cb) => {
  return del(['./{{ project_name }}/static/styles/**/*'], cb);
});

gulp.task('build', ['default']);

gulp.task('default', ['clean'], cb => {
  runSequence(['styles', 'scripts'], cb);
});
