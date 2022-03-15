# network_pinger
Very simple script to ping cloudflare every 5 seconds, to check and log if (and when) your network goes down

# Required Modules
```pythonping``` (https://pypi.org/project/pythonping/)

```time```

```datetime```

# Usage
Download / git clone the repo, install the requirements (should only be pythonping) and run via ```python3 main.py```

# Example File Output
Success: ```Pings Successful! | Time: 2022-03-15 16:33:40.721818 | Avg Ping: 9.79```

Failure: ```Pings Failed! | Time: 2022-03-15 16:23:59.227668```


