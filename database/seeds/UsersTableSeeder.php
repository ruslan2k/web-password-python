<?php

use Illuminate\Database\Seeder;

use App\User;

class UserTableSeeder extends Seeder
{
    public function run ()
    {
        DB::table('users')->delete();
        User::create([
            // 'id' => 11,
            'name' => 'ruslan',
            'email' => 'ruslan2k@mail.ru',
            'password' => '********',
            'salt' => '**********',
            'created_at' => '2016-01-10 17:00:10',
            'updated_at' => '2016-01-10 17:00:10',
        ]);
    }
}
