# Copyright 2018 Microsoft Corporation
# Copyright (c) 2016, 2017 by Delphix. All rights reserved.
# Copyright 2019 Joyent, Inc.
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
#
# Requires Python 2.6+ and Openssl 1.0+
#

import azurelinuxagent.common.conf as conf

from azurelinuxagent.common.version import DISTRO_NAME, DISTRO_VERSION, \
                                     DISTRO_FULL_NAME

from .default import ProvisionHandler
from .cloudinit import CloudInitProvisionHandler
from .illumos import illumosProvisionHandler

def get_provision_handler(distro_name=DISTRO_NAME, 
                            distro_version=DISTRO_VERSION,
                            distro_full_name=DISTRO_FULL_NAME):

    if distro_name == "illumos":
        return illumosProvisionHandler();

    if conf.get_provision_cloudinit():
        return CloudInitProvisionHandler()

    return ProvisionHandler()

