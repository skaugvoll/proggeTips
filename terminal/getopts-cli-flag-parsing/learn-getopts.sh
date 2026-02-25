#!/usr/bin/env bash
# learn-getopts.sh
#
# A small "generic" getopts learning script:
# - Flags configure behavior (e.g. -t, -n, -v)
# - Remaining positional arguments are treated as ARGS (data)
# - Demonstrates how getopts, OPTARG, OPTIND, and shifting work
#
# Examples:
#   ./learn-getopts.sh
#   ./learn-getopts.sh -h
#   ./learn-getopts.sh -t 10
#   ./learn-getopts.sh -t 3 -n 2 "alpha beta" gamma
#   ./learn-getopts.sh -v -- "arg starting with -" "-x is not a flag now"
#
# NOTE: getopts supports short options (-t), not long options (--timeout)
# The special token "--" ends option parsing (useful for args that start with "-").

set -u

usage() {
  cat <<EOF
Usage:
  $0 [-t seconds] [-n count] [-v] [--] [args...]

Options:
  -t <seconds>   Example option with an argument (default: 5)
  -n <count>     Another option with an argument (default: 1)
  -v             Verbose mode (boolean flag)
  -h             Show this help

How parsing works:
  - getopts reads options from the front of the argument list.
  - OPTARG holds the option argument (for options like -t 10).
  - OPTIND is the index of the next argument to be processed.
  - After getopts, you usually run: shift \$((OPTIND - 1))
    so that "\$@" contains only the remaining positional arguments.

Examples:
  $0 -t 10 file1 file2
  $0 -v -n 3 "hello world" test
  $0 -v -- "-not-a-flag" "-t" "still just args"
EOF
}

parse_args() {
  #####################################################################
  # getopts parses short options like: -t 10 -v -h
  #
  # The option string ":t:n:vh" means:
  #   Leading ":"  → silent error mode (we handle errors ourselves)
  #   t:           → -t requires an argument
  #   n:           → -n requires an argument
  #   v            → -v takes no argument
  #   h            → -h takes no argument
  #
  # Variables used:
  #   opt     → current option letter being processed
  #   OPTARG  → the value for an option that requires an argument
  #   OPTIND  → index of next arg to process; used for shifting
  #
  # After parsing:
  #   shift $((OPTIND - 1))
  # removes processed flags from "$@" leaving only positional args.
  #####################################################################

  # Reset OPTIND in case parse_args is called more than once
  OPTIND=1

  # Defaults
  TIMEOUT=5
  COUNT=1
  VERBOSE=0
  ARG_SOURCE="no positional args"

  # Parse flags
  while getopts ":t:n:vh" opt; do
    case "$opt" in
      t)
        TIMEOUT="$OPTARG"
        ;;
      n)
        COUNT="$OPTARG"
        ;;
      v)
        VERBOSE=1
        ;;
      h)
        usage
        exit 0
        ;;
      :)
        echo "Error: Option -$OPTARG requires an argument." >&2
        usage
        exit 2
        ;;
      \?)
        echo "Error: Invalid option -$OPTARG" >&2
        usage
        exit 2
        ;;
    esac
  done

  # Drop parsed options so "$@" becomes positional args only
  shift $((OPTIND - 1))

  # Save remaining positional args into an array (generic data)
  ARGS=()
  if [[ $# -gt 0 ]]; then
    ARGS=( "$@" )
    ARG_SOURCE="positional arguments"
  fi
}

main() {
  # parse_args "$@"

  echo "Parsed options:"
  echo "  TIMEOUT:   $TIMEOUT"
  echo "  COUNT:     $COUNT"
  echo "  VERBOSE:   $VERBOSE"
  echo "  ARG_SOURCE:$ARG_SOURCE"
  echo ""

  echo "Positional args (\"$@\" after shifting):"
  if [[ ${#ARGS[@]} -eq 0 ]]; then
    echo "  (none)"
  else
    for i in "${!ARGS[@]}"; do
      printf "  ARGS[%d]=%q\n" "$i" "${ARGS[$i]}"
    done
  fi
  echo ""

  # Demonstrate using COUNT with ARGS (just as an example)
  if [[ ${#ARGS[@]} -gt 0 ]]; then
    echo "Example: print first COUNT args (or fewer if not enough):"
    max=$COUNT
    if [[ $max -gt ${#ARGS[@]} ]]; then
      max=${#ARGS[@]}
    fi
    for ((i=0; i<max; i++)); do
      echo "  ${ARGS[$i]}"
    done
  fi

  if [[ $VERBOSE -eq 1 ]]; then
    echo ""
    echo "Verbose debug:"
    echo "  Script name: $0"
    echo "  getopts ended with OPTIND=$OPTIND"
  fi
}


parse_args "$@"
main
