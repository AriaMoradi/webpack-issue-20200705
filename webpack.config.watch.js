const glob = require('glob');
const path = require('path');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');

const commonModules = "vendor.js";
const commonModulesList = ['react', 'react-dom'];

const reactRenderer = "react_renderer.js";
const reactRendererPath = './react_mpa/react_renderer.js';

let defaultEntries = {};
defaultEntries[reactRenderer] = reactRendererPath;
defaultEntries[commonModules] = commonModulesList;

// ref: https://webpack.js.org/configuration/entry-context/#entry
function entryMaker() {
    return glob.sync('./*/templates/**/*.js').reduce(
        (entries, path) => {
            let entry = path.replace(/templates\/.*\//, '');
            entries[entry] = {import: path, dependOn: commonModules}
            return entries
        }, defaultEntries)
}

module.exports = {
    entry: entryMaker,
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