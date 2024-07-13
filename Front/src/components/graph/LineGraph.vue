<template>
    <figure class="highcharts-figure">
        <div ref="chartContainer" class="chart-container"></div>
    </figure>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue';

import Highcharts from 'highcharts';
import HighchartsMore from 'highcharts/highcharts-more';
import Stock from 'highcharts/modules/stock';
import NoDataToDisplay from 'highcharts/modules/no-data-to-display';

import { controller_experiment } from '@/stores/counter'

HighchartsMore(Highcharts);
Stock(Highcharts);
NoDataToDisplay(Highcharts);

const props = defineProps(['name', 'max', 'min', 'unit', 'numDataPoints']);
const chartContainer = ref(null);
const experiment = controller_experiment();

const showChart = () => {
    const createChart = (container, yAxisOptions, seriesOptions) => {
        return Highcharts.chart(container, {
            chart: {
                type: 'line', // Set the chart type to 'line'
                backgroundColor: '#fafafa',
            },
            chart: {
                zooming: {
                    type: 'xy'
                }
            },
            title: null,
            yAxis: {
                title: {
                    text: props.name,
                },
                min: Number(props.min),
                max: Number(props.max),
            },
            series: [{
                name: props.name,
                data: [0],
            }],
            tooltip: {
                valueSuffix: " " + props.unit,
            },
            exporting: {
                enabled: false,
            },
        });
    };

    const targetChart = createChart(chartContainer.value, {
        title: {
            text: props.name,
        },
    });

    setInterval(() => {
        if (experiment.now_mode()) {
            if (experiment.get_result_list(props.name)) {
                const resultData = experiment.get_result_list(props.name);
                targetChart.series[0].setData(resultData, true, true);

                // if (resultData.length < props.numDataPoints) {
                //     targetChart.series[0].setData(resultData, true, true);
                // } else {
                //     const newData = resultData.slice(-props.numDataPoints);
                //     targetChart.series[0].setData(newData, true, true);
                // }
            }
        }

        else if (experiment.is_reset()){
            targetChart.series[0].setData([0], true);
        }
    }, 1);
};

onMounted(() => {
    if (chartContainer.value) {
        showChart();
    }
});
</script>

<style scoped>
.highcharts-figure .chart-container {
    width: 300px;
    height: 200px;
}

.highcharts-data-table table {
    font-family: Verdana, sans-serif;
    border-collapse: collapse;
    border: 1px solid var(--color-graph-border);
    margin: 10px auto;
    text-align: center;
    width: 100%;
    max-width: 500px;
}

.highcharts-data-table caption {
    padding: 1em 0;
    font-size: 1.2em;
    color: var(--color-graph-text);
}

.highcharts-data-table th {
    font-weight: 600;
    padding: 0.5em;
}

.highcharts-data-table td,
.highcharts-data-table th,
.highcharts-data-table caption {
    padding: 0.5em;
}

.highcharts-data-table thead tr,
.highcharts-data-table tr:nth-child(even) {
    background: var(--color-graph-background);
}

.highcharts-data-table tr:hover {
    background: var(--color-graph-background);
}
</style>