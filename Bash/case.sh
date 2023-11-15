echo "##################################"

var="red"

case ${var} in
	"yes" )
		echo "glad you agreed"
		;;
	"no" )
		echo "sorry; good bye"
		exit
		;;
	* )
		echo "invalid answer. try again"
		;;
esac

echo "##################################"

var="yes"

case ${var} in
	( "yes" )
		echo "glad you agreed"
		;;
	( "no" )
		echo "sorry; good bye"
		exit
		;;
	( * )
		echo "invalid answer. try again"
		;;
esac

echo "##################################"

var="yes"

case ${var} in
	[Yy]?? | [Ss]ure | [Oo][Kk]* )
		echo "OK. Glad we agree"
		;;
	[Nn][Oo]* )
		echo "Fine. Leave then"
		exit
		;;
	( * )
		echo "Try again"
		# continue
		;;
esac

echo "##################################"