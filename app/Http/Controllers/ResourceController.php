<?php

namespace App\Http\Controllers;

use App\Resource;
use App\Http\Requests;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use App\Repositories\ResourceRepository;


class ResourceController extends Controller
{
    /**
     * The resources repository instance.
     *
     * @var ResourceRepository
     *
     */
    protected $resources;

    /**
     * Create a new controller instance.
     *
     * @param ResourceRepository $resources
     * @return void
     */
    public function __construct (ResourceRepository $resources)
    {
        $this->middleware('auth');

        $this->resources = $resources;
    }

    public function index (Request $request)
    {
        //$resources = Resource::all();
        $resources = Resource::where('user_id', $request->user()->id)->get();

        return view('resource.index', [
            'resources' => $resources,
        ]);
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
