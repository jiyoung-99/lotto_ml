<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>CONTACT OUR DEVELOPER</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.support-modal>Add question</button>
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
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.support-update-modal
                          @click="editSupport(support)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteSupport(support)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  <!--모달창-->
    <b-modal ref="addSupportModal"
          id="support-modal"
          title="Add a new question"
          hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addSupportForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-writer-group"
                      label="Writer"
                      label-for="form-writer-input">
            <b-form-input id="form-writer-input"
                          type="text"
                          v-model="addSupportForm.writer"
                          required
                          placeholder="Enter writer">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-content-group"
                      label="Content"
                      label-for="form-content-input">
            <b-form-input id="form-content-input"
                          type="text"
                          v-model="addSupportForm.content"
                          required
                          placeholder="Enter content">
            </b-form-input>
          </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <!--수정 모달-->
    <b-modal ref="editSupportModal"
            id="support-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-writer-edit-group"
                      label="Writer"
                      label-for="form-writer-edit-input">
            <b-form-input id="form-writer-edit-input"
                          type="text"
                          v-model="editForm.writer"
                          required
                          placeholder="Enter writer">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group"
                      label="Content"
                      label-for="form-content-edit-input">
            <b-form-input id="form-content-edit-input"
                          type="text"
                          v-model="editForm.content"
                          required
                          placeholder="Enter content">
            </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      supports: [],
      addSupportForm: {
        title: '',
        writer: '',
        content: ''
      },
      editForm: {
        id: '',
        title: '',
        writer: '',
        content: '',
        
      },
      
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getSupports() {
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
    addSupport(payload) {
      const path = 'http://localhost:5000/support';
      axios.post(path, payload)
        .then(() => {
          this.getSupports();
          this.message = '문의가 등록되었습니다';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getSupports();
        });
    },
    updateSupport(payload, s_ID) {
      const path = `http://localhost:5000/support/${s_ID}`;
      axios.put(path, payload)
        .then(() => {
          this.getSupports();
          this.message = '수정이 완료되었습니다.';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getSupports();
        });
    },
    removeSupport(s_ID) {
      const path = `http://localhost:5000/support/${s_ID}`;
      axios.delete(path)
        .then(() => {
          this.getSupports();
          this.message = '삭제되었습니다.';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getSupports();
        });
    },
    onDeleteSupport(support) {
      this.removeSupport(support.id);
    },
    initForm() {
      this.addSupportForm.title = '';
      this.addSupportForm.writer = '';
      this.addSupportForm.content = '';
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.writer = '';
      this.editForm.content = '';
    },

    editSupport(support) {
          this.editForm = support;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      // let read = false;
      // if (this.addSupportForm.read[0]) read = true;
      const payload = {
        title: this.addSupportForm.title,
        writer: this.addSupportForm.writer,
        content: this.addSupportForm.content
      };
      this.addSupport(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSupportModal.hide();
      // let read = false;
      // if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        writer: this.editForm.writer,
        content: this.editForm.content,
      };
      this.updateSupport(payload, this.editForm.id);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSupportModal.hide();
      this.initForm();
      this.getSupports(); // why?
},

  },
  created() {
    this.getSupports();
  },
};
</script>