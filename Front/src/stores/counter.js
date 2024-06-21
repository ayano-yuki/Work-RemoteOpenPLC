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

export const controller_experiment = defineStore('controller_experiment', () => {
    const flag_run_mode   = ref(false)
    const flag_reset   = ref(true)
    const result = ref({})

    function now_mode(){
        return flag_run_mode.value
    }

    function is_reset(){
        return flag_reset.value
    }

    async function start_experiment() {
        flag_run_mode.value = true
        flag_reset.value = false
   }

    async function stop_experiment() {
        flag_run_mode.value = false
    }

    function create_dict(name) {
        result.value[name] = []
    }

    function push_result(name, newResult) {
        if ( !(name in result.value) ) {
            result.value[name] = []
        }

        console.log(name, result.value)
        result.value[name].push(newResult)
    }

    function clear_result() {
        for (var key in result.value){
            result.value[key] = []
        }
        flag_reset.value = true
    }

    function get_result_list(name){
        return result.value[name]
    }

    function get_result_latest(name){
        if ( !(name in result.value) ) {
            return 0
        }
        else {
            return result.value[name].slice(-1)[0]
        }
    }

    return { 
        result,
        start_experiment, stop_experiment, now_mode, is_reset,
        create_dict, push_result, clear_result, get_result_list, get_result_latest, 
    }
})