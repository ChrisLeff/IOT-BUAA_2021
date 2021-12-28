<template>
  <el-container id="app">
    <el-header>
      温湿度自动检测系统
    </el-header>
    <el-main>
      <router-view/>
    </el-main>
  </el-container>
</template>

<script>
import webApp from "@/components/webApp"
import  "babel-polyfill"
export default {
  name: 'App',
  components: {
    webApp: webApp
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.el-header {
  font-size: 30px;
}
</style>
