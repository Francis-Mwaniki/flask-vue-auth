import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios';
import App from './App.vue'
import router from './router'

const app = createApp(App)
axios.defaults.baseURL = 'http://127.0.0.1:5000';

app.config.globalProperties.$axios = axios;
app.use(createPinia())
app.use(router)

app.mount('#app')
