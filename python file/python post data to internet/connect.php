<?php
$MyUsername = "yourDatabaseUsername";  // enter your username for mysql
$MyPassword = "yourFatabasePassword";  // enter your password for mysql
$MyHostname = "localhost";      // this is usually "localhost" unless your database resides on a different server

$dbh = mysql_pconnect($MyHostname , $MyUsername, $MyPassword);
$selected = mysql_select_db("yourDatabaseName",$dbh); //Enter your database name here 
?>