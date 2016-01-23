<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Resource extends Model
{
//    /**
//     * The attributes that are mass assignable.
//     *
//     * @var array
//     */
//    protected $fillable = [
//        'name', 'email', 'password',
//    ];
//
//    /**
//     * The attributes excluded from the model's JSON form.
//     *
//     * @var array
//     */
//    protected $hidden = [
//        'password', 'salt', 'remember_token',
//    ];

    public function items ()
    {
        return $this->hasMany('App\Item');
    }


}
