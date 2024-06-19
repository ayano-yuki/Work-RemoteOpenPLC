<template>
	<div id="str-title">Setting</div>
	<TopicPath id="topicpath"></TopicPath>

	<div id="forms" class="forms-container">
		<h1>Please enter the data to display</h1>
		<div v-for="(form, index) in forms" :key="index" class="form-replication_target">
			<table>
				<tr>
					<td>Name</td>
					<td><input type="text" Autocomplete="off" v-model="form.Name" name="Name"></td>
				</tr>
				<tr>
					<td>Address</td>
					<td><input type="number" Autocomplete="off" v-model="form.Address" name="Address"></td>
				</tr>
				<tr>
					<td>Max</td>
					<td><input type="number" Autocomplete="off" v-model="form.Max" name="Max"></td>
				</tr>
				<tr>
					<td>Min</td>
					<td><input type="number" Autocomplete="off" v-model="form.Min" name="Min"></td>
				</tr>
				<tr>
					<td>Unit</td>
					<td><input type="text" Autocomplete="off" v-model="form.Unit" name="Unit"></td>
				</tr>
				<tr>
					<td>Division result</td>
					<td><input type="number" Autocomplete="off" v-model="form.Division" name="Division"></td>
				</tr>
				<tr>
					<td>Multiplication result</td>
					<td><input type="number" Autocomplete="off" v-model="form.Multiplication" name="Multiplication"></td>
				</tr>
				<tr>
					<td>Generate graph</td>
					<td>
						<input type="radio" value="none" v-model="form.Graph">none
						<input type="radio" value="x" v-model="form.Graph">x
						<input type="radio" value="y" v-model="form.Graph">y
					</td>
				</tr>
			</table>

			<button @click="addForm" :disabled="forms.length >= 10">Add</button>
			<button @click="removeForm(index)" :disabled="forms.length <= 1">Delete</button>
		</div>

		<button @click="SaveSetting()">Save</button>
	</div>
</template>

<script setup>
import TopicPath from '@/components/TopicPath.vue';
import { config_data } from '@/stores/counter';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const forms = ref([
	{ Name: '', Address: '', Max: null, Min: null, Unit: '', Division: 1, Multiplication: 1, Graph: "none" }
]);

const addForm = () => {
	if (forms.value.length < 10) {
		forms.value.push({ Name: '', Address: '', Max: null, Min: null, Unit: '', Division: 1, Multiplication: 1, Graph: "none" });
	}
};

const removeForm = (index) => {
	if (forms.value.length > 1) {
		forms.value.splice(index, 1);
	}
};

onMounted(async () => {
	try {
        const response = await fetch("../../public/json/setting.json");
        const data = await response.json();
        forms.value = data;
    } catch (error) {
        console.error("Error fetching data:", error);
    }
});

const SaveSetting = async () => {
    const isValid = forms.value.every((form) => {
        const isNotEmpty = form.Name.trim() !== '' &&
                           form.Unit.trim() !== '';

        const isNumeric = !isNaN(form.Address) &&
                          !isNaN(form.Max) &&
                          !isNaN(form.Min) &&
                          !isNaN(form.Division) &&
                          !isNaN(form.Multiplication);

        const isMinLessThanMax = parseFloat(form.Min) < parseFloat(form.Max);
        const isSameTitle = new Set(forms.value.map(item => item.Name)).size === forms.value.length;

        return isNotEmpty && isNumeric && isMinLessThanMax && isSameTitle;
    }) && checkGraphCondition();

    if (isValid) {
        const jsonData = JSON.stringify(forms.value, null, 2);

        try {
            const res = await axios.post(
                config_data().get_api_url() + "/save_setting",
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
    else {
        alert('Input Error: Please fill in all fields properly before saving.');
    }
};

const checkGraphCondition = () => {
    let result_x = 0;
    let result_y = 0;

    forms.value.forEach((form) => {
        if (form.Graph === "x") {
            result_x += 1;
        } else if (form.Graph === "y") {
            result_y += 1;
        }
    });

    return (result_x === 1 && result_y === 1) || (result_x === 0 && result_y === 0);
};
</script>

<style scoped>
#forms {
	position: absolute;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -45%);
	height: 80vh;
	width: 90vw;
	overflow-y: auto;
	display: flex;
	flex-direction: column;
	justify-content: flex-start;
	align-items: center;
}

.form-replication_target {
	margin-bottom: 10px;
}

.form-replication_target:last-child {
	margin-bottom: 0;
}
</style>
