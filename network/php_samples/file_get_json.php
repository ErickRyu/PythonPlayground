<?php
#sending binary file,json file to php server

#$name  = $_POST['data'];
$name = file_get_contents("php://input");

file_put_contents("./train_condition.json", $name);

#$file_name = $_FILES['rawHexBPfile']['name'];
#$file_tmp = $_FILES['rawHexBPfile']['tmp_name'];

#move_uploaded_file($file_tmp,'./'.$file_name);


#sending result.json to ios
#$contents = file_get_contents("./train_condition.json");

$array = json_decode($contents, true);
$result = json_encode($array, true);

print_r($name);

?>
