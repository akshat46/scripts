# scripts
Set of short handy scripts.

## drop_shadow

Adds drop shadows to given image.

## BR

Sets the brightness for `gmux_backlight`. Not tested on any device other than MacBook Pro with Ubuntu 16.04.

Input: `sudo br <brightness value between 1-420>`

May require a `NOPASSWD` rule to bypass passwords everytime.

## setmeupfam

a script for setting up a pi/linux device for routing, dns.
it can do following:
* add a direct route to laptop ip address
* flush gateways
* add default gateway to router interface
* replace given interface's ip address

  ####Options
  
  *Parameters*                    |*Detail*   
  |---                            |---
  **-h, --help**                  |show this help message and exit   
  **-l, --laptop-ip**             | your device(laptop) ip-address  
  **-i, --laptop-interface**      |name of the (pi) interface that is connected with your device(laptop) (default: eth0)
  **-r, --router-interface**      |name of the interface that is connected with router   
  **-changeIP**                                                       |change ip address of an interface. specify ip address with -l and interface with -j
  **-j, --laptop-pi-interface**   |name of the device interface whose ip address you want to change. this command is used with -changeIP (default: eth0)
  **-dns DNS**                    |your dns name
  **--no-routing**                |include this if you want to use the script to add dns name only. no route manipulation will be done
