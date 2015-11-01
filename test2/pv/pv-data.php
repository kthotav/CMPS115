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


    $i=0;
    while($rows=mysql_fetch_array($query))
    {
      $roll[$i]=$rows['var_date'];
      $i++;
    }
    $total_elmt=count($roll);

    ?>

    <form method="POST" action="">
    Select Roll No: <select name="sel">
    <option>Select</option>


    <?php
    for($j=0;$j<$total_elmt;$j++)
    {
    ?><option><?php
    echo $roll[$j];
    ?></option><?php
    }
    ?>


    </select>

    <input name="submit" type="submit" value="Search"/><br />

    </form>



    <?php

    if(isset($_POST['submit']))
    {
    $value=$_POST['sel'];

    $query2 = "SELECT * FROM pv WHERE var_date='$value'";
    $result2=mysql_query($query2) or die("Query Failed : ".mysql_error());
    while($row=mysql_fetch_array($result2))
    {
       echo "Roll No: ".$row['var_date']."<br/>";

    }


        $myfile = fopen("data.json", "w") or die("Unable to open file!");
        fwrite($myfile,  json_encode($data));
        fclose($myfile);

        mysql_close($server);
    // mysql_close($connect_mysql);
    }
    ?>


    <p align=right><a href="index.php">HOME</a></p>

<!--
 <?php


   //  echo json_encode($data);

   //  $myfile = fopen("data.json", "w") or die("Unable to open file!");
   //  fwrite($myfile,  json_encode($data));
   //  fclose($myfile);


    mysql_close($server);
?> -->
