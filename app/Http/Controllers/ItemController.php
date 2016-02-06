<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Item;
use App\Http\Requests;
use App\Http\Controllers\Controller;

use RedBeanPHP\Facade as R;

class ItemController extends Controller
{
    public function index ()
    {
        $items = R::findAll('item');
        $tables = R::getAll('SELECT name FROM sqlite_master WHERE type = "table"');
        return view('item.index', ['items' => $items, 'tables' => $tables]);
    }

    public function create ()
    {
        return view('item.create');
    }


    public function show ($id)
    {
        $item = R::load('item', $id);
        return view('item.show',
            ['item' => $item, 'attributes' => $item->ownAttributeList]);
    }


    public function store_RedBean (Request $request)
    {
        $item = R::dispense('item');
        $item->name = $request->input('name');
        $id = R::store($item);
        return redirect()->route('item.show', ['id' => $id]);
    }

    public function store (Request $request)
    {
        $item = new Item;
        $item->setSymPass($request->session()->get('sym_pass'));
        $item->key = $request->key;
        $item->value = $request->value;
        $item->resource_id = $request->resource_id; 
        $item->save(); 
        return redirect()->route('resource.show',
            ['id' => $request->resource_id]);
    }

    /**
     * Update the specified item.
     *
     * @param  Request  $request
     * @param  string  $id
     * @return Response
     */
    public function update (Request $request, $id)
    {
        //
    }

    /**
     * Destroy
     */
    public function destroy (Request $request, $id)
    {
        $item = R::load('item', $id);
        R::trash($item);
    }


}
