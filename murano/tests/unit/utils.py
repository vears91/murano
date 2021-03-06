# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from murano import context
from murano.db import session


def dummy_context(user='test_username', tenant_id='test_tenant_id',
                  request_id='dummy-request', **kwargs):

    # NOTE(kzaitsev) we need to pass non-False value to request_id, to
    # prevent it being generated by oslo during tests.
    params = {
        'request_id': request_id,
        'tenant': tenant_id,
        'user': user,
    }
    params.update(kwargs)
    return context.RequestContext.from_dict(params)


def save_models(*models):
    s = session.get_session()
    for m in models:
        m.save(s)
