import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios';

export const config_data = defineStore('config_data', () => {
    const api_url = ref("http://127.0.0.1:8000")

    function get_api_url() {
        return api_url.value
    }

    return { get_api_url }
})

export const controller_experiment = defineStore('controller_experiment', () => {
    const config = config_data()
    const flag_run_mode = ref(false)
    const flag_reset = ref(true)
    const result = ref({})

    function now_mode() {
        return flag_run_mode.value
    }

    function is_reset() {
        return flag_reset.value
    }

    async function start_experiment() {
        try {
            const res = await axios.post(
                config.get_api_url() + "/start_experiment",
                "",
                {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    timeout: 5000
                }
            );
            flag_run_mode.value = true
            flag_reset.value = false

        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    async function stop_experiment() {
        try {
            const res = await axios.post(
                config.get_api_url() + "/stop_experiment",
                "",
                {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    timeout: 5000
                }
            );
            flag_run_mode.value = false
            save_result()

        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    async function save_result() {
        const response = await fetch("../../public/json/setting.json")
        const setting_data = await response.json();
        const output = ref([])

        for (var key in result.value) {
            for (var i in setting_data) {
                if (key == setting_data[i]["Name"]) {
                    output.value.push({
                        Name: key,
                        Data: result.value[key],
                        Graph: setting_data[i]["Graph"]
                    })
                }
            }
        }

        const jsonData = JSON.stringify(output.value, null, 2);
        try {
            const res = await axios.post(
                config_data().get_api_url() + "/save_result",
                jsonData,
                {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    timeout: 5000
                }
            );
        } catch (error) {
            console.error('Error saving data:', error);
        }
    }

    function create_dict(name) {
        result.value[name] = []
    }

    function push_result(name, newResult) {
        if (!(name in result.value)) {
            result.value[name] = []
        }

        result.value[name].push(newResult)
    }

    async function clear_result() {
        if (!now_mode()) {
            for (var key in result.value) {
                result.value[key] = []
            }
            flag_reset.value = true
            download_result()
        }
        else {
            alert("please stop experiment.")
        }

    }

    function download_result() {
        fetch('../../public/json/result.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'experiment_result.json';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }

    function get_result_list(name) {
        return result.value[name]
    }

    function get_result_latest(name) {
        if (!(name in result.value)) {
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