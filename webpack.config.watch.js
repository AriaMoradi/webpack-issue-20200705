const glob = require('glob')
const path = require('path')
const {CleanWebpackPlugin} = require('clean-webpack-plugin')
module.exports = {
    entry: glob.sync('./*/templates/**/*.js').reduce((acc, path) => {
        var entry = path.replace(/templates\/.*\//, '')
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
    resolve: {
        alias: glob.sync('./*/react_components').reduce((acc, p) => {
            var djangoapp = p.replace("/react_components", '').replace("./", '');
            acc[djangoapp] = path.resolve(__dirname, p);
            console.log(acc)
            return acc
        }, {}),
    }
};