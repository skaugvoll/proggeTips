#!/usr/bin/env bash

## Test connectivity to a list of hosts and ports
## usage:
##   ./test-conn.sh [timeout_seconds] ["host port [port..]"]...
##   ./test-conn.sh 10 "dns.google 53" "www.google.com 443" # (uses 10 seconds timeout for each connection attempt)
##   ./test-conn.sh "dns.google 53" "www.google.com 443" #  (uses default timeout of 5 seconds)

set -u

# ANSI colors
GREEN=$'\e[0;32m'
RED=$'\e[0;31m'
NC=$'\e[0m' # Reset color

## ---------- Config
## ---- timeout config
TIMEOUT=5 # Default timeout in seconds for each connection attempt
# If first arg looks like an integer, treat it as timeout
if [[ $# -ge 1 && "$1" =~ ^[0-9]+$ ]]; then
  TIMEOUT="$1"
  shift
fi
## ---- hosts config
HOST_SOURCE="hardcoded list"
HOSTS=(
  #dns.google                         53     TCP: OPEN   UDP: OPEN   ICMP: OPEN
  "dns.google 53"
  #www.google.com                    80,443     TCP: OPEN   UDP: OPEN ICMP: OPEN
  "www.google.com 80 443"
)
# Remaining args (if any) are host rows, overwrite the default list
if [[ $# -ge 1 ]]; then
  HOSTS=( "$@" )
  HOST_SOURCE="command-line arguments"

fi


## ---------- Config


RESULTS=()

function status_to_text_and_color() {
    local code=$1
    local text color
    if [[ $code -eq 0 ]]; then
        text="OPEN"
        color=$GREEN
    else
        text="CLOSED"
        color=$RED
    fi
    printf "%s|%s" "$text" "$color"
}

function store_connection_status() {
    local host_url=$1
    local port=$2
    local tcp_code=$3
    local udp_code=$4
    local icmp_code=$5

    local tcp_txt tcp_col udp_txt udp_col icmp_txt icmp_col tmp

    tmp="$(status_to_text_and_color "$tcp_code")"
    tcp_txt="${tmp%%|*}"; tcp_col="${tmp#*|}"

    tmp="$(status_to_text_and_color "$udp_code")"
    udp_txt="${tmp%%|*}"; udp_col="${tmp#*|}"

    tmp="$(status_to_text_and_color "$icmp_code")"
    icmp_txt="${tmp%%|*}"; icmp_col="${tmp#*|}"

    # Keep alignment similar to your existing output
    line=$(printf "%-35s %-6s TCP: %s%-7s%s UDP: %s%-7s%s ICMP: %s%-7s%s" \
        "$host_url" \
        "$port" \
        "$tcp_col" "$tcp_txt" "$NC" \
        "$udp_col" "$udp_txt" "$NC" \
        "$icmp_col" "$icmp_txt" "$NC")

    RESULTS+=("$line")
}

function print_config() {
    echo "Configuration:"
    echo "=============="
    echo "Source host: $(hostname)"
    echo "Timeout: $TIMEOUT seconds"
    echo "Host source: $HOST_SOURCE"
    echo "For each destination host & port"
    echo "the script will attempt to connect using netcat (TCP + UDP) and ping (ICMP),"
    echo "each with the specified timeout."
    echo ""
    echo "Note: UDP checks are best-effort; 'CLOSED' can mean 'no response' (might still be open)."
}

function show_progress_bar() {
    local progress=$1
    local width=40

    local filled=$((progress * width / 100))
    local empty=$((width - filled))

    printf "\r[%-${width}s] %3d%%" "$(printf '#%.0s' $(seq 1 "$filled"))" "$progress"
}

function print_results() {
    echo "Connection Test Results: [$(date)] [tcp: nc -vz <adr> <prt>] [udp: nc -uvz <adr> <prt>]"
    echo "========================"
    printf "%s\n" "${RESULTS[@]}"
}

function main(){
    echo "Testing connectivity to hosts..."
    START=0
    END=${#HOSTS[@]}

    for row in "${HOSTS[@]}"; do
        read -r host_url _ <<< "$row"

        show_progress_bar $((START * 100 / END))

        # Loop all ports except the first column
        for port in ${row#"$host_url"}; do
            # TCP
            nc -vz -w "$TIMEOUT" "$host_url" "$port" >/dev/null 2>&1
            tcp_res=$?

            # UDP (-u) + "zero-I/O mode" (-z). Still best-effort.
            nc -uvz -w "$TIMEOUT" "$host_url" "$port" >/dev/null 2>&1
            udp_res=$?

            # ICMP
            ping -c1 -W "$TIMEOUT" "$host_url" >/dev/null 2>&1
            ping_res=$?

            store_connection_status "$host_url" "$port" "$tcp_res" "$udp_res" "$ping_res"
        done

        START=$((START + 1))
        show_progress_bar $((START * 100 / END))
    done

    echo ""
}

print_config
main
echo ""
print_results