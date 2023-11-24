<template>
  <div class="form-container">
    <h4 class="text-center">Update password</h4>
    <!-- Update Password Form Elements -->
    <input type="text" v-model="resetToken" placeholder="Reset Token" />
    <input type="password" v-model="newPassword" placeholder="New Password" />
    <button @click="updatePassword">
      <span v-if="loading" class="spinner-border spinner-border-sm"></span>
      <span v-else>Update password</span>
    </button>
  </div>
</template>

<script>
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
export default {
  data() {
    return {
      resetToken: "",
      newPassword: "",
      loading: false,
    };
  },
  methods: {
    async updatePassword() {
      this.loading = true;
      try {
        const response = await this.$axios.post("/update-password", {
          reset_token: this.resetToken,
          new_password: this.newPassword,
        });

        if (response.data === "ok") {
          this.loading = false;
          toast.success("Password updated!", {
            autoClose: 7000,
            transition: "zoom",
            position: toast.POSITION.BOTTOM_CENTER,
            theme: "dark",
          });
          this.$router.push("/login");
        }
        toast.error("invalid token", {
          autoClose: 7000,
          transition: "zoom",
          position: toast.POSITION.BOTTOM_CENTER,
          theme: "dark",
        });
      } catch (error) {
        this.loading = false;
        toast.error("invalid password!", {
          autoClose: 7000,
          transition: "zoom",
          position: toast.POSITION.BOTTOM_CENTER,
          theme: "dark",
        });
        console.error(error); // Handle password update error
      }
    },
  },
};
</script>

<style scoped>
.form-container {
  display: flex;
  margin: 0 auto;
  padding: 20px;
  width: 100%;
  max-width: 400px;
  background-color: #ffffff;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  min-height: 50vh;

  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.form-container h4 {
  margin-bottom: 20px;
  font-weight: bold;
  text-transform: uppercase;
  text-align: center;
}
.form-container input {
  margin: 10px;
  padding: 10px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.form-container button {
  margin: 10px;
  padding: 10px;
  width: 330px;
  color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: rgb(0, 0, 0);
  cursor: pointer;
}
.form-container button:hover {
  background-color: rgb(0, 0, 0, 0.8);
}

input[type="text"],
input[type="email"],
input[type="password"] {
  display: block;
  margin: 10px;
  padding: 10px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus {
  outline: none;
  border-color: #aaa;
}
.spinner-border {
  display: inline-block;
  width: 1rem;
  height: 1rem;
  vertical-align: text-bottom;
  border: 0.2em solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  -webkit-animation: spinner-border 0.75s linear infinite;
  animation: spinner-border 0.75s linear infinite;
}

@-webkit-keyframes spinner-border {
  to {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes spinner-border {
  to {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

.text-center {
  text-align: center;
}

.spinner-border-sm {
  height: 1rem;
  border-width: 0.2em;
}
</style>
