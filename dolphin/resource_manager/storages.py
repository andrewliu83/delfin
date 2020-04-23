# Copyright 2013 NetApp
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""The shares api."""


import copy


from oslo_log import log
from dolphin import db
from dolphin.db.sqlalchemy import api as db

LOG = log.getLogger(__name__)


def build_storages(storages):
    views = [build_storage(storage)
             for storage in storages]
    return dict(storage=views)


def build_storage(storage):
    view = copy.deepcopy(storage)
    return view


def get_all(req):
    storage_all = db.storage_get_all()
    search_opts = [
        'name',
        'vendor',
        'model',
        'status',
    ]
    for search_opt in search_opts:
        if search_opt in req.GET:
            value = req.GET[search_opt]
            storage_all = [s for s in storage_all if s[search_opt] == value]
        if len(storage_all) == 0:
            break
    return build_storages(storage_all)