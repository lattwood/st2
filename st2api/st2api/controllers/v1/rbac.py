# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pecan import rest

from st2api.controllers.resource import ResourceController
from st2common.models.api.base import jsexpose
from st2common.models.api.rbac import RoleAPI
from st2common.persistence.rbac import Role

__all__ = [
    'RBACController',
    'RolesController'
]


class RolesController(ResourceController):
    model = RoleAPI
    access = Role
    supported_filters = {
        'name': 'name',
    }

    query_options = {
        'sort': ['name']
    }

    @jsexpose(arg_types=[str])
    def get_one(self, name_or_id):
        return self._get_one_by_name_or_id(name_or_id=name_or_id)


class RBACController(rest.RestController):
    roles = RolesController()
