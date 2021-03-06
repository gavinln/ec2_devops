#!/bin/bash

# Copyright 2014 The Kubernetes Authors All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

unset FLOWER_SERVICE_PORT_5555_TCP_PORT
unset FLOWER_SERVICE_SERVICE_HOST
unset FLOWER_SERVICE_PORT_5555_TCP_PROTO
unset FLOWER_SERVICE_SERVICE_PORT
unset FLOWER_SERVICE_PORT
unset FLOWER_SERVICE_PORT_5555_TCP_ADDR
unset FLOWER_SERVICE_PORT_5555_TCP

#while true; do echo 'Hit CTRL+C'; sleep 35; done

flower --broker=amqp://guest:guest@${RABBITMQ_SERVICE_SERVICE_HOST}:5672//
