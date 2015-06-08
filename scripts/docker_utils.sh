#!/bin/bash
#
# Usage: source docker_utils.sh

SOURCE="${BASH_SOURCE[0]:-$0}"
DIR="$( cd "$( dirname "$SOURCE" )" && pwd )"

alias drm="docker rm"

function drma() {
	docker rm $(docker ps -q -a -f status=exited);
}

alias dps="docker ps"
alias dlps="docker ps | less -S"

alias dpsa="docker ps -a"
alias dlpsa="docker ps -a | less -S"

function dexec() {
	docker exec -t -i $1 bash
}
