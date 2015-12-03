// define margin to display the graph within the SVG
var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

// date formater.
var parseTime = d3.time.format("%H:%M").parse;

// define x and y scales
var x = d3.time.scale().range([0, width]);

var y = d3.scale.linear().range([height, 0]);

// define x and y axes
var xAxis = d3.svg.axis().scale(x).orient("bottom");

var yAxis = d3.svg.axis().scale(y).orient("left");

// define the line being plotted
var line = d3.svg.line()
  .interpolate("basis")
  .x(function(d) { return x(d.TimeStep); })
  .y(function(d) { return y(d.Temperature); });

// define the SVG, where the graph will be drawn onto
var svg = d3.select("body").append("svg")
   .attr("width", width + margin.left + margin.right)
   .attr("height", height + margin.top + margin.bottom)
   .append("g")
   .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


// load the data file
d3.csv("dataC.csv", function(error, data) {

  dataset = data.filter(function (d){
    return d.VarDate === "2015-05-01";
  });

    // read and parse the values as int
   dataset.forEach(function(d) {
      d.TimeStep = +parseTime(d.TimeStep);
      d.Temperature = +d.Temperature;
      d.Vac = +d.Vac;
      d.Pac = +d.Pac;
      d.VarDate = d.VarDate;
   });


   // determine domain (input) values
     x.domain(d3.extent(dataset, function(d) { return d.TimeStep; }));
     y.domain(d3.extent(dataset, function(d) { return d.Temperature; }));


   // draw/append the x-axis
   svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);


   // draw/append the y-axis and label the axis
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

  // draw/append the line
  svg.append("path")
      .datum(dataset)
      .attr("class", "line")
      .attr("d", line);

});


function updateChart(ds) {
  d3.csv("dataC.csv", function(error, data) {

  // fileter data based on date.
  dataset = data.filter(function (d){
    return d.VarDate === "2015-05-01";
  });

    // read and parse the values as int
   dataset.forEach(function(d) {
      d.TimeStep = +parseTime(d.TimeStep);
      d.Temperature = +d.Temperature;
      d.Vac = +d.Vac;
      d.Pac = +d.Pac;
      d.VarDate = d.VarDate;
   });

   // determine which attribute was passed in and what the input(domain) values are
  var line;
  if (ds === "Temperature") {
    x.domain(d3.extent(dataset, function(d) { return d.TimeStep; }));
    y.domain(d3.extent(dataset, function(d) { return d.Temperature; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStep); })
        .y(function(d) { return y(d.Temperature); });
  }
  else if (ds === "Pac") {
    x.domain(d3.extent(dataset, function(d) { return d.TimeStep; }));
    y.domain(d3.extent(dataset, function(d) { return d.Pac; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStep); })
        .y(function(d) { return y(d.Pac); });
  }
  else {
    x.domain(d3.extent(dataset, function(d) { return d.TimeStep; }));
    y.domain(d3.extent(dataset, function(d) { return d.Vac; }));

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

function temperature() {
  updateChart("Temperature");
}

function pac() {
  updateChart("Pac");
}

function vac() {
  updateChart("Vac");
}
