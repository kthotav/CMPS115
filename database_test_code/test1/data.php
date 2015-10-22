<!-- <?php
   $dbhost = 'localhost';
   $dbuser = 'root';
   $dbpass = "root";
   $db = "mysql";

   $conn = mysql_connect($dbhost, $dbuser, $dbpass);
   mysql_select_db($db);


   $query = "SELECT * FROM data1";

   $result = mysql_query($query);

   while($person = mysql_fetch_array($result)) {
      echo "<h2>" . $person['TimeStep'] . "</h2>";
      echo "<p>" .  $person['Temperature'] . "</p>";
   }


?> -->

<?php
    $username = "root";
    $password = "root";
    $host = "localhost";
    $database="mysql";

    $server = mysql_connect($host, $username, $password);
    $connection = mysql_select_db($database, $server);

    $myquery = "SELECT  *  FROM  data1";
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

    mysql_close($server);
?>
