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
        'create_floatingip_port_forwarding',
        'rule:admin_or_ext_parent_owner',
        description='Access rule for creating floating IP port forwarding'),
    policy.RuleDefault(
        'get_floatingip_port_forwarding',
        'rule:admin_or_ext_parent_owner',
        description='Access rule for getting floating IP port forwarding'),
    # TOOD(amotoki): get_floatingip_port_forwardings looks unnecessary.
    policy.RuleDefault(
        'get_floatingip_port_forwardings',
        'rule:admin_or_ext_parent_owner',
        description='Access rule for listing floating IP port forwardings'),
    policy.RuleDefault(
        'update_floatingip_port_forwarding',
        'rule:admin_or_ext_parent_owner',
        description='Access rule for updating floating IP port forwarding'),
    policy.RuleDefault(
        'delete_floatingip_port_forwarding',
        'rule:admin_or_ext_parent_owner',
        description='Access rule for deleting floating IP port forwarding'),
]


def list_rules():
    return rules
