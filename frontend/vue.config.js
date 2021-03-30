module.exports = {
    devServer: {
      proxy: {
        "/api": {
          target: "http://localhost:5000",
          pathRewrite: { "^/api/": "/api/" },
          timeout: 10000,
          secure: false,
          changeOrigin: true,
          logLevel: "debug"
        }
      }
    }
  }