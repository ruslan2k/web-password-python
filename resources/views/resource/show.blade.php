@extends('layouts.app')

@section('content')
<p>Resource Show</p>
<h2>
  {{ $resource->name }}
</h2>
  {{ dump($resource->attributes_123) }}
  <li>
  </li>
{!! Form::open(['method' => 'post', 'url' => 'attribute']) !!}
{!! Form::label('key', 'Key') !!}
{!! Form::text('key') !!}
{!! Form::label('value', 'Value') !!}
{!! Form::text('value') !!}
{!! Form::hidden('resource_id', $resource->id) !!}
{!! Form::submit('Add') !!}
{!! Form::close() !!}
@endsection
