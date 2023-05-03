<?php

$law = $_POST['lawtype'];
$legislative = $_POST['legislative'];
$search = $_POST['search'];
$dbname = 'Lawtabase';
$dbuser = 'postgres';
$dbpass = 'VaL123eNt456Ik789.';
$dbhost = 'localhost';
$dbport = '5432';

$conn = pg_connect("host=$dbhost port=$dbport dbname=$dbname user=$dbuser password=$dbpass");

$sql = "SELECT * FROM $law.$legislative WHERE law LIKE '%$search%'";
$result = pg_query($conn, $sql);

echo $result;
pg_close($conn);
?>

