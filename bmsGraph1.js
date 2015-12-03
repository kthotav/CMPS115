
// define margin so that the graphs is displayed within the SVG
var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

// parse time function
var parseTime = d3.time.format("%H:%M").parse;

// define x and y scales
var x = d3.time.scale().range([0, width]);

var y = d3.scale.linear().range([height, 0]);

// define x and y axis
var xAxis = d3.svg.axis().scale(x).orient("bottom");

var yAxis = d3.svg.axis().scale(y).orient("left");

// define the line being drawn
var line = d3.svg.line()
  .interpolate("basis")
  .x(function(d) { return x(d.TimeStamp); })
  .y(function(d) { return y(d.Temperature); });

// define svg, this is where the graph is being drawn onto
var svg = d3.select("body").append("svg")
   .attr("width", width + margin.left + margin.right)
   .attr("height", height + margin.top + margin.bottom)
   .append("g")
   .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// import the data file
d3.csv("BMSOne.csv", function(error, data) {

  dataset = data.filter(function (d){
    return d.VarDate === "7-29-2015";
  });

// parse the values as type int
   dataset.forEach(function(d) {
      d.TimeStamp = +parseTime(d.TimeStamp);
      d.Temperature = +d.Temperature;
      d.RelativeHumidity = +d.RelativeHumidity;
      d.COtwo = +d.COtwo;
      d.SensibleHeat = d.SensibleHeat;
      d.VarDate = d.VarDate;
   });


    // set the domain of x and y values
     x.domain(d3.extent(dataset, function(d) { return d.TimeStamp; }));
     y.domain(d3.extent(dataset, function(d) { return d.Temperature; }));

     // draw/append the x-axis
   svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

    // draw/apend the y-axis
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

      // draw the line
  svg.append("path")
      .datum(dataset)
      .attr("class", "line")
      .attr("d", line);

});


function updateChart(ds, file) {
  console.log(file);
  // import the data file
  d3.csv(file, function(error, data) {


  dataset = data.filter(function (d){
    return d.VarDate === "7-29-2015";
  });

  // parse the values as type int
   dataset.forEach(function(d) {
      d.TimeStamp = +parseTime(d.TimeStamp);
      d.Temperature = +d.Temperature;
      d.RelativeHumidity = +d.RelativeHumidity ;
      d.COtwo = +d.COtwo;
      d.SensibleHeat = d.SensibleHeat;
      d.VarDate = d.VarDate;
   });

  var line;
   // determine which attribute was passed in and what the input(domain) values are
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
    y.domain(d3.extent(dataset, function(d) { return d.RelativeHumidity ; }));

    line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.TimeStamp); })
        .y(function(d) { return y(d.RelativeHumidity ); });
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

// Update room 1
function temperatureB1() {
  updateChart("Temperature", "BMSOne.csv");
}

function cotwoB1() {
  updateChart("COtwo", "BMSOne.csv");
}

function relhumB1 () {
  updateChart("RelativeHumidity", "BMSOne.csv");
}

function senheatB1() {
  updateChart("SensibleHeat", "BMSOne.csv");
}




// Update room 2
function temperatureB2() {
  updateChart("Temperature", "BMSTwo.csv");
}

function cotwoB2() {
  updateChart("COtwo", "BMSTwo.csv");
}

function relhumB2 () {
  updateChart("RelativeHumidity", "BMSTwo.csv");
}


function senheatB2() {
  updateChart("SensibleHeat", "BMSTwo.csv");
}
