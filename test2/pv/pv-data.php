<?php

    $username = "root";
    $password = "root";
    $host = "localhost";
    $database="dbPV";

    $server = mysql_connect($host, $username, $password);
    $connection = mysql_select_db($database, $server);

    $name =$_GET['name'];
    echo $name;

    $myquery = "SELECT timeStep AS TimeStep, pac AS Pac, temperature AS Temperature, vac as Vac FROM pv WHERE var_date= '10/21/2015' ";
    $query = mysql_query($myquery);

    if ( ! $query ) {
        echo mysql_error();
        die;
    }

    $data = array();

    for ($x = 0; $x < mysql_num_rows($query); $x++) {
        $data[] = mysql_fetch_assoc($query);
    }


    echo json_encode($data);

    $myfile = fopen("data.json", "w") or die("Unable to open file!");
    fwrite($myfile,  json_encode($data));
    fclose($myfile);


    mysql_close($server);
?>
