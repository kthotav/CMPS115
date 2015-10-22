<?php
$servername = "localhost";
$username = "root";
$password = "SoccerNike19";
$dbname = "pvDB";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
print("Plese fuvekj orprpruhnt");

$sql = "INSERT INTO pv_data VALUES "; //(timestep, temp) VALUES ";
//print($sql);

if (file_exists('data.csv')) { 
    print("Im so in this shit: <br \> \n");
    //get the csv file 
    $file = 'data.csv'; 
    $handle = fopen($file,"r"); 
     
    //loop through the csv file and insert into database 
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $sql .= "('" . $data[0] . "', '" . $data[1] . "'), ";
    }
    $sql = trim($sql);
    $sql = trim($sql, ",");
    //print_r($sql);
    fclose($handle);
} 

if (mysqli_query($conn, $sql)) {
    echo "New records created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);
?>
