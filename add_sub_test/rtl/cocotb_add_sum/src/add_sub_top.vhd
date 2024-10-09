library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity add_sub_top is
	port(dataa	 : in std_logic_vector(7 downto 0);
		  datab	 : in std_logic_vector(7 downto 0);
		  cin		 : in std_logic;
		  add_sub : in std_logic;
		  cout	 : out std_logic;
		  overflow: out std_logic;
		  result	 : out std_logic_vector(7 downto 0));
end entity;

architecture add_sub_top_rtl of add_sub_top is
	signal result_sig: std_logic_vector(7 downto 0);
	signal cout_sig  : std_logic;
	signal overflow_sig: std_logic;
	
begin
	lpm_add_sub_inst: entity work.lpm_add_sub_ip(syn)
		port map(dataa => dataa, datab => datab, add_sub => add_sub, cin => cin,
					cout => cout_sig, overflow => overflow_sig, result => result_sig);
	
	result <= result_sig;
	cout <= cout_sig;
	overflow <= overflow_sig;
end add_sub_top_rtl;