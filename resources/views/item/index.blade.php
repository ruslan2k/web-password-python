@extends('layouts.master')

@section('content')

<p>Index</p>

@forelse ($tables as $table)
<a href="/{{ $table['name'] }}">{{ $table['name'] }}</a>
@empty
<p>No tables</p>
@endforelse

@forelse ($items as $item)
  <li>
    id: {{ $item['id'] }}
    <a href="/item/{{ $item['id'] }}">name: {{ $item->name }}</a>
    <a data-id="{{ $item['id'] }}" class="del" href="#">[x]</a>
  </li>
@empty
<p>No items</p>
@endforelse

@endsection
