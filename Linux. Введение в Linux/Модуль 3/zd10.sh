#!bin/bash
while true; do
        read exp
        if [[ $exp = 'exit' ]]; then echo 'bye'; break; fi
        if let r=$(( $exp )); then echo $r; else echo 'error'; break; fi
done