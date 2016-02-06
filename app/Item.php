<?php

namespace App;

use App\Library\CryptoLib;
use Illuminate\Database\Eloquent\Model;

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
            $iv = random_bytes(16); 
            $value = openssl_encrypt($item->value, 'AES-256-CBC', $item->sym_pass, 0, $iv);
            $item->value = $value;
        });
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
