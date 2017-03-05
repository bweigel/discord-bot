#!/bin/bash

PROJECT=discord-app

function usage() {
  echo "Usage:"
  echo "$0 [-b (builds image) | -r (runs docker)]"
}

function build_docker () {
    docker ps -a | grep "$PROJECT" | awk '{print $1}' | xargs docker rm
    docker build -t "$PROJECT":latest -f ./Dockerfile .
    RM_IMAGES=$(docker images | grep "\<none\>" | awk '{print $3}')
    if [[ ! -z "$RM_IMAGES" ]]; then
        for id in $RM_IMAGES; do
            docker rmi -f $id
        done
    fi
}

function run_docker () {
    docker run \
    -d \
    -v $HOME/.aws:/root/.aws \
    -v $(pwd):/dev_data/discord \
    "$PROJECT":latest \
    "/dev_data/discord/start_bot.sh"
}

while getopts ':hrb' option; do
  case "$option" in
    h) usage
       exit
       ;;
    r) run_docker
       ;;
    b) build_docker
       ;;
    :) echo "missing argument for -$OPTARG" >&2
       usage
       exit 1
       ;;
   \?) echo "Invalid option: -$OPTARG" >&2
       usage
       exit 1
       ;;
  esac
done
shift $((OPTIND - 1))


