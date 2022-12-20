#!usr/bin/env sh
curl --unix-socket /tmp/firecracker.socket -i \
  -X PUT 'http://localhost/network-interfaces/wlan0' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
      "iface_id": "wlan0",
      "guest_mac": "AA:FC:00:00:00:01",
      "host_dev_name": "tap0"
    }'
