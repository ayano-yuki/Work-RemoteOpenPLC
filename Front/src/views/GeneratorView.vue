<template>
    <div id="str-title"> Generator </div>

    <div id="content">
        <Scatter 
            v-if="dataLoaded"
            :name_x="nameX" 
            unit_x="unit" 
            :data_x="dataX" 
            :name_y="nameY" 
            unit_y="unit" 
            :data_y="dataY"
        ></Scatter>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Scatter from '@/components/graph/ScatterPlot.vue';

const nameX = ref('');
const dataX = ref([]);
const nameY = ref('');
const dataY = ref([]);
const dataLoaded = ref(false);

const loadJsonData = async () => {
    try {
        const response = await fetch('../../../public/json/result.json');
        const jsonData = await response.json();

        jsonData.forEach(item => {
            if (item.Graph === 'x') {
                nameX.value = item.Name;
                dataX.value = item.Data;
            } else if (item.Graph === 'y') {
                nameY.value = item.Name;
                dataY.value = item.Data;
            }
        });

        dataLoaded.value = true;
    } catch (error) {
        console.error('Error loading JSON data:', error);
    }
};

onMounted(() => {
    loadJsonData();
});
</script>

<style scoped>
#content {
    position: absolute;
    width: 90%;
    height: 75%;
    top: 53%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
}
</style>
