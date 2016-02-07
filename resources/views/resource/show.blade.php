@extends('layouts.app')

@section('content')
<h2>
  {{ $resource->name }}
</h2>
<ul>
@forelse ($resource->items as $item)
  <li>
    {{ $item->key }}: <input class="secret" value="{{ $item->val }}"/>
  </li>
@empty
@endforelse
</ul>

{!! Form::open(['method' => 'post', 'url' => 'item']) !!}
{!! Form::label('key', 'Key') !!}
{!! Form::text('key') !!}
{!! Form::label('val', 'Value') !!}
{!! Form::text('val') !!}
{!! Form::hidden('resource_id', $resource->id) !!}
{!! Form::submit('Add') !!}
{!! Form::close() !!}
@endsection
