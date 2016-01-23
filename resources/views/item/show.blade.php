@extends('layouts.master')

@section('content')

<p>Show</p>

<h2>{{ $item->name }}</h2>

@forelse ($attributes as $attribute)
  <li>
    key: {{ $attribute['key'] }}
    value: {{ $attribute['value'] }}
  </li>
@empty

@endforelse

<p>
  <form action="/test" method="post">
    item_id: <input type="text" name="item_id" value="{{ $item->id }}"><br>
    key: <input type="text" name="key"><br>
    value: <input type="text" name="value"><br>
    <input type="submit" value="Add">
  </form>
</p>

@endsection
