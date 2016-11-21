var path = require('path');
var webpack = require('webpack');

var src_path = path.join(__dirname, 'src')
var dst_path = path.join(__dirname, 'dst')

module.exports = {
    entry: {
        index: path.join(src_path, 'index.js'),
    },
    output: {
        filename: '[name].js',
        path: dst_path,
    },
    module: {
        // preLoaders: [
        //     {
        //         test: /\.tag$/,
        //         loader: 'riotjs-loader',
        //         query: {type: 'none'},
        //         exclude: /(node_modules|bower_components)/,
        //     },
        // ],
        loaders: [
            {
                test: /\.tag$/,
                loader: 'riotjs-loader',
                query: {type: 'none'},
                exclude: /(node_modules|bower_components)/,
            },
        ],
    },
    plugins: [
        new webpack.ProvidePlugin({
            riot: 'riot',
        }),
    ],
}
