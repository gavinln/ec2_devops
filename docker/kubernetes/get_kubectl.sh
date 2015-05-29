#!/bin/bash

KUBECTL_BIN=https://storage.googleapis.com/kubernetes-release/release/v0.17.0/bin/linux/amd64/kubectl

wget $KUBECTL_BIN
chmod +x ./kubectl


