#!/bin/bash
# Makes request that causes the server to responsd with a message in the body
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me