<?php

namespace App;

use App\Library\CryptoLib;
use Illuminate\Database\Eloquent\Model;

define('DEF_METHOD', 'AES-256-CBC');

class Item extends Model
{
    /**
     * Symetryc pass for encrypt value
     *
     * @var string
     */
    private $sym_pass;

    /**
     * Add hook for model
     *
     * @return void
     */
    public static function boot ()
    {
        parent::boot();

        Item::creating(function ($item) {
            if ( ! isset($item->sym_pass)) {
                return false;
            }
            $bin_iv = random_bytes(16); 
            $val = openssl_encrypt(serialize($item->val), DEF_METHOD, $item->sym_pass, 0, $bin_iv);
            $item->val = $val;
            $item->iv = base64_encode($bin_iv);
        });
    }

    public function getDecryptedValue ()
    {
        if ( ! isset($this->sym_pass)) {
            return false;
        }
        $bin_iv = base64_decode($this->iv);
        $val = openssl_decrypt($this->val, DEF_METHOD, $this->sym_pass, 0, $bin_iv);
        return unserialize($val);
    }

    /**
     * Set Symetric pass for encrypt values
     *
     * @param string $sym_pass
     */
    public function setSymPass ($sym_pass)
    {
        $this->sym_pass = $sym_pass;
    }
}
