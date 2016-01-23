<?php

/**
 * http://php.net/manual/en/function.hash-pbkdf2.php
 */
$password = "password";
$iterations = 1000;

$salt = mcrypt_create_iv(16, MCRYPT_DEV_URANDOM);

$hash = hash_pbkdf2("sha256", $password, $salt, $iterations, 20);

echo $hash;


