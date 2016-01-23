<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Attribute;
use App\Http\Requests;
use App\Http\Controllers\Controller;

class AttributeController extends Controller
{
    public function store (Request $request)
    {
        $attribute = new Attribute;
        dump($request); 
        $attribute->key = $request->key; 
        $attribute->value = $request->value; 
        $attribute->resource_id = $request->resource_id; 
        dump($attribute); 
        $attribute->save(); 
    } 
}
