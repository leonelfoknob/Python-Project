<?php
    // Connect to MySQL
    include("connect.php");

    // Prepare the SQL statement
      date_default_timezone_set('Europe/Athens');
     $dateS = date('m/d/Y h:i:s', time());
    echo $dateS;
    $SQL = "INSERT INTO yourdatabasename.data (date,temperature,pressure,altitude,ReadSealevelPressure,Real_altitude) VALUES (".$_GET["temperature"]."','".$_GET["pressure"]."','".$_GET["altitude"]."','".$_GET["ReadSealevelPressure"]."','".$_GET["Real_altitude"]."')";     

    // Execute SQL statement
    mysql_query($SQL);

    // Go to the review_data.php (optional)
    header("Location: index.php");
?>