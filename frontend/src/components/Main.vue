<template>
  <div class="main-container">
    <h1>머신러닝으로 로또를 예측해보세요</h1>
    <hr><br><br>
    <div class="circle-container">
      <div v-for="(lotto_result, index) in lotto_results" :key="index">
        <div 
          :class="['circle', lotto_result.color]"
        >
          {{ lotto_result.value }}
        </div>
      </div>
      
    </div>
    <div class="button-container">
      <b-button @click="onClick()">CLICK</b-button>
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
      lotto_results: []
    };
  },
  methods: {
    onClick() {
      const path = '/api/lottoml';
      axios.get(path)
        .then((res) => {
          // console.log(res.data.lotto_result)
          const _result = res.data.lotto_result.map(i => {
            if (i >= 0 && i <= 10) return { value: i, color: 'yellow' };
            if (i >= 11 && i <= 20) return { value: i, color: 'blue' };
            if (i >= 21 && i <= 30) return { value: i, color: 'red' };
            if (i >= 31 && i <= 40) return { value: i, color: 'grey' };
            return { value: i, color: 'green' };
          });
          // console.log('>>>', _result);
          this.lotto_results = _result;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    
  },
  // created() {
    
  // },
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
  width:80px;
  height:80px;
  border-radius:75px;
  /* text-align:center; */
  color: #ffffff;
  margin:1em;
  font-size:20px;
  vertical-align:middle;
  line-height:80px;
}

.circle.green {
  background-color: #8adb76;
  
}

.circle.yellow {
  background-color: rgb(252, 255, 80);
  color: rgb(51, 51, 51);
}

.circle.blue {
  background-color: rgb(75, 174, 255);
}

.circle.red {
  background-color: rgb(255, 108, 82);
}

.circle.grey {
  background-color: rgb(136, 136, 136);
}
.button-container {
  padding: 100px;
}
button{
  background-color:#1d00be;
}

</style>