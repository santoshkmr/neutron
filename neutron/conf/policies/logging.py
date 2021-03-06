#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from oslo_policy import policy


rules = [
    policy.RuleDefault(
        'get_loggable_resources',
        'rule:admin_only',
        description='Access rule for getting loggable resources'),
    policy.RuleDefault(
        'create_log',
        'rule:admin_only',
        description='Access rule for creating network log'),
    policy.RuleDefault(
        'get_log',
        'rule:admin_only',
        description='Access rule for getting network log'),
    policy.RuleDefault(
        'get_logs',
        'rule:admin_only',
        description='Access rule for listing network logs'),
    policy.RuleDefault(
        'update_log',
        'rule:admin_only',
        description='Access rule for updating network log'),
    policy.RuleDefault(
        'delete_log',
        'rule:admin_only',
        description='Access rule for deleting network log'),
]


def list_rules():
    return rules
