import gulp from 'gulp'
import u from 'gulp-util'
import gulpLoadPlugins from 'gulp-load-plugins'

import browserSync from 'browser-sync'
import stripAnsi from 'strip-ansi'
import webpack from 'webpack'
import webpackDevMiddleware from 'webpack-dev-middleware'
import yargs from 'yargs'

const projectFolder = '{{ project_name }}'

const $ = gulpLoadPlugins()
const args = yargs.argv
const bs = browserSync.create()

import webpackConfig from './webpack.config'
if (args.production) {
  webpackConfig.debug = false
  webpackConfig.devtool = 'source-map'
  webpackConfig.plugins.push(
    new webpack.optimize.UglifyJsPlugin()
  )
}
const webpackBundle = webpack(webpackConfig)

webpackBundle.plugin('done', (stats) => {
  if (stats.hasErrors() || stats.hasWarnings()) {
    return bs.sockets.emit('fullscreen:message', {
      title: 'Webpack Error:',
      body: stripAnsi(stats.toString()),
      timeout: 100000
    })
  }

  bs.reload()
})

gulp.task('scripts', (cb) => {
  webpackBundle.run((err, stats) => {
    if (err) throw new u.PluginError('webpack', err)
    u.log('[webpack]', stats.toString({colors: true}))

    cb()
  })
})

gulp.task('styles', () => {
  return gulp.src(`./${projectFolder}/static_src/scss/*.scss`)
    .pipe($.newer(`./${projectFolder}/static/styles`))
    .pipe($.sourcemaps.init())
    .pipe($.sass({
      includePaths: ['node_modules'],
      precision: 10
    }).on('error', $.sass.logError))
    .pipe($.if(args.production, $.cssnano({
      autoprefixer: {
        browsers: ['last 2 versions']
      },
      discardComments: {
        removeAll: true
      }
    })))
    .pipe($.sourcemaps.write(args.production ? '.' : undefined))
    .pipe(gulp.dest(`./${projectFolder}/static/styles/`))
    .pipe(bs.stream({match: '**/*.css'}))
    .pipe($.size({title: 'styles'}))
})

gulp.task('images', () => {
  return gulp.src(`./${projectFolder}/static_src/images/**/*`)
    .pipe($.cache($.imagemin({
      progressive: true,
      interlaced: true
    })))
    .pipe(gulp.dest(`./${projectFolder}/static/images/`))
    .pipe($.size({title: 'images'}))
})

gulp.task('extras', () => {
  return gulp.src([`./${projectFolder}/static_src/favicon.ico`, `./${projectFolder}/static_src/robots.txt`])
    .pipe(gulp.dest(`./${projectFolder}/static`))
    .pipe($.size({title: 'extras'}))
})

gulp.task('serve', ['images', 'extras', 'styles'], () => {
  bs.init({
    logConnections: true,
    logPrefix: projectFolder.toUpperCase(),
    middleware: [
      webpackDevMiddleware(webpackBundle, {
        publicPath: webpackConfig.output.publicPath,
        stats: {colors: true}
      })
    ],
    notify: false,
    open: false,
    plugins: ['bs-fullscreen-message'],
    proxy: 'localhost:8000'
  })

  gulp.watch([`./${projectFolder}/static_src/scss/**/*.scss`], ['styles'])
  gulp.watch([`./${projectFolder}/templates/**/*.html`]).on('change', bs.reload)
})

gulp.task('default', ['images', 'extras', 'scripts', 'styles'])

gulp.task('build', ['default'])
