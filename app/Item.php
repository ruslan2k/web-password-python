<?php

namespace App;

use App\Library\CryptoLib;
use Illuminate\Database\Eloquent\Model;

class Item extends Model
{
    /**
     * Add hook for model
     *
     * @return void
     */
    public static function boot ()
    {
        parent::boot();

        Item::creating(function ($item) {
            //$item->key = CryptoLib::genSaltBase64();
            $item->key = '[' . $item->key .']';
        });
    }
    //
}
