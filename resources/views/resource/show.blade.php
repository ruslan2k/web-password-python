@extends('layouts.app')

@section('content')
<p>Resource Show</p>
<h2>
  {{ $resource->name }}
</h2>
  {{ dump($resource->items) }}
  <li>
  </li>
{!! Form::open(['method' => 'post', 'url' => 'item']) !!}
{!! Form::label('key', 'Key') !!}
{!! Form::text('key') !!}
{!! Form::label('value', 'Value') !!}
{!! Form::text('value') !!}
{!! Form::hidden('resource_id', $resource->id) !!}
{!! Form::submit('Add') !!}
{!! Form::close() !!}
@endsection
