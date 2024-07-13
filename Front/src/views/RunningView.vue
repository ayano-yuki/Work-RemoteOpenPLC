<template>
	<TopicPath id="topicpath"></TopicPath>
	<div id="str-title"> Running </div>

	<div>
		<img class="camera" @click="" />
	</div>

	<div class="gauge-container">
		<GaugeGraph v-for="(form, index) in forms" :key="index" :name=form.Name :max=form.Max
			:min=form.Min :unit=form.Unit>
		</GaugeGraph>
	</div>

	<div class="line-container">
		<LineGraph v-for="(form, index) in forms" :key="index" :name=form.Name :max=form.Max
			:min=form.Min :unit=form.Unit :numDataPoints="30">
		</LineGraph>
	</div>

	<div id="buttons">
		<div id="contens-center">
			<RunController></RunController>
			<GeneratorButton></GeneratorButton>
			<ResultController></ResultController>
		</div>
	</div>

</template>

<script setup>
import TopicPath from '@/components/TopicPath.vue';
import LineGraph from '@/components/graph/LineGraph.vue';
import GaugeGraph from '@/components/graph/GaugeGraph.vue';
import RunController from '@/components/button/RunController.vue'
import ResultController from '@/components/button/ResultController.vue'
import GeneratorButton from '@/components/button/GeneratorButton.vue'
import { config_data, controller_experiment } from '@/stores/counter'
import { ref, onMounted } from 'vue';
import axios from 'axios';

const experiment = controller_experiment();
const forms = ref([]);
const clock = ref(100);

onMounted(async () => {
	try {
		const response = await fetch("../../public/json/setting.json");
		const data = await response.json();
		forms.value = data;
	} catch (error) {
		console.error("Error fetching data:", error);
	}
});


setInterval(async () => {
	if (experiment.now_mode()) {
		try {
			const res = await axios.get(config_data().get_api_url() + "/get_experiment_result");
			for (var i in forms.value) {
				var push_data = res.data.result[Number(forms.value[i]["Address"])] * Number(forms.value[i]["Multiplication"]) / Number(forms.value[i]["Division"])
				experiment.push_result(forms.value[i]["Name"], push_data)
			}

		} catch (error) {
			console.error('Error fetching data:', error);
		}
	}
}, clock.value);
</script>

<style scoped>
.camera {
	position: absolute;
	top: 17vh;
	right: 5vw;
	width: 25%;
	background-color: var(--color-camera-background);
	aspect-ratio: 16 / 11;
}

.gauge-container {
	position: absolute;
	bottom: 9vh;
	left: 7vw;
	width: 60%;
	height: 35%;
	display: flex;
	align-items: center;
	white-space: nowrap;
	overflow-x: auto;

	border-top: solid 5px var(--color-box-border);
	box-shadow: 0 3px 5px var(--color-box-shadow);
}

.line-container {
	position: absolute;
	top: 17vh;
	left: 7vw;
	width: 60%;
	height: 35%;
	display: flex;
	align-items: center;
	white-space: nowrap;
	overflow-x: auto;

	border-top: solid 5px var(--color-box-border);
	box-shadow: 0 3px 5px var(--color-box-shadow);
}

#buttons {
	position: absolute;
	bottom: 11.5vh;
	right: 5vw;
	width: 25%;
	height: 35%;
}

#contens-center {
	position: absolute;
	width: 80%;
	height: 100%;
	left: 45%;
	transform: translateX(-50%);
}
</style>