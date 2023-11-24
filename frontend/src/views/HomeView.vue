<template>
  <div class="form-container">
    <h4 class="text-center">Register</h4>
    <input type="text" v-model="username" placeholder="Username" />
    <input type="email" v-model="email" placeholder="Email" />
    <input type="password" v-model="password" placeholder="Password" />
    <button @click="register">
      <span v-if="loading" class="spinner-border spinner-border-sm"></span>
      <span v-else>Register</span>
    </button>

    <p>Already have an account? <router-link to="/login">Login</router-link></p>
  </div>
</template>

<script>
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      loading: false,
    };
  },
  methods: {
    async register() {
      this.loading = true;
      try {
        const response = await this.$axios.post("/register", {
          username: this.username,
          email: this.email,
          password: this.password,
        });
        console.log(response.data);
        if (response.data === "ok") {
          this.loading = false;
          toast.success("logging ..", {
            autoClose: 7000,
            transition: "zoom",
            position: toast.POSITION.BOTTOM_CENTER,
            theme: "dark",
          });
          this.$router.push("/login");
        }
        if (response.data === "User already exists") {
          this.loading = false;
          toast.error("User already exists", {
            autoClose: 7000,
            transition: "zoom",
            position: toast.POSITION.BOTTOM_CENTER,
            theme: "dark",
          });
        }
      } catch (error) {
        this.loading = false;
        toast.error(error?.message, {
          autoClose: 7000,
          transition: "zoom",
          position: toast.POSITION.BOTTOM_CENTER,
          theme: "dark",
        });
        console.log(error);
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

.form-container p {
  margin-top: 20px;
  text-align: center;
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
