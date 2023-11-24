<template>
  <div class="dashboard">
    <div class="wrapper">
      <h1>Dashboard</h1>
      <p>
        Welcome to your dashboard,
        <strong>
          <span v-if="loading" class="spinner-border spinner-border-sm"></span>
          <span v-else>{{ user }}</span>
        </strong>
      </p>
      <p>
        <a @click="logout" href="#" class="logout">
          <span v-if="logging_out" class="spinner-border spinner-border-sm"></span>
          <span v-else>Logout</span>
        </a>
      </p>
    </div>
  </div>
</template>

<script>
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
export default {
  data() {
    return {
      user: localStorage.getItem("user"),
      loading: true,
      logging_out: false,
    };
  },
  methods: {
    logout() {
      this.logging_out = true;
      localStorage.removeItem("user");
      toast.info("Logging out!", {
        autoClose: 7000,
        transition: "zoom",
        position: toast.POSITION.BOTTOM_CENTER,
        theme: "dark",
      });
      setTimeout(() => {
        this.logging_out = false;
        this.$router.push("/login");
      }, 7000);
    },
  },

  mounted() {
    this.user = localStorage.getItem("user");

    setTimeout(() => {
      this.loading = false;
    }, 5000);

    if (!this.user) {
      this.$router.push("/login");
    }
  },
};
</script>

<style scoped>
.dashboard {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
.dashboard .logout {
  color: #000000;
  text-decoration: none;
  cursor: pointer;
  font-weight: bold;
  background-color: #d40505;
  padding: 10px;
  border-radius: 5px;
  text-transform: uppercase;
}

.dashboard .logout:hover {
  color: #ffffff;
  background-color: #000000;
}
.wrapper {
  text-align: center;
}

.wrapper h1 {
  margin-bottom: 20px;
  font-weight: bold;
  text-transform: uppercase;
}

.wrapper p {
  margin-top: 20px;
  text-align: center;
}

.wrapper p a {
  color: #000000;
  text-decoration: none;
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
