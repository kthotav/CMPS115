
var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

var parseTime = d3.time.format("%H:%M").parse;

var x = d3.time.scale().range([0, width]);

var y = d3.scale.linear().range([height, 0]);

var xAxis = d3.svg.axis().scale(x).orient("bottom");

var yAxis = d3.svg.axis().scale(y).orient("left");

var line = d3.svg.line()
  .interpolate("basis")
  .x(function(d) { return x(d.TimeStamp); })
  .y(function(d) { return y(d.Temperature); });


var svg = d3.select("body").append("svg")
   .attr("width", width + margin.left + margin.right)
   .attr("height", height + margin.top + margin.bottom)
   .append("g")
   .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var dropDown = d3.select("#filter").append("select")
                  .attr("name", "date-list");

d3.csv("BMSOne.csv", function(error, data) {

  dataset = data.filter(function (d){
    return d.VarDate === "2015-05-01";
  });


   dataset.forEach(function(d) {
      d.TimeStamp = +parseTime(d.TimeStamp);
      d.Temperature = +d.Temperature;
      d.RelateiveHumidity = +d.RelateiveHumidity;
      d.COtwo = +d.COtwo;
      d.SensibleHeat = d.SensibleHeat;
      d.VarDate = d.VarDate;
   });

   dataDates = ["2015-05-01", "2015-05-02", "2015-05-03", "2015-05-04", "2015-05-05" ];
   var options = dropDown.selectAll("option")
           .data(dataDates)
         .enter()
           .append("option");
   options.text(function (d) { return d; })
      .attr("value", function (d) { return d; });

     x.domain(d3.extent(dataset, function(d) { return d.TimeStamp; }));
     y.domain(d3.extent(dataset, function(d) { return d.Temperature; }));

   svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);


   svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("class","tmp-text")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Temperature");

  svg.append("path")
      .datum(dataset)
      .attr("class", "line")
      .attr("d", line);

});


function updateChart(ds) {
  d3.csv("BMSOne.csv", function(error, data) {


  dataset = data.filter(function (d){
    return d.VarDate === "2015-05-01";
  });

   dataset.forEach(function(d) {
      d.TimeStamp = +parseTime(d.TimeStamp);
      d.Temperature = +d.Temperature;
      d.RelateiveHumidity  = +d.RelateiveHumidity ;
      d.COtwo = +d.COtwo;
      d.SensibleHeat = d.SensibleHeat;
      d.VarDate = d.VarDate;
   });

  var line;
  if (ds === "Temperature") {
    x.domain(d3.extent(dataset, function(d) { return d.TimeStamp; }));
    y.domain(d3.extent(dataset, function(d) { return d.Temperature; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStamp); })
        .y(function(d) { return y(d.Temperature); });
  }
  else if (ds === "COtwo") {
    x.domain(d3.extent(dataset, function(d) { return d.TimeStamp; }));
    y.domain(d3.extent(dataset, function(d) { return d.COtwo; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStamp); })
        .y(function(d) { return y(d.COtwo); });
  }
  else if (ds === "SensibleHeat") {
    x.domain(d3.extent(dataset, function(d) { return d.TimeStamp; }));
    y.domain(d3.extent(dataset, function(d) { return d.SensibleHeat; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStamp); })
        .y(function(d) { return y(d.COtwo); });
  }
  else {
    x.domain(d3.extent(dataset, function(d) { return d.TimeStamp; }));
    y.domain(d3.extent(dataset, function(d) { return d.RelateiveHumidity ; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStamp); })
        .y(function(d) { return y(d.RelateiveHumidity ); });
  }


// Select the section we want to apply our changes to
 var svg = d3.select("body").transition();

 // Make the changes
     svg.select(".line")   // change the line
         .duration(750)
         .attr("d", line);
     svg.select(".y.axis") // change the y axis
         .duration(750)
         .call(yAxis);
      svg.select(".tmp-text")
        .duration(750)
        .text(ds);
});
}

function temperatureB1() {
  updateChart("Temperature");
}

function cotwoB1() {
  updateChart("COtwo");
}

function relhumB1 () {
  updateChart("RelateiveHumidity");
}

function senheatB1() {
  updateChart("SensibleHeat");
}



function temperatureB2() {
  updateChart("Temperature");
}

function cotwoB2() {
  updateChart("COtwo");
}

function relhumB2 () {
  updateChart("RelateiveHumidity");
}


function senheatB2() {
  updateChart("SensibleHeat");
}
