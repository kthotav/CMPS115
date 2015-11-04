// document.write('<button id="Population" class="Button" onclick="population();">Population</button>');
document.write('<a id="temperature" class="col s4 waves-effect waves-light btn" onclick="temperature()">Temperature</a>');
document.write('<a id="pac" class="col s4 waves-effect waves-light btn" onclick="pac()">Pac</a>');
document.write('<a id="vac" class="col s4 waves-effect waves-light btn" onclick="vac()">Vac</a>');

var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var parseTime = d3.time.format("%H:%M").parse;

var x = d3.time.scale().range([0, width]);

var y = d3.scale.linear().range([height, 0]);

var xAxis = d3.svg.axis().scale(x).orient("bottom");

var yAxis = d3.svg.axis().scale(y).orient("left");


var svg = d3.select("body").append("svg")
   .attr("width", width + margin.left + margin.right)
   .attr("height", height + margin.top + margin.bottom)
   .append("g")
   .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv("data.csv", function(error, data) {

   data.forEach(function(d) {
      d.TimeStep = +parseTime(d.TimeStep);
      d.Temperature = +d.Temperature;
      d.Vac = +d.Vac;
      d.Pac = +d.Pac;
      // console.log(d.Temperature); DEBUG
   });

     x.domain(d3.extent(data, function(d) { return d.TimeStep; }));
     y.domain(d3.extent(data, function(d) { return d.Temperature; }));

     var line = d3.svg.line()
       .interpolate("basis")
       .x(function(d) { return x(d.TimeStep); })
       .y(function(d) { return y(d.Temperature); });

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
      .datum(data)
      .attr("class", "line")
      .attr("d", line);

});


function updateChart(ds) {
  d3.csv("data.csv", function(error, data) {

     data.forEach(function(d) {
        d.TimeStep = +parseTime(d.TimeStep);
        d.Temperature = +d.Temperature;
        d.Vac = +d.Vac;
        d.Pac = +d.Pac;
        console.log(d.Vac);
     });
  var line;
  if (ds === "Temperature") {
    x.domain(d3.extent(data, function(d) { return d.TimeStep; }));
    y.domain(d3.extent(data, function(d) { return d.Temperature; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStep); })
        .y(function(d) { return y(d.Temperature); });
  }
  else if (ds === "Pac") {
    x.domain(d3.extent(data, function(d) { return d.TimeStep; }));
    y.domain(d3.extent(data, function(d) { return d.Pac; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStep); })
        .y(function(d) { return y(d.Pac); });
  }
  else {
    x.domain(d3.extent(data, function(d) { return d.TimeStep; }));
    y.domain(d3.extent(data, function(d) { return d.Vac; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStep); })
        .y(function(d) { return y(d.Vac); });
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

function temperature(){
  updateChart("Temperature");
}

function pac() {
  updateChart("Pac");
}

function vac() {
  updateChart("Vac");
}
