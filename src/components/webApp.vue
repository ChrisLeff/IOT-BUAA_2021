<template>
  <div>
    <div class="block">
      <p></p>
      <span class="demonstration">请选择时间范围</span>
      <el-date-picker
        v-model="datetime"
        type="datetimerange"
        range-separator="至"
        start-placeholder="开始时间"
        end-placeholder="结束时间">
      </el-date-picker>
      <el-button type="primary" @click="selectData()">查询</el-button>
      <p></p>
    </div>
    <div class="change">
      <p></p>
      温度阈值:<el-input size="medium" v-model="tempstd" placeholder="请输入内容" style="width:25%"></el-input>
      <p></p>
      湿度阈值:<el-input size="medium" v-model="humidstd" placeholder="请输入内容" style="width:25%"></el-input>
      <p></p>
    </div>
    <el-button type="primary" @click="getWorkData">检测当前数据</el-button> <el-link type="primary" href="../../static/index.html">查看折线图</el-link>
    <el-table :data="showdata" style="width: 100%">
      <el-table-column prop="temprature" label="温度"></el-table-column>
      <el-table-column prop="humidity" label="湿度"></el-table-column>
      <el-table-column prop="time" label="时间"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import { setTimeout } from "timers";
export default {
  data () {
    return {
      showdata: [],
      newdata: [],
      datetime: '',
      tempstd: 0,
      humidstd: 0
    };
  },
  methods: {
    selectData() {
      this.showdata = [];
      var begintime;
      var endtime;
      if (this.datetime != null && this.datetime != '') {
        begintime = this.datetime[0].getTime();
        endtime = this.datetime[1].getTime();
      } else {
        begintime = 0;
        endtime = new Date().getTime();
      }
      this.$axios.post(`${this.$store.state.origin}/get_history_status_page`, {
        begin_timestamp: begintime,
        end_timestamp: endtime
      }).then(
        res => {
          var times = res.data["timestamp"];
          var temps = res.data["temperature_data"];
          var humids = res.data["humidity_data"];
          var data = {};
          for(i = 0;i < times.length;i++) {
            if (times[i] >= begintime && times[i] <= endtime) {
              data["time"] = (new Date(times[i])).toLocaleString;
              data["temprature"] = temps[i];
              data["humidity"] = humids[i];
            }
            this.showdata.push(data);
          }
        }
      ).catch((e) => {
        console.log(e);
      });
    },
    getWorkData() {
      this.$axios.get(`${this.$store.state.origin}/get_temperature_humidity`, {
        params: {}
      }).then(
        res => {
          console.log(res.data);
          console.log(JSON.parse(res.data));
          this.tempAlert(res.data[1]["value"]);
          this.humidAlert(res.data[0]["value"]);
        }
      ).catch((e) => {
        console.log(e);
      });
    },
    tempAlert(temp) {
      if (temp > this.tempstd) {
        this.$axios.post(`${this.$store.state.origin}/turn_motor_on`).then(
          res => {
            this.$alert('温度超标', '警告', {
              confirmButtonText: '确定'
            });
          }
        ).catch((e) => {
          console.log(e);
        });
      }
    },
    humidAlert(humid) {
      if (humid > this.humidstd) {
        this.$axios.post(`${this.$store.state.origin}/turn_motor_on`).then(
          res => {
            this.$alert('湿度超标', '警告', {
              confirmButtonText: '确定'
            });
          }
        ).catch((e) => {
          console.log(e);
        });
      }
    },
    created() {
      this.selectData();
    }
  }
}
</script>

<style scoped>
.button{
  padding: 1%;
}
</style>
