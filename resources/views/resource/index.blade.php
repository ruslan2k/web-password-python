@extends('layouts.app')

@section('content')
<p>Resource Index</p>
<ul>
@forelse ($resources as $resource)
  <li>
    {{--
    <a href="/resource/{{ $resource->id }}">
      {{ $resource->name }}
    </a>
    --}}
      {{-- dump($resource) --}}
    <form action="/resource/{{ $resource->id }}" method="post">
      <span>
        <a href="/resource/{{ $resource->id }}">
          {{ $resource->name }}
        </a>
      </span>
      {{ csrf_field() }}
      {{ method_field('DELETE') }}
      <button>x</button>
    </form>
  </li>
@empty
  <p>No resources</p>
@endforelse
<ul>
{!! Form::open(['method' => 'post']) !!}
{!! Form::label('name', 'Resource Name') !!}
{!! Form::text('name') !!}
{!! Form::submit('Create') !!}
{!! Form::close() !!}
@endsection
