'use strict'

const u = require('gulp-util')
const webpack = require('webpack')

const webpackConfig = process.env.NODE_ENV === 'production' ? require('../webpack.config.prod') : require('../webpack.config')
const bundle = webpack(webpackConfig)

module.exports = (done) => {
  bundle.run((err, stats) => {
    if (err) throw new u.PluginError('webpack', err)
    u.log('[webpack]', stats.toString({colors: true}))

    done()
  })
}
