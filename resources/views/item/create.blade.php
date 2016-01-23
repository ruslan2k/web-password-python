@extends('layouts.master')

@section('content')

<p>Create</p>

<form action="/item" method="post">
  <input type="text" name="name">
  <input type="submit" value="Submit">
</form>

@endsection
