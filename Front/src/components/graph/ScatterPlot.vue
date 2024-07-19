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

HighchartsMore(Highcharts);
Stock(Highcharts);
NoDataToDisplay(Highcharts);

const props = defineProps({
    name_x: { type: String, required: true },
    unit_x: { type: String, required: false, default: '' },
    data_x: { type: Array, required: true },
    name_y: { type: String, required: true },
    unit_y: { type: String, required: false, default: '' },
    data_y: { type: Array, required: true }
});

const chartContainer = ref(null);

const showChart = () => {
    const createChart = (container, seriesOptions, x_name, y_name) => {
        return Highcharts.chart(container, {
            chart: {
                type: 'scatter',
                zooming: {
                    type: 'xy'
                },
                backgroundColor: '#fafafa'
            },
            title: {
                text: `${x_name} × ${y_name}`
            },
            yAxis: {
                title: {
                    text: y_name
                },
                labels: {
                    format: '{value:.2f}'
                },
            },
            xAxis: {
                title: {
                    text: x_name
                },
                startOnTick: true,
                endOnTick: true,
                showLastLabel: true,
                labels: {
                    format: '{value:.2f}'
                },
            },
            tooltip: {
                pointFormat: `${x_name}: {point.x} ${props.unit_x} <br/> ${y_name}: {point.y} ${props.unit_y}`
            },
            exporting: {
                enabled: false
            },
            series: seriesOptions
        });
    };

    const seriesOptions = [{
        data: [],
        marker: {
            radius: 2.5,
            symbol: 'circle',
            states: {
                hover: {
                    enabled: true,
                    lineColor: 'rgb(100,100,100)'
                }
            }
        },
        states: {
            hover: {
                marker: {
                    enabled: false
                }
            }
        },
        jitter: {
            x: 0.005
        }
    }];

    const newData = props.data_x.map((x, i) => [x, props.data_y[i]]);
    seriesOptions[0].data = newData;

    createChart(chartContainer.value, seriesOptions, props.name_x, props.name_y);
};

onMounted(() => {
    if (chartContainer.value) {
        showChart();
    }
});
</script>

<style scoped>
.highcharts-figure .chart-container {
    width: 100%;
    max-height: 30%;
    aspect-ratio: 2 / 1;
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
