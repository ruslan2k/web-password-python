<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

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


    public function store (Request $request)
    {
        $item = R::dispense('item');
        $item->name = $request->input('name');
        $id = R::store($item);
        return redirect()->route('item.show', ['id' => $id]);
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
