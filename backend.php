<?php

    require_once('config.php');

    function check_post_var($post_var)
    {
        $return_val = false;

        if(isset($post_var) && trim($post_var) != '' && trim($post_var) != '0' && trim($post_var) != 'false')
            $return_val = trim($post_var);

        return $return_val;
    }

    $post_fields = (check_post_var($_POST['token']) || check_post_var($_POST['useremail']) ) ? http_build_query($_POST) : '';

    $service_url = SITE_ROOT . 'cgi-bin/backend.py';
    $headers = array(
                    'Accept: application/json'
                );
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $service_url);
    curl_setopt($ch, CURLOPT_TIMEOUT, 30);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post_fields);

    $response = curl_exec($ch);

    curl_close($ch);

    print_r($response);

?>