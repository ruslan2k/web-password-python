<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests;
use App\Http\Controllers\Controller;

use RedBeanPHP\Facade as R;

class TestController extends Controller
{

    public function index (Request $request, $model)
    {
        $beans = R::findAll($model);
        $records = R::exportAll($beans, true);
        $tables = R::getAll(
            'SELECT name FROM sqlite_master WHERE type = "table"');
        return view('umodel.index',
            ['records' => $records, 'tables' => $tables]);
    }

    public function create (Request $request, $model)
    {
        $model_name = $model;
        $record = R::dispense($model_name);
        $id = R::store($record);
        $record  = R::load($model, $id);
        $columns = $record->export();
        R::trash($record);
        $uri = $request->path();
        echo "<pre>\n";
        echo "Create Uri: $uri\n"
            . "Model: $model\n";
        var_dump($columns);
        echo "</pre>";
    }

    /**
     * Store a new record.
     *
     * @param  Request  $request
     * @return Response
     */
    public function store (Request $request)
    {
        $item_id = $request->input('item_id');
        $item = R::load('item', $item_id);
        $attribute = R::dispense('attribute');
        $attribute->key   = $request->input('key');
        $attribute->value = $request->input('value');
        $item->ownAttributeList[] = $attribute;
        R::store($item);
        echo "<pre>\n";
        var_dump($attribute->export());
        var_dump($item->export());
    }

}
