<template>
  <div class="form-container">
    <h4 class="text-center">Update password</h4>
    <!-- Update Password Form Elements -->
    <input type="text" v-model="resetToken" placeholder="Reset Token" />
    <input type="password" v-model="newPassword" placeholder="New Password" />
    <button @click="updatePassword">Update Password</button>
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
    };
  },
  methods: {
    async updatePassword() {
      try {
        const response = await this.$axios.post("/update-password", {
          reset_token: this.resetToken,
          new_password: this.newPassword,
        });

        if (response.data === "ok") {
          toast("Password updated!", {
            autoClose: 3000,
          });
          this.$router.push("/login");
        }
        toast("invalid token", {
          autoClose: 3000,
        });
      } catch (error) {
        toast("invalid password!", {
          autoClose: 3000,
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
</style>
