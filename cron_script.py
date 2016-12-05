import requests
get_stats_endpoint = "http://ec2-52-214-14-232.eu-west-1.compute.amazonaws.com/get_stats"
get_stats = requests.get(get_stats_endpoint)
print get_stats.status_code