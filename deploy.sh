#!/bin/bash

function usage() {
  echo "Usage:"
  echo "$0 -v <version> -s <source-files>"
}

while getopts ':hv:s:' option; do
  case "$option" in
    h) usage
       exit
       ;;
    v) VERSION_TEXT="$OPTARG"
       ;;
    s) SOURCE_FILES="$OPTARG"
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

pushd .
cd src/elasticbeanstalk

zip -r  discord-app.zip *
popd
mv src/elasticbeanstalk/discord-app.zip .
