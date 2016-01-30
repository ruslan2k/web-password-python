<?php

/**
 * http://stackoverflow.com/questions/18398489/laravel-performing-some-task-on-every-insert-update-when-using-query-builder-or
 */

namespace App;

use App\Library\CryptoLib;

use Illuminate\Foundation\Auth\User as Authenticatable;

class User extends Authenticatable
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'email', 'password',
    ];

    /**
     * The attributes excluded from the model's JSON form.
     *
     * @var array
     */
    protected $hidden = [
        'password', 'salt', 'remember_token',
    ];

    /**
     *
     */
    public static function boot ()
    {
        parent::boot();

        User::creating (function ($user) {
            $user->salt = CryptoLib::genSaltBase64();
        });
    }

    /**
     * Get all of the resources for the user.
     */
    public function resources()
    {
        return $this->hasMany(Resource::class);
    }
}
