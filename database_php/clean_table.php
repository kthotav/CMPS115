<?php
$servername = "localhost";
$username = "root";
$password = "SoccerNike19";
$dbname = "pvDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

// sql to drop table
$sql = "DROP TABLE pv_data";

if ($conn->query($sql) === TRUE) {
    echo "Table pv_data dropped successfully";
} else {
    echo "Error dropping table: " . $conn->error;
}

$conn->close();
?>
