#!/bin/bash
#
# Usage: source docker_utils.sh

SOURCE="${BASH_SOURCE[0]:-$0}"
DIR="$( cd "$( dirname "$SOURCE" )" && pwd )"

alias drm="docker rm"
alias drma="docker rm $(docker ps -aq)"

alias dps="docker ps"
alias dlps="docker ps | less -S"

alias dpsa="docker ps -a"
alias dlpsa="docker ps -a | less -S"
