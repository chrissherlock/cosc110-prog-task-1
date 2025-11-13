#!/bin/bash

unittest() {
    python3 -m unittest discover tests -v
}

interactiontest() {
   ./voting.py < tests/interaction1
   ./voting.py < tests/interaction2
   ./voting.py < tests/interaction3
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
	    echo "Usage: test.sh [--unittest] [--interactiontest]"
	    shift
	    ;;

        *)
	    echo "Error: unknown command"
	    echo "Usage: test.sh [--unittest] [--interactiontest]"
	    shift
    esac
done
