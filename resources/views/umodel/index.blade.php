<p>Index</p>

@forelse ($tables as $table)
  <a href="/{{ $table['name'] }}">{{ $table['name'] }}</a>
@empty
@endforelse

<ul>
@forelse ($records as $record)
  <li>
    {{ dump($record) }}
  </li>
@empty
<p>No records</p>
@endforelse
</ul>
