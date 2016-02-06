<?php

namespace App\Http\Middleware;

use Closure;
use Monolog\Logger;
use App\Library\CryptoLib;

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
        $log = new Logger('test');

        $request->session()->put('answer', '42');
        $sym_pass = CryptoLib::genSymKey($request->password, 'bla');
        $request->session()->put('sym_pass', $sym_pass);

        $log->addError('test1', [$request->password]);
        $log->addError('test2', [$sym_pass]);

        $response = $next($request);
        return $response;
    }
}
