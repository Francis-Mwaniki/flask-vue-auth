<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="wrapper">
      <nav class="nav">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Fira+Sans&display=swap");
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: "Fira Sans", sans-serif;
  /* background-color: #f5f5f5; */
}
.wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}
.nav {
  display: flex;
  justify-content: center;
  background-color: #fff;
  gap: 20px;
  align-items: center;
  padding: 20px 0;
}

.nav a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.nav a:hover {
  color: #000;
}
</style>
