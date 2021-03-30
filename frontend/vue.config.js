module.exports = {
    devServer: {
      proxy: {
        "/api": {
          target: `http://${process.env.VUE_APP_API_HOST}:5000`,
          pathRewrite: { "^/api/": "/api/" },
          timeout: 10000,
          secure: false,
          changeOrigin: true,
          logLevel: "debug"
        }
      }
    }
  }