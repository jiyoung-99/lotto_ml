<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>CONTACT OUR DEVELOPER</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add question</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Writer</th>
              <th scope="col">Content</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(support, index) in supports" :key="index">
              <td>{{ support.title }}</td>
              <td>{{ support.writer }}</td>
              <td>{{ support.content }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>

import axios from 'axios';

export default {
  data() {
    return {
      supports: [],
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/support';
      axios.get(path)
        .then((res) => {
          this.supports = res.data.supports;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>