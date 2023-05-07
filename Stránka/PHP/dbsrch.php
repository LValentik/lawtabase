<?php
$law = $_POST['lawtype'];
$legislative = $_POST['legislative'];
$search_parag = $_POST['search_parag'];
$search_law = $_POST['search_law'];
$dbname = 'Lawtabase';
$dbuser = 'postgres';
$dbpass = 'VaL123eNt456Ik789.';
$dbhost = 'localhost';
$dbport = '5432';

$conn = pg_connect("host=$dbhost port=$dbport dbname=$dbname user=$dbuser password=$dbpass");
if(!$search_parag){
    $sql = "SELECT * FROM $legislative.$law WHERE law LIKE '%$search_law%'";
}
else {
    $sql = "SELECT * FROM $legislative.$law WHERE paragraph_num = '$search_parag' OR law LIKE '%$search_law'";
}

$result = pg_query($conn, $sql);

if (!$result) {
    echo "An error occurred.\n";
    exit;
}

echo "<table>\n";
while ($row = pg_fetch_assoc($result)) {
    echo "<tr border>";
    echo "<td>" . $row['paragraph_num'] . "</td>";
    echo "<td>" . $row['law'] . "</td>";
    echo "</tr>\n";
}
echo "</table>\n";

pg_free_result($result);
pg_close($conn);
?>
