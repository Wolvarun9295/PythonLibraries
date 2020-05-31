$(document).ready(function () {
    $(chart1_id).highcharts({
        chart: chart1,
        title: title1,
        xAxis: xAxis1,
        yAxis: yAxis1,
        series: series1,
        plotOptions: plotOptions1,
        tooltip: tooltip1,
        credits: credits
    });
});

$(document).ready(function () {
    $(chart2_id).highcharts({
        chart: chart2,
        title: title2,
        xAxis: xAxis2,
        yAxis: yAxis2,
        series: series2,
        plotOptions: plotOptions2,
        tooltip: tooltip1,
        credits: credits
    })
});

$(document).ready(function () {
    $(chart3_id).highcharts({
        chart: chart3,
        title: title3,
        series: series3,
        yAxis: yAxis3,
        xAxis: xAxis3,
        plotOptions: plotOptions3,
        tooltip: tooltip1,
        credits: { enabled: false },
        pane: pane3
    });
});

$(document).ready(function () {
    $(chart4_id).highcharts({
        chart: chart4,
        title: title4,
        series: series4,
        yAxis: yAxis4,
        xAxis: xAxis4,
        plotOptions: plotOptions4,
        tooltip: tooltip1,
        credits: credits
    });
});

$(document).ready(function () {
    $(chart5_id).highcharts({
        chart: chart5,
        title: title5,
        series: series5,
        yAxis: yAxis5,
        xAxis: xAxis5,
        plotOptions: plotOptions5,
        tooltip: tooltip2,
        credits: credits
    });
});

$(document).ready(function () {
    $(chart6_id).highcharts({
        chart: chart6,
        title: title6,
        xAxis: xAxis6,
        yAxis: yAxis6,
        series: series6,
        plotOptions: plotOptions6,
        tooltip: tooltip2,
        credits: credits,
        pane: pane6
    });
});