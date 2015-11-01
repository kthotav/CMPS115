<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "dbPV";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// sql to create table
$sql = "CREATE TABLE pv (
timeStep VARCHAR(30) NOT NULL,
pac VARCHAR(30) NOT NULL,
temperature VARCHAR(30) NOT NULL,
vac VARCHAR(30) NOT NULL,
var_date VARCHAR(30) NOT NULL
)";

include 'pv-data.php';
// if (mysqli_query($conn, $sql)) {
//     echo "Table created successfully";
// } else {
//     echo "Error creating table: " . mysqli_error($conn);
// }

mysqli_close($conn);
?>
<!DOCTYPE html>
<meta charset='utf-8'>
<title>D3JS PHP MySQLP</title>
<head>
<link rel='stylesheet' type='text/css' href='style.css'>
<link rel='stylesheet' type='text/css' href='materialize/css/materialize.min.css'>
<script type='text/javascript' src='jquery.min.js'></script>
</head>
<body>


<script type='text/javascript' src='d3/d3.min.js'></script>
<script type='text/javascript' src='graph.js'></script>
<script type='text/javascript' src='materialize/js/materialize.min.js'></script>
<!-- <a class="waves-effect waves-light btn">Temperature</a> -->
</body>
<script>
$(document).ready(function() {
    $('select').material_select();
  });

$('.datepicker').pickadate({
  selectMonths: true, // Creates a dropdown to control month
  selectYears: 15 // Creates a dropdown of 15 years to control year
});


</script>

</html>
