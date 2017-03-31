#!/bin/bash
pushd site
gsutil rsync -d ./* gs://museum.naturalcapitalproject.org
popd
