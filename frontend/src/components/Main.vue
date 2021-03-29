<template>
  <div class="main-container">
    <h1>머신러닝으로 로또를 예측해보세요</h1>
    <hr><br><br>
    <div class="circle-container">
      <div class="circle">
        1
      </div>
      <div class="circle">
        1
      </div>
      <div class="circle">
        1
      </div>
      <div class="circle">
        1
      </div>
      <div class="circle">
        1
      </div>
      <div class="circle">
        1
      </div>
    </div>
    <div class="button-container">
      <b-button @click.native="onClick()">CLICK</b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Main',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    onClick() {
      const path = '/api/lottoml';
      axios.get(path)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getMessage() {
      const path = '/api';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
<style>
.main-container{
  /* margin: 5em 0 10em; */
  padding: 100px;
}
.circle-container {
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 60%;
  margin:0 auto;
}
.circle {
  background-color:#e26868;
  width:80px;
  height:80px;
  border-radius:75px;
  /* text-align:center; */
  color: #ffffff;
  margin:0 auto;
  font-size:20px;
  vertical-align:middle;
  line-height:80px;
}
.button-container {
  padding: 100px;
}
button{
  background-color:#1d00be;
}

</style>