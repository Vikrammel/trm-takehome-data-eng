## Overview

This repo houses an api server used to query direct exposure information relating to cryptocurrency addresses

pre-reqs: install docker-compose (version 3.2 used to write docker-compose.yml)

**1. Build and run images**

```
docker-compose build --no-cache api-server
docker-compose up -d api-server
```

`curl localhost:5000/address/exposure/direct?address=1BQAPyku1ZibWGAgd8QePpW1vAKHowqLez`

**2. Hit the endpoint from your local browser**
Enter `http://localhost:5000/address/exposure/direct?address=1BQAPyku1ZibWGAgd8QePpW1vAKHowqLez` into your browser!

You should see the following response:
```
{
  "chain": "btc", 
  "next_offset": 2, 
  "page_size": 100, 
  "rank_order_flowtype": "outflow", 
  "top_n": [
    {
      "both": "0.01733177", 
      "counterparty": "1FGhgLbMzrUV5mgwX9nkEeqHbKbUK29nbQ", 
      "inflows": "0", 
      "outflows": "0.01733177", 
      "rank": 1
    }, 
    {
      "both": "0.01733177", 
      "counterparty": "1Huro4zmi1kD1Ln4krTgJiXMYrAkEd4YSh", 
      "inflows": "0.01733177", 
      "outflows": "0", 
      "rank": 2
    }
  ]
}
```
