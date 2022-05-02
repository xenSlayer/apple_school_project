#!/bin/sh

printf "Run app on\n1.Production mode [P]\n2.Production local simulation [S]\n3.Development mode [D]\n>> "
read params
if [[$params == 'p']] || [[$params == 'P']];then echo "nice"; else echo "not nice"; fi