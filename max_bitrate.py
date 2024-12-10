# max_bitrate.py
# usage python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# Written by Tejas Vinod
# Test
# python3 max_bitrate.py 1 1 1 100 1 .9 1
# 16

# import Python modules
# e.g., import math # math module
import sys # argv
import math # math module

# "constants"
c = 2.99792458e8; # speed of light (m/s)

# assumptons
L_a_dB = 0; # atmospheric loss (dB)
L_t_dB = -1; # transmitter to antenna line loss (dB)


# initialize script arguments
tx_w = float('nan')
tx_gain_db = float('nan')
freq_hz = float('nan')
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

# parse script arguments
if len(sys.argv) == 8:
     tx_w = float(sys.argv[1])
     tx_gain_db = float(sys.argv[2])
     freq_hz = float(sys.argv[3])
     dist_km = float(sys.argv[4])
     rx_gain_db = float(sys.argv[5])
     n0_j = float(sys.argv[6])
     bw_hz = float(sys.argv[7])

else:
   print(\
    'Usage: '\
    'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
   )
   exit()

# write script below this line
L_a = 10**(L_a_dB/10); 
L_l = 10**(L_t_dB/10); 

G_t = 10**(tx_gain_db/10)
G_r = 10**(rx_gain_db/10)

lam = c/freq_hz

C = tx_w*L_l*G_t*(lam/(4*math.pi*(dist_km*1000)))**2*L_a*G_r
N = n0_j*bw_hz


r_max = bw_hz*math.log2(1 + C/N)

print(math.floor(r_max))