var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var parseTime = d3.time.format("%H:%M").parse;

var x = d3.time.scale().range([0, width]);

var y = d3.scale.linear().range([height, 0]);

var xAxis = d3.svg.axis().scale(x).orient("bottom");

var yAxis = d3.svg.axis().scale(y).orient("left");

var line = d3.svg.line()
   .x(function(d) { return x(d.TimeStep); })
   .y(function(d) { return y(d.Temperature); });

var svg = d3.select("body").append("svg")
   .attr("width", width + margin.left + margin.right)
   .attr("height", height + margin.top + margin.bottom)
   .append("g")
   .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


d3.json("data.json", function(error, data) {

   data.forEach(function(d) {
      d.TimeStep = +parseTime(d.TimeStep);
      d.Temperature = +d.Temperature;
      // console.log(d.Temperature); DEBUG
   });

   x.domain(d3.extent(data, function(d) { return d.TimeStep; }));
   y.domain(d3.extent(data, function(d) { return d.Temperature; }));


   svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

   svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Temperature");

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);

});
