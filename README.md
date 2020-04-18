swig -python groupcidr.i

gcc -fPIC -c groupcidr.c groupcidr_wrap.c -I/usr/include/python3.7m

ld -shared groupcidr.o groupcidr_wrap.o -o _groupcidr.so

python3

import groupcidr

groupcidr.read_input("example.txt")

14.224.234.238/32
47.55.81.118/32
49.241.218.177/32
64.128.217.133/32
65.203.182.111/32
71.129.145.227/32
87.66.68.24/32
88.206.198.236/32
89.145.152.25/32
102.139.81.170/32
125.250.137.63/32
132.166.163.0/32
151.164.56.87/32
185.61.131.190/32
201.48.44.210/32
