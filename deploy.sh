#!/bin/bash
gsutil -m rsync -d -R site/ gs://museum.naturalcapitalproject.org/
