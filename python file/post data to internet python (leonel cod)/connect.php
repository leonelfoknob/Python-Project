<?php
$MyUsername = "id17256696_leonel";  // enter your username for mysql
$MyPassword = "zjU~mSx5L/xrh*ag";  // enter your password for mysql
$MyHostname = "localhost";      // this is usually "localhost" unless your database resides on a different server

$dbh = mysql_pconnect($MyHostname , $MyUsername, $MyPassword);
$selected = mysql_select_db("id17256696_weater",$dbh); //Enter your database name here 
?>