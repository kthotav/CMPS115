<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "test1";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// sql to create table
$sql = "CREATE TABLE data2 (
TimeStep VARCHAR(30) NOT NULL,
Temperature VARCHAR(30) NOT NULL
)";

if (mysqli_query($conn, $sql)) {
    echo "Table data2 created successfully";
} else {
    echo "Error creating table: " . mysqli_error($conn);
}

$sql = "INSERT INTO data2 VALUES "; //(timestep, temp) VALUES ";
//print($sql);
if (file_exists('datatest.csv')) {
    print("Im so in this shit: <br \> \n");
    //get the csv file
    $file = 'datatest.csv';
    $handle = fopen($file,"r");

    //loop through the csv file and insert into database
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $sql .= "('" . $data[0] . "', '" . $data[1] . "'), ";
    }
    $sql = trim($sql);
    $sql = trim($sql, ",");
    print_r($sql);
}
if (mysqli_query($conn, $sql)) {
    echo "New records created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

include 'data.php';


fclose($file);
echo "File data successfully imported to database!!";

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
   <div class="row">
         <div class="input-field col s3 m3 l3">
       <select>
         <option value="" disabled selected>Choose your option</option>
         <option value="1">Option 1</option>
         <option value="2">Option 2</option>
         <option value="3">Option 3</option>
       </select>
       <label>Atrribute Select</label>
     </div>

     <div class="input-field col s3 m3 l3">
   <select>
    <option value="" disabled selected>Choose your option</option>
    <option value="1">Option 1</option>
    <option value="2">Option 2</option>
    <option value="3">Option 3</option>
   </select>
   <label>Atrribute Select</label>
   </div>
   <div class='col s3 m3 l3'>
      <label>Date picker</label>
   <input type="date" class="datepicker">

</div>

   </div>

<script type='text/javascript' src='d3/d3.min.js'></script>
<script type='text/javascript' src='graph.js'></script>
<script type='text/javascript' src='materialize/js/materialize.min.js'></script>

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
