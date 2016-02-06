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
        //return dump($request->user());
        //return dump($request->session());
        return view('resource.index', [
            'resources' => $this->resources->forUser($request->user()),
        ]);
    }

    public function show (Resource $resource)
    {
        return view('resource.show', ['resource' => $resource]);
    }

    /**
     * Create a new resource
     *
     * @param Request $request
     * @return Response
     */
    public function store (Request $request)
    {
        //$this->validate();

        $request->user()->resources()->create([
            'name' => $request->name,
        ]);

        return redirect()->route('resource.index');
    }

    public function destroy (Resource $resource)
    {
        $resource->delete();
        return redirect('/resource');   
    }

    public function test (Request $request)
    {
        dump($request->session()->get('sym_pass'));
    }
}
