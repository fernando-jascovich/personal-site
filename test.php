<?php

	define('SITE_ROOT', 'http://www.fernandojascovich.com.ar');

	//$service_url = SITE_ROOT . '/cgi-bin/test.py';
	$service_url = 'cgi-bin/test.py';
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

	var_dump($response);

?>