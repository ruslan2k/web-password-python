<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Resource;
use App\Http\Requests;
use App\Http\Controllers\Controller;

class ResourceController extends Controller
{

    public function index ()
    {
        $resources = Resource::all();

        //return dump($resources);
        return view('resource.index', ['resources' => $resources]);
    }

    public function show (Resource $resource)
    {
        return view('resource.show', ['resource' => $resource]);
    }

    public function store (Request $request)
    {
        $resource = new Resource;
        $resource->name = $request->name;
        $resource->save();
        //return redirect()->route('resource.index', ['id' => $id]);
        return redirect()->route('resource.index');
    }

    public function destroy (Resource $resource)
    {
        $resource->delete();
        return redirect('/resource');   
    }
}
