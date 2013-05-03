<?php

	require_once('config.php');

	$service_url = SITE_ROOT . 'cgi-bin/main.py';
	$headers = array(
			    	'Accept: application/json'
				);
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $service_url);
	curl_setopt($ch, CURLOPT_TIMEOUT, 30);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

	$response = curl_exec($ch);

	curl_close($ch);

	print_r($response);

?>