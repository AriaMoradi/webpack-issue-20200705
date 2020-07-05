const glob = require('glob')
const path = require('path')
const {CleanWebpackPlugin} = require('clean-webpack-plugin')
module.exports = {
    entry: glob.sync('./*/templates/**/*.js').reduce((acc, path) => {
        var entry = path.replace(/templates\/.*\//, '')
        console.log(entry)
        acc[entry] = path
        return acc
    }, {}),
    // course: './course/templates/course/index.js',
    output: {
        filename: '[name]',
        path: __dirname + '/webpack-static'
    },
    plugins: [
        new CleanWebpackPlugin({cleanStaleWebpackAssets: false}),
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', "@babel/react"]
                    }
                }
            }
        ]
    },
};