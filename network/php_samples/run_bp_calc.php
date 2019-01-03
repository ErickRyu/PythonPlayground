<?php

$name  = $_POST['data'];
$file_name = $_FILES['rawHexBPfile']['name'];
$file_tmp = $_FILES['rawHexBPfile']['tmp_name'];

if (empty($name)) {
    echo 'data is empty <br>';
}
else {
    file_put_contents('/var/www/html/testsite/miffle/calc_score/Data/train_condition.json', $name);
    move_uploaded_file($file_tmp,'/var/www/html/testsite/miffle/calc_score/Data/'.$file_name);
}

$cnt_wait = 10;
do {
    if (file_exists("/var/www/html/testsite/miffle/calc_score/Data/train_condition.json")) {
        echo "The file was found: " . date("d-m-Y h:i:s") . "<br>";
        break;
    }
    sleep(1);
    echo "<Error> The file was not found: " . date("d-m-Y h:i:s") . "<br>";
    $cnt_wait = $cnt_wait -1;
} while($cnt_wait > 0);

if (0 == $cnt_wait) {
    # Run python
    chdir("/var/www/html/testsite/miffle/calc_score");
    shell_exec('python3.6 ./BP_score.py');

    #sending result.json to ios
    $contents = file_get_contents("/var/www/html/testsite/miffle/calc_score/Data/result.json");

    $array = json_decode($contents, true);
    $result = json_encode($array, true);
}
else {
    #sending result.json to ios
    $contents = file_get_contents("/var/www/html/testsite/miffle/calc_score/Data/result.json");
    echo 'Timeout error';
}

?>
