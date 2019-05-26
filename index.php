<?php

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=utf-8');

exec('./shock.py');
echo json_encode([ 'status' => 'OK' ]);