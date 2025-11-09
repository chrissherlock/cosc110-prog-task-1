#!/bin/bash

unittest() {
    python3 -m unittest discover tests -v
}

interactiontest() {
   ./vote.py < tests/interaction1
   ./vote.py < tests/interaction2
   ./vote.py < tests/interaction3
}

if [[ "$#" -eq 0 ]]; then
    unittest
    interactiontest
    exit 0
fi

while [[ "$#" -gt 0 ]]; do
    case "$1" in
        --unittest)
	    unittest
	    shift
	    ;;

	--interactiontest)
	    interactiontest
	    shift
	    ;;

	-h|--help)
	    echo "Usage: vote.sh [--unittest] [--interactiontest]"
    esac
done
