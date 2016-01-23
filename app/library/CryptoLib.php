<?php

/**
 * https://laracasts.com/discuss/channels/general-discussion/l5-how-to-add-custom-php-classes-in-l5
 */

namespace App\library;


define("DEF_ITERATIONS", 1000);

class CryptoLib
{
    /**
     *
     */
    public static function genSaltBin ()
    {
        return mcrypt_create_iv(16, MCRYPT_DEV_URANDOM);
    }

    /**
     *
     */
    public static function genSaltBase64 ()
    {
        return base64_encode(self::genSaltBin());
    }

    /**
     * Generate Symetric-key from Password and Salt
     */
    public static function genSymKey ($password, $salt)
    {
        return hash_pbkdf2("sha256", $password, $salt, DEF_ITERATIONS, 20);
    }

}
