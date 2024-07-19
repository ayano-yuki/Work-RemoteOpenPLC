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
import SolidGauge from 'highcharts/modules/solid-gauge';

import { controller_experiment } from '@/stores/counter'

HighchartsMore(Highcharts);
Stock(Highcharts);
NoDataToDisplay(Highcharts);
SolidGauge(Highcharts);

const props = defineProps(['name', 'max', 'min', 'unit']);
const chartContainer = ref(null);
const experiment = controller_experiment();

const showChart = () => {
    const createChart = (container, yAxisOptions, seriesOptions) => {
        return Highcharts.chart(container, Highcharts.merge(gaugeOptions, {
            yAxis: yAxisOptions,
            series: [seriesOptions],
        }));
    };

    const gaugeOptions = {
        chart: {
            type: 'solidgauge',
            backgroundColor: '#fafafa',
        },
        title: null,
        pane: {
            center: ['50%', '85%'],
            size: '140%',
            startAngle: -90,
            endAngle: 90,
            background: {
                backgroundColor: Highcharts.defaultOptions.legend.backgroundColor || '#EEE',
                innerRadius: '60%',
                outerRadius: '100%',
                shape: 'arc',
            },
        },
        exporting: {
            enabled: false,
        },
        tooltip: {
            enabled: false,
        },
        yAxis: {
            lineWidth: 0,
            tickWidth: 0,
            minorTickInterval: null,
            tickAmount: 2,
            title: {
                y: -70,
            },
            labels: {
                y: 16,
            	format: '{value:.2f}', // 小数点以下３桁にフォーマットする
            },
        },
        plotOptions: {
            solidgauge: {
                dataLabels: {
                    y: 5,
                    borderWidth: 0,
                    useHTML: true,
                },
            },
        },
    };

    const targetChart = createChart(chartContainer.value, {
        min: Number(props.min),
        max: Number(props.max),
        title: {
            text: props.name,
        },
    }, {
        name: props.name,
        data: [experiment.get_result_latest(props.name)],
        dataLabels: {
            format: '<div style="text-align:center">' +
                '<span style="font-size:25px">{y:.2f}</span><br/>' +
                '<span style="font-size:12px;opacity:0.4">' +
                props.unit +
                '</span>' +
                '</div>',
        },
        tooltip: {
            valueSuffix: props.unit,
        },
    });

    setInterval(() => {
        if (experiment.now_mode()) {
            const resultData = experiment.get_result_latest(props.name);
            targetChart.series[0].setData([Number(resultData)], true);
        }

        else if (experiment.is_reset()){
            targetChart.series[0].setData([0], true);
        }

        // else {
        //     targetChart.series[0].setData([0], true, true);
        // }
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
