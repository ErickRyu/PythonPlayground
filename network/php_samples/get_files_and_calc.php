
<?php
#sending binary file,json file to php server

$name  = $_POST['json'];
$file_name = $_FILES['rawHexBPfile']['name'];
$file_tmp = $_FILES['rawHexBPfile']['tmp_name'];

file_put_contents('./calc_score/Data/train_condition.json', $name);
move_uploaded_file($file_tmp,'./calc_score/Data/'.$file_name);


# Run python
chdir("./calc_score");
shell_exec('python3.6 ./BP_score.py');

#sending result.json to ios

$contents = file_get_contents("./Data/result.json");

$array = json_decode($contents, true);
$result = json_encode($array, true);

print_r($result);

?>


