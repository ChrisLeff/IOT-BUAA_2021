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
    <el-button type="primary" @click="getWorkData">检测当前数据</el-button>
    <p></p>
    <el-link type="primary" href="../../static/index1.html">查看温度折线图</el-link>
    <el-link type="primary" href="../../static/index2.html">查看湿度折线图</el-link>
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
      // console.log(begintime);
      // console.log(endtime);
      this.$axios.post(`${this.$store.state.origin}/get_history_status_page`, {
        begin_timestamp: begintime,
        end_timestamp: endtime
      }).then(
        res => {
          var times = res.data["timestamp"];
          var temps = res.data["temperature_data"];
          var humids = res.data["humidity_data"];
          var i;
          for(i = 0;i < times.length;i++) {
            if (times[i] >= begintime && times[i] <= endtime) {
              var data = {time: "", temprature:0, humidity:0};
              data["time"] = this.formatDate(times[i]);
              data["temprature"] = parseFloat(temps[i]).toFixed(2);
              data["humidity"] = humids[i];
              this.showdata.push(data);
            }
          }
          var fso=new ActiveXObject("Scripting.FileSystemObject");
          var f=fso.OpenTextFile("D:\\vscodeFile\\frontend\\static\\js\\data.txt", 2); //这里必须为绝对路径
          for(i = 0;i < this.showdata.length;i = i + 10) {
            f.Writeline(this.showdata[i]["time"] + " " + this.showdata[i]["temprature"] + " " + this.showdata[i]["humidity"]);
          }
        }
      ).catch((e) => {
        console.log(e);
      });
    },
    getWorkData() {
      this.$axios.post(`${this.$store.state.origin}/get_temperature_humidity`).then(
        res => {
          //console.log(res.data);
          this.humidAlert(res.data[1]["value"]);
          this.tempAlert(res.data[2]["value"]);
        }
      ).catch((e) => {
        console.log(e);
      });
    },
    tempAlert(temp) {
      //console.log(this.tempstd);
      //console.log(temp);
      if (temp > this.tempstd) {
        this.$axios.post(`${this.$store.state.origin}/turn_motor_on`).then(
          res => {
            this.$message({
              showClose: true,
              message: "温度超标",
              type: "warning"
            });
            setTimeout(() => {
              this.turnoff();
            }, 2000);
          }
        ).catch((e) => {
          console.log(e);
        });
      }
    },
    humidAlert(humid) {
      //console.log(this.humidstd);
      if (humid > this.humidstd) {
        this.$axios.post(`${this.$store.state.origin}/turn_motor_on`).then(
          res => {
            this.$message({
              showClose: true,
              message: "湿度超标",
              type: "warning"
            });
            setTimeout(() => {
              this.turnoff();
            }, 2000);
          }
        ).catch((e) => {
          console.log(e);
        });
      }
    },
    turnoff() {
      this.$axios.post(`${this.$store.state.origin}/turn_motor_off`).then(
        res => {
          console.log("turnoff");
        }
      ).catch((e) => {
        console.log(e);
      });
    },
    formatDate(value) {
      let date = new Date(value);
      let y = date.getFullYear();
      let MM = date.getMonth() + 1;
      MM = MM < 10 ? ('0' + MM) : MM;
      let d = date.getDate();
      d = d < 10 ? ('0' + d) : d;
      let h = date.getHours();
      h = h < 10 ? ('0' + h) : h;
      let m = date.getMinutes();
      m = m < 10 ? ('0' + m) : m;
      let s = date.getSeconds();
      s = s < 10 ? ('0' + s) : s;
      return y + '-' + MM + '-' + d + ' ' + h + ':' + m + ':' + s;
    },
    inquirebegin() {
      this.selectData();
      this.getWorkData();
    }
  },
  created() {
    this.inquirebegin();
    this.timer = window.setInterval(() => {
      setTimeout(() => {
          this.inquirebegin();
      },0)
    },20000)
  },
  destroyed() {
    window.clearInterval(this.timer)
  }
}
</script>

<style scoped>
.button{
  padding: 1%;
}
</style>
