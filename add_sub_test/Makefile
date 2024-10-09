TOPLEVEL_LANG = vhdl
SIM = questa
WAVES=1

# VHDL_SOURCES = ~/Documents/Quartus/cocotb_add_sum/IP/lpm_add_sub_ip.vhd \
# 			   ~/Documents/Quartus/cocotb_add_sum/src/add_sub_top.vhd
VHDL_SOURCES = ./rtl/cocotb_add_sum/IP/lpm_add_sub_ip.vhd \
			   ./rtl/cocotb_add_sum/src/add_sub_top.vhd
			   
TOPLEVEL = add_sub_top
MODULE = lpm_add_sub_test

include $(shell cocotb-config --makefiles)/Makefile.sim