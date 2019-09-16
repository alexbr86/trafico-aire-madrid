#!/usr/bin/env bash

../../../lib/flume/apache-flume-1.9.0-bin/bin/flume-ng agent \
   -f /home/abalserio/tfm/source/flume/trafico/conf/flume.conf \
   --name Agent4 \
   -Dflume.root.logger=INFO,console \
   
#####################################################
## Para enviar datos:
## 
#####################################################
