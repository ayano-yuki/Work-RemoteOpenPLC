import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios';

export const config_data = defineStore('config_data', () => {
    const api_url = ref("http://127.0.0.1:8000")

    function get_api_url(){
        return api_url.value
    }

    return { get_api_url }
})