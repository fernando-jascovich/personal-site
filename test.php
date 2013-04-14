<?php

	//define('SITE_ROOT', 'http://localhost/personal-site/');
	define('SITE_ROOT', 'http://www.fernandojascovich.com.ar/test/');

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