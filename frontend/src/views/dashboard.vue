<template>
  <div class="dashboard">
    <div class="wrapper">
      <h1>Dashboard</h1>
      <p>
        Welcome to your dashboard, <strong>{{ user }}</strong
        >!
      </p>
      <p>
        <a @click="logout" href="#" class="logout">Logout</a>
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
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("user");
      toast("Logging out!", {
        autoClose: 3000,
      });
      this.$router.push("/login");
    },
  },

  mounted() {
    this.user = localStorage.getItem("user");

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
</style>
