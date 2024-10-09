transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vcom -93 -work work {/home/ojakinlade/Documents/Quartus/cocotb_add_sum/IP/lpm_add_sub_ip.vhd}
vcom -93 -work work {/home/ojakinlade/Documents/Quartus/cocotb_add_sum/src/add_sub_top.vhd}

