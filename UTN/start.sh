#!/bin/sh
redis-server &
python3 -m flask run --host=0.0.0.0