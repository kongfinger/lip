<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "lipservice";

// open csv file
$file = fopen("c:\\\\lip\\smine.csv","r");
print_r(fgetcsv($file));
fclose($file);

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

//$sql = "INSERT INTO MyGuests (firstname, lastname, email)
//VALUES ('John', 'Doe', 'john@example.com')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
