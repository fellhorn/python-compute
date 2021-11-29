# Copyright 2021 Google LLC
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
import time
import uuid

import google.auth
from google.cloud import compute_v1
import pytest


from sample_firewall import (
    create_firewall_rule,
    delete_firewall_rule,
    get_firewall_rule,
    list_firewall_rules,
    patch_firewall_priority,
)

PROJECT = google.auth.default()[1]


@pytest.fixture
def firewall_rule():
    firewall_rule = compute_v1.Firewall()
    firewall_rule.name = "firewall-sample-test" + uuid.uuid4().hex[:10]
    firewall_rule.direction = "INGRESS"
    allowed_ports = compute_v1.Allowed()
    allowed_ports.I_p_protocol = "tcp"
    allowed_ports.ports = ["80"]
    firewall_rule.allowed = [allowed_ports]
    firewall_rule.source_ranges = ["0.0.0.0/0"]
    firewall_rule.network = "global/networks/default"
    firewall_rule.description = "Rule generated by Python sample test fixture."
    firewall_rule.target_tags = ["web"]

    firewall_client = compute_v1.FirewallsClient()
    op = firewall_client.insert(project=PROJECT, firewall_resource=firewall_rule)

    op_client = compute_v1.GlobalOperationsClient()
    op_client.wait(project=PROJECT, operation=op.name)

    yield firewall_client.get(project=PROJECT, firewall=firewall_rule.name)

    op = firewall_client.delete(project=PROJECT, firewall=firewall_rule.name)
    op_client.wait(project=PROJECT, operation=op.name)


def test_create_delete():
    rule_name = "firewall-sample-test-" + uuid.uuid4().hex[:10]
    create_firewall_rule(PROJECT, rule_name)
    rule = get_firewall_rule(PROJECT, rule_name)
    assert rule.name == rule_name
    assert "web" in rule.target_tags
    delete_firewall_rule(PROJECT, rule_name)
    assert all(rule.name != rule_name for rule in list_firewall_rules(PROJECT))


def test_patch_rule(firewall_rule):
    fw_client = compute_v1.FirewallsClient()
    assert firewall_rule.priority == 1000
    patch_firewall_priority(PROJECT, firewall_rule.name, 500)
    time.sleep(2)
    updated_firewall_rule = fw_client.get(project=PROJECT, firewall=firewall_rule.name)
    assert updated_firewall_rule.priority == 500
