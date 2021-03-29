<template>
  <div class="lotto-container">
    <div class="main-label">
      <label >회차바로가기</label>
      <b-form-select
        id="select-id"
        v-model="tableVariant"
        :options="tableVariants"
        @change="onSelectBtnChange(tableVariant)"
        
      >
        <template #first>
          <option value="">-- None --</option>
        </template>
      </b-form-select>
    </div>

    <table class="table table-hover">
      <thead>
            <tr>
              <th scope="col">순위</th>
              <th scope="col">당첨게임 수</th>
              <th scope="col">1게임당 당첨금액</th>
              <th scope="col">1</th>
              <th scope="col">2</th>
              <th scope="col">3</th>
              <th scope="col">4</th>
              <th scope="col">5</th>
              <th scope="col">6</th>
              <th scope="col">Bonus</th>
            </tr>
          </thead>
      <tbody>
        
        <tr>
          <td>1등</td>
          <td>{{item.first_num}}</td>
          <td>{{item.first_cnt}}</td>
          <td>{{item.one}}</td>
          <td>{{item.two}}</td>
          <td>{{item.three}}</td>
          <td>{{item.four}}</td>
          <td>{{item.five}}</td>
          <td>{{item.six}}</td>
          <td>{{item.bonus}}</td>
        </tr>

      </tbody>

    </table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      fields: ['순위', '당첨게임 수', '1게임당 당첨금액', '1', '2', '3', "4", "5", "6", "보너스"],
      item: {},
      tableVariants:[],
      striped: false,
      bordered: false,
      borderless: false,
      outlined: false,
      small: false,
      hover: false,
      dark: false,
      fixed: false,
      footClone: false,
      headVariant: null,
      tableVariant: '',
      noCollapse: false
    }
  },
  methods: {
    getLottoId() {
      const path = "/api/lottohis";
      axios.get(path)
      .then((res) => {
        // console.log(res.data)
        this.tableVariants = res.data.lottohis_id
      })
      .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getLottoId();
      });
    },
    getLottoOne(tableVariant) {
      const path = `/api/lottohis/one/${tableVariant}`
      axios.get(path)
      .then((res) => {
        this.item = res.data.selectLottoOne
        // console.log(this.item)
      })
      .catch((error) => {
        console.log(error)
      });

    },

    onSelectBtnChange(id) {
      console.log("change", id)
      this.getLottoOne(id)
    }
  },
  created() {
    this.getLottoId();
  },


}
</script>
<style>
.lotto-container{
  /* margin-top: 10em; */
  box-sizing: border-box;
  /* display: flex; */
  padding: 20px;
  margin: 7em auto auto;
  max-width: 100%;
  width: 1000px;
}
.table{
  margin: 7em auto auto;
}
.form-row form-group{
  width: 20em;
}
#select-id{
  float: right;
  width: 12em;
}
.main-label {
  float: right;
  width: 15em;
}




</style>
