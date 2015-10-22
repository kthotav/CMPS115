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

// sql to create table
$sql = "CREATE TABLE pv_data (
timestep VARCHAR(30),
temp VARCHAR(30)
)";

if (mysqli_query($conn, $sql)) {
    echo "Table pv_data created successfully";
} else {
    echo "Error creating table: " . mysqli_error($conn);
}

mysqli_close($conn);
?>
