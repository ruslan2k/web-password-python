<?php

namespace App\Http\Middleware;

use Closure;
use Monolog\Logger;

class AfterLoginMiddleware
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        //$log = new Logger('test');
        //$log->addError('test', [$request->password]);
        $response = $next($request);

        $request->session()->put('answer', '42');

        return $response;
    }
}
