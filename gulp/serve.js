'use strict'

const gulp = require('gulp')
const stripAnsi = require('strip-ansi')
const webpack = require('webpack')
const webpackDevMiddleware = require('webpack-dev-middleware')

const bs = require('./browsersync')
const webpackConfig = require('../webpack.config')
const bundler = webpack(webpackConfig)

bundler.plugin('done', function (stats) {
  if (stats.hasErrors() || stats.hasWarnings()) {
    return bs.sockets.emit('fullscreen:message', {
      title: 'Webpack Error:',
      body: stripAnsi(stats.toString()),
      timeout: 100000
    })
  }

  bs.reload()
})

module.exports = () => {
  bs.init({
    logPrefix: 'DJANGO',
    middleware: [
      webpackDevMiddleware(bundler, {
        publicPath: webpackConfig.output.publicPath,
        stats: {colors: true}
      })
    ],
    notify: false,
    open: false,
    plugins: ['bs-fullscreen-message'],
    port: 3000,
    proxy: 'localhost:8000'
  })

  gulp.watch(['./{{ project_name }}/static_src/scss/**/*.scss'], ['styles'])
  gulp.watch(['./{{ project_name }}/templates/**/*.html']).on('change', bs.reload)
}
