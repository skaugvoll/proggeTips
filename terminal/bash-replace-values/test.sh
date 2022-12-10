string="a@1.2.0-beta.21"
delimiter="@"
temp_1=${string#*$delimiter} # remover everything up to (including), delimiter
temp_2=${string%$delimiter*} # remover everything after (including), delimiter

echo $temp_1
echo $temp_2
