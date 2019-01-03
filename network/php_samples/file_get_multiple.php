<?php

#$data = file_get_contents("php://input");

$name  = $_POST['json'];

$file_name = $_FILES['rawHexBPfile']['name'];
$file_tmp = $_FILES['rawHexBPfile']['tmp_name'];

file_put_contents("./train_condition.json", $name);
$uploaddir = './';
$uploadfile = $uploaddir . basename($file_name);
move_uploaded_file($file_tmp, $uploadfile);

print_r($name);

?>
