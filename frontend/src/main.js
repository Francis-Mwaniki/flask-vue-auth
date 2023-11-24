import './assets/main.css'
import Vue3Toasity from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import { toast } from 'vue3-toastify';
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios';
import App from './App.vue'
import router from './router'

const app = createApp(App)
axios.defaults.baseURL = 'http://127.0.0.1:5000';

app.config.globalProperties.$axios = axios;
app.use(createPinia())
app.use(  Vue3Toasity,
    {
        autoClose: 7000,
        position: toast.POSITION.BOTTOM_CENTER,
        theme: "dark",
      // ...
    } )
app.use(router)

app.mount('#app')
