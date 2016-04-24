<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::group(['middleware' => ['web']], function () {
    //
});

Route::group(['middleware' => ['web']], function () {
    Route::auth(['middleware' => 'after_login']);

    Route::get('/home', 'HomeController@index');
    Route::get('/test', 'ResourceController@test');
    Route::resource('resource', 'ResourceController');
    Route::resource('item', 'ItemController');
});

//Route::resource('test', 'TestController');
//Route::resource('{model}', 'TestController');
