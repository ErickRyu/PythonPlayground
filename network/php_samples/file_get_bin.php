<?php

$uploaddir = './';
$filename = $_FILES['rawHexBPfile']['name'];
$uploadfile = $uploaddir . basename($filename);
$file_tmp = $_FILES['rawHexBPfile']['tmp_name'];
move_uploaded_file($file_tmp, $uploadfile);

print_r($filename)

?>
