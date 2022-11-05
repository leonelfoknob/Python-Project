<?php
$temperature = htmlspecialchars($_GET["temperature"]);
$pressure = htmlspecialchars($_GET["pressure"]);
$altitude = htmlspecialchars($_GET["altitude"]);
$ReadSealevelPressure = htmlspecialchars($_GET["ReadSealevelPressure"]);
$Real_altitude = htmlspecialchars($_GET["Real_altitude"]);

echo "temperature: $temperature pressure: $pressure altitude: $altitude ReadSealevelPressure: $ReadSealevelPressure Real_altitude: $Real_altitude";
?>