# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from requests import __version__ as requests_version
import dataclasses
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.compute_v1.types import compute

from .base import (
    NetworkFirewallPoliciesTransport,
    DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO,
)


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class NetworkFirewallPoliciesRestInterceptor:
    """Interceptor for NetworkFirewallPolicies.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the NetworkFirewallPoliciesRestTransport.

    .. code-block:: python
        class MyCustomNetworkFirewallPoliciesInterceptor(NetworkFirewallPoliciesRestInterceptor):
            def pre_add_association(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_association(response):
                logging.log(f"Received response: {response}")

            def pre_add_rule(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_rule(response):
                logging.log(f"Received response: {response}")

            def pre_clone_rules(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_clone_rules(response):
                logging.log(f"Received response: {response}")

            def pre_delete(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete(response):
                logging.log(f"Received response: {response}")

            def pre_get(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get(response):
                logging.log(f"Received response: {response}")

            def pre_get_association(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_association(response):
                logging.log(f"Received response: {response}")

            def pre_get_iam_policy(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iam_policy(response):
                logging.log(f"Received response: {response}")

            def pre_get_rule(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_rule(response):
                logging.log(f"Received response: {response}")

            def pre_insert(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert(response):
                logging.log(f"Received response: {response}")

            def pre_list(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list(response):
                logging.log(f"Received response: {response}")

            def pre_patch(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_patch(response):
                logging.log(f"Received response: {response}")

            def pre_patch_rule(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_patch_rule(response):
                logging.log(f"Received response: {response}")

            def pre_remove_association(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_association(response):
                logging.log(f"Received response: {response}")

            def pre_remove_rule(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_rule(response):
                logging.log(f"Received response: {response}")

            def pre_set_iam_policy(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_iam_policy(response):
                logging.log(f"Received response: {response}")

            def pre_test_iam_permissions(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_iam_permissions(response):
                logging.log(f"Received response: {response}")

        transport = NetworkFirewallPoliciesRestTransport(interceptor=MyCustomNetworkFirewallPoliciesInterceptor())
        client = NetworkFirewallPoliciesClient(transport=transport)


    """

    def pre_add_association(
        self,
        request: compute.AddAssociationNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        compute.AddAssociationNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for add_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_add_association(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for add_association

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_add_rule(
        self,
        request: compute.AddRuleNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[compute.AddRuleNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for add_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_add_rule(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for add_rule

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_clone_rules(
        self,
        request: compute.CloneRulesNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        compute.CloneRulesNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for clone_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_clone_rules(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for clone_rules

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_delete(
        self,
        request: compute.DeleteNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[compute.DeleteNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_delete(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for delete

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_get(
        self,
        request: compute.GetNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[compute.GetNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_get(self, response: compute.FirewallPolicy) -> compute.FirewallPolicy:
        """Post-rpc interceptor for get

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_get_association(
        self,
        request: compute.GetAssociationNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        compute.GetAssociationNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for get_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_get_association(
        self, response: compute.FirewallPolicyAssociation
    ) -> compute.FirewallPolicyAssociation:
        """Post-rpc interceptor for get_association

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: compute.GetIamPolicyNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        compute.GetIamPolicyNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: compute.Policy) -> compute.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_get_rule(
        self,
        request: compute.GetRuleNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[compute.GetRuleNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_get_rule(
        self, response: compute.FirewallPolicyRule
    ) -> compute.FirewallPolicyRule:
        """Post-rpc interceptor for get_rule

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_insert(
        self,
        request: compute.InsertNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[compute.InsertNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for insert

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_insert(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for insert

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_list(
        self,
        request: compute.ListNetworkFirewallPoliciesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[compute.ListNetworkFirewallPoliciesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_list(
        self, response: compute.FirewallPolicyList
    ) -> compute.FirewallPolicyList:
        """Post-rpc interceptor for list

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_patch(
        self,
        request: compute.PatchNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[compute.PatchNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for patch

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_patch(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for patch

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_patch_rule(
        self,
        request: compute.PatchRuleNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        compute.PatchRuleNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for patch_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_patch_rule(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for patch_rule

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_remove_association(
        self,
        request: compute.RemoveAssociationNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        compute.RemoveAssociationNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for remove_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_remove_association(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for remove_association

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_remove_rule(
        self,
        request: compute.RemoveRuleNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        compute.RemoveRuleNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for remove_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_remove_rule(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for remove_rule

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: compute.SetIamPolicyNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        compute.SetIamPolicyNetworkFirewallPolicyRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: compute.Policy) -> compute.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: compute.TestIamPermissionsNetworkFirewallPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        compute.TestIamPermissionsNetworkFirewallPolicyRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkFirewallPolicies server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: compute.TestPermissionsResponse
    ) -> compute.TestPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the NetworkFirewallPolicies server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class NetworkFirewallPoliciesRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: NetworkFirewallPoliciesRestInterceptor


class NetworkFirewallPoliciesRestTransport(NetworkFirewallPoliciesTransport):
    """REST backend transport for NetworkFirewallPolicies.

    The NetworkFirewallPolicies API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    _STUBS: Dict[str, NetworkFirewallPoliciesRestStub] = {}

    def __init__(
        self,
        *,
        host: str = "compute.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[NetworkFirewallPoliciesRestInterceptor] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or NetworkFirewallPoliciesRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AddAssociation(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("AddAssociation")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.AddAssociationNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Operation:
            r"""Call the add association method over HTTP.

            Args:
                request (~.compute.AddAssociationNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.AddAssociation.
                See the method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}/addAssociation",
                    "body": "firewall_policy_association_resource",
                },
            ]
            request, metadata = self._interceptor.pre_add_association(request, metadata)
            request_kwargs = compute.AddAssociationNetworkFirewallPolicyRequest.to_dict(
                request
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            # Jsonify the request body
            body = compute.FirewallPolicyAssociation.to_json(
                compute.FirewallPolicyAssociation(transcoded_request["body"]),
                including_default_value_fields=False,
                use_integers_for_enums=False,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.AddAssociationNetworkFirewallPolicyRequest.to_json(
                    compute.AddAssociationNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Operation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_add_association(resp)
            return resp

    class _AddRule(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("AddRule")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.AddRuleNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Operation:
            r"""Call the add rule method over HTTP.

            Args:
                request (~.compute.AddRuleNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.AddRule. See the
                method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}/addRule",
                    "body": "firewall_policy_rule_resource",
                },
            ]
            request, metadata = self._interceptor.pre_add_rule(request, metadata)
            request_kwargs = compute.AddRuleNetworkFirewallPolicyRequest.to_dict(
                request
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            # Jsonify the request body
            body = compute.FirewallPolicyRule.to_json(
                compute.FirewallPolicyRule(transcoded_request["body"]),
                including_default_value_fields=False,
                use_integers_for_enums=False,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.AddRuleNetworkFirewallPolicyRequest.to_json(
                    compute.AddRuleNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Operation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_add_rule(resp)
            return resp

    class _CloneRules(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("CloneRules")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.CloneRulesNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Operation:
            r"""Call the clone rules method over HTTP.

            Args:
                request (~.compute.CloneRulesNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.CloneRules. See
                the method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}/cloneRules",
                },
            ]
            request, metadata = self._interceptor.pre_clone_rules(request, metadata)
            request_kwargs = compute.CloneRulesNetworkFirewallPolicyRequest.to_dict(
                request
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.CloneRulesNetworkFirewallPolicyRequest.to_json(
                    compute.CloneRulesNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Operation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_clone_rules(resp)
            return resp

    class _Delete(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("Delete")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.DeleteNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Operation:
            r"""Call the delete method over HTTP.

            Args:
                request (~.compute.DeleteNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.Delete. See the
                method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}",
                },
            ]
            request, metadata = self._interceptor.pre_delete(request, metadata)
            request_kwargs = compute.DeleteNetworkFirewallPolicyRequest.to_dict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.DeleteNetworkFirewallPolicyRequest.to_json(
                    compute.DeleteNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Operation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_delete(resp)
            return resp

    class _Get(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("Get")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.GetNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.FirewallPolicy:
            r"""Call the get method over HTTP.

            Args:
                request (~.compute.GetNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.Get. See the
                method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.FirewallPolicy:
                    Represents a Firewall Policy
                resource.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}",
                },
            ]
            request, metadata = self._interceptor.pre_get(request, metadata)
            request_kwargs = compute.GetNetworkFirewallPolicyRequest.to_dict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.GetNetworkFirewallPolicyRequest.to_json(
                    compute.GetNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.FirewallPolicy.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_get(resp)
            return resp

    class _GetAssociation(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("GetAssociation")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.GetAssociationNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.FirewallPolicyAssociation:
            r"""Call the get association method over HTTP.

            Args:
                request (~.compute.GetAssociationNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.GetAssociation.
                See the method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.FirewallPolicyAssociation:

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}/getAssociation",
                },
            ]
            request, metadata = self._interceptor.pre_get_association(request, metadata)
            request_kwargs = compute.GetAssociationNetworkFirewallPolicyRequest.to_dict(
                request
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.GetAssociationNetworkFirewallPolicyRequest.to_json(
                    compute.GetAssociationNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.FirewallPolicyAssociation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_get_association(resp)
            return resp

    class _GetIamPolicy(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("GetIamPolicy")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.GetIamPolicyNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (~.compute.GetIamPolicyNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.GetIamPolicy.
                See the method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources. A
                ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role. For some types of Google
                Cloud resources, a ``binding`` can also specify a
                ``condition``, which is a logical expression that allows
                access to a resource only if the expression evaluates to
                ``true``. A condition can add constraints based on
                attributes of the request, the resource, or both. To
                learn which resources support conditions in their IAM
                policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.
                **JSON example:** { "bindings": [ { "role":
                "roles/resourcemanager.organizationAdmin", "members": [
                "user:mike@example.com", "group:admins@example.com",
                "domain:google.com",
                "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                ] }, { "role":
                "roles/resourcemanager.organizationViewer", "members": [
                "user:eve@example.com" ], "condition": { "title":
                "expirable access", "description": "Does not grant
                access after Sep 2020", "expression": "request.time <
                timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag":
                "BwWWja0YfJA=", "version": 3 } **YAML example:**
                bindings: - members: - user:mike@example.com -
                group:admins@example.com - domain:google.com -
                serviceAccount:my-project-id@appspot.gserviceaccount.com
                role: roles/resourcemanager.organizationAdmin - members:
                - user:eve@example.com role:
                roles/resourcemanager.organizationViewer condition:
                title: expirable access description: Does not grant
                access after Sep 2020 expression: request.time <
                timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA=
                version: 3 For a description of IAM and its features,
                see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{resource}/getIamPolicy",
                },
            ]
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            request_kwargs = compute.GetIamPolicyNetworkFirewallPolicyRequest.to_dict(
                request
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.GetIamPolicyNetworkFirewallPolicyRequest.to_json(
                    compute.GetIamPolicyNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Policy.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_get_iam_policy(resp)
            return resp

    class _GetRule(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("GetRule")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.GetRuleNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.FirewallPolicyRule:
            r"""Call the get rule method over HTTP.

            Args:
                request (~.compute.GetRuleNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.GetRule. See the
                method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.FirewallPolicyRule:
                    Represents a rule that describes one
                or more match conditions along with the
                action to be taken when traffic matches
                this condition (allow or deny).

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}/getRule",
                },
            ]
            request, metadata = self._interceptor.pre_get_rule(request, metadata)
            request_kwargs = compute.GetRuleNetworkFirewallPolicyRequest.to_dict(
                request
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.GetRuleNetworkFirewallPolicyRequest.to_json(
                    compute.GetRuleNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.FirewallPolicyRule.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_get_rule(resp)
            return resp

    class _Insert(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("Insert")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.InsertNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Operation:
            r"""Call the insert method over HTTP.

            Args:
                request (~.compute.InsertNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.Insert. See the
                method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies",
                    "body": "firewall_policy_resource",
                },
            ]
            request, metadata = self._interceptor.pre_insert(request, metadata)
            request_kwargs = compute.InsertNetworkFirewallPolicyRequest.to_dict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            # Jsonify the request body
            body = compute.FirewallPolicy.to_json(
                compute.FirewallPolicy(transcoded_request["body"]),
                including_default_value_fields=False,
                use_integers_for_enums=False,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.InsertNetworkFirewallPolicyRequest.to_json(
                    compute.InsertNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Operation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_insert(resp)
            return resp

    class _List(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("List")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.ListNetworkFirewallPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.FirewallPolicyList:
            r"""Call the list method over HTTP.

            Args:
                request (~.compute.ListNetworkFirewallPoliciesRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.List. See the
                method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.FirewallPolicyList:

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies",
                },
            ]
            request, metadata = self._interceptor.pre_list(request, metadata)
            request_kwargs = compute.ListNetworkFirewallPoliciesRequest.to_dict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.ListNetworkFirewallPoliciesRequest.to_json(
                    compute.ListNetworkFirewallPoliciesRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.FirewallPolicyList.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_list(resp)
            return resp

    class _Patch(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("Patch")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.PatchNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Operation:
            r"""Call the patch method over HTTP.

            Args:
                request (~.compute.PatchNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.Patch. See the
                method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}",
                    "body": "firewall_policy_resource",
                },
            ]
            request, metadata = self._interceptor.pre_patch(request, metadata)
            request_kwargs = compute.PatchNetworkFirewallPolicyRequest.to_dict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            # Jsonify the request body
            body = compute.FirewallPolicy.to_json(
                compute.FirewallPolicy(transcoded_request["body"]),
                including_default_value_fields=False,
                use_integers_for_enums=False,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.PatchNetworkFirewallPolicyRequest.to_json(
                    compute.PatchNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Operation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_patch(resp)
            return resp

    class _PatchRule(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("PatchRule")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.PatchRuleNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Operation:
            r"""Call the patch rule method over HTTP.

            Args:
                request (~.compute.PatchRuleNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.PatchRule. See
                the method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}/patchRule",
                    "body": "firewall_policy_rule_resource",
                },
            ]
            request, metadata = self._interceptor.pre_patch_rule(request, metadata)
            request_kwargs = compute.PatchRuleNetworkFirewallPolicyRequest.to_dict(
                request
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            # Jsonify the request body
            body = compute.FirewallPolicyRule.to_json(
                compute.FirewallPolicyRule(transcoded_request["body"]),
                including_default_value_fields=False,
                use_integers_for_enums=False,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.PatchRuleNetworkFirewallPolicyRequest.to_json(
                    compute.PatchRuleNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Operation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_patch_rule(resp)
            return resp

    class _RemoveAssociation(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("RemoveAssociation")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.RemoveAssociationNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Operation:
            r"""Call the remove association method over HTTP.

            Args:
                request (~.compute.RemoveAssociationNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.RemoveAssociation.
                See the method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}/removeAssociation",
                },
            ]
            request, metadata = self._interceptor.pre_remove_association(
                request, metadata
            )
            request_kwargs = (
                compute.RemoveAssociationNetworkFirewallPolicyRequest.to_dict(request)
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.RemoveAssociationNetworkFirewallPolicyRequest.to_json(
                    compute.RemoveAssociationNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Operation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_remove_association(resp)
            return resp

    class _RemoveRule(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("RemoveRule")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.RemoveRuleNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Operation:
            r"""Call the remove rule method over HTTP.

            Args:
                request (~.compute.RemoveRuleNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.RemoveRule. See
                the method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource. Google Compute Engine
                has three Operation resources: \*
                `Global </compute/docs/reference/rest/v1/globalOperations>`__
                \*
                `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                \*
                `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__
                You can use an operation resource to manage asynchronous
                API requests. For more information, read Handling API
                responses. Operations can be global, regional or zonal.
                - For global operations, use the ``globalOperations``
                resource. - For regional operations, use the
                ``regionOperations`` resource. - For zonal operations,
                use the ``zonalOperations`` resource. For more
                information, read Global, Regional, and Zonal Resources.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{firewall_policy}/removeRule",
                },
            ]
            request, metadata = self._interceptor.pre_remove_rule(request, metadata)
            request_kwargs = compute.RemoveRuleNetworkFirewallPolicyRequest.to_dict(
                request
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.RemoveRuleNetworkFirewallPolicyRequest.to_json(
                    compute.RemoveRuleNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Operation.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_remove_rule(resp)
            return resp

    class _SetIamPolicy(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("SetIamPolicy")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.SetIamPolicyNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (~.compute.SetIamPolicyNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.SetIamPolicy.
                See the method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources. A
                ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role. For some types of Google
                Cloud resources, a ``binding`` can also specify a
                ``condition``, which is a logical expression that allows
                access to a resource only if the expression evaluates to
                ``true``. A condition can add constraints based on
                attributes of the request, the resource, or both. To
                learn which resources support conditions in their IAM
                policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.
                **JSON example:** { "bindings": [ { "role":
                "roles/resourcemanager.organizationAdmin", "members": [
                "user:mike@example.com", "group:admins@example.com",
                "domain:google.com",
                "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                ] }, { "role":
                "roles/resourcemanager.organizationViewer", "members": [
                "user:eve@example.com" ], "condition": { "title":
                "expirable access", "description": "Does not grant
                access after Sep 2020", "expression": "request.time <
                timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag":
                "BwWWja0YfJA=", "version": 3 } **YAML example:**
                bindings: - members: - user:mike@example.com -
                group:admins@example.com - domain:google.com -
                serviceAccount:my-project-id@appspot.gserviceaccount.com
                role: roles/resourcemanager.organizationAdmin - members:
                - user:eve@example.com role:
                roles/resourcemanager.organizationViewer condition:
                title: expirable access description: Does not grant
                access after Sep 2020 expression: request.time <
                timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA=
                version: 3 For a description of IAM and its features,
                see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{resource}/setIamPolicy",
                    "body": "global_set_policy_request_resource",
                },
            ]
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            request_kwargs = compute.SetIamPolicyNetworkFirewallPolicyRequest.to_dict(
                request
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            # Jsonify the request body
            body = compute.GlobalSetPolicyRequest.to_json(
                compute.GlobalSetPolicyRequest(transcoded_request["body"]),
                including_default_value_fields=False,
                use_integers_for_enums=False,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.SetIamPolicyNetworkFirewallPolicyRequest.to_json(
                    compute.SetIamPolicyNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.Policy.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_set_iam_policy(resp)
            return resp

    class _TestIamPermissions(NetworkFirewallPoliciesRestStub):
        def __hash__(self):
            return hash("TestIamPermissions")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: compute.TestIamPermissionsNetworkFirewallPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> compute.TestPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (~.compute.TestIamPermissionsNetworkFirewallPolicyRequest):
                    The request object. A request message for
                NetworkFirewallPolicies.TestIamPermissions.
                See the method description for details.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compute.TestPermissionsResponse:

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/v1/projects/{project}/global/firewallPolicies/{resource}/testIamPermissions",
                    "body": "test_permissions_request_resource",
                },
            ]
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            request_kwargs = (
                compute.TestIamPermissionsNetworkFirewallPolicyRequest.to_dict(request)
            )
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            # Jsonify the request body
            body = compute.TestPermissionsRequest.to_json(
                compute.TestPermissionsRequest(transcoded_request["body"]),
                including_default_value_fields=False,
                use_integers_for_enums=False,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                compute.TestIamPermissionsNetworkFirewallPolicyRequest.to_json(
                    compute.TestIamPermissionsNetworkFirewallPolicyRequest(
                        transcoded_request["query_params"]
                    ),
                    including_default_value_fields=False,
                    use_integers_for_enums=False,
                )
            )

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compute.TestPermissionsResponse.from_json(
                response.content, ignore_unknown_fields=True
            )
            resp = self._interceptor.post_test_iam_permissions(resp)
            return resp

    @property
    def add_association(
        self,
    ) -> Callable[
        [compute.AddAssociationNetworkFirewallPolicyRequest], compute.Operation
    ]:
        stub = self._STUBS.get("add_association")
        if not stub:
            stub = self._STUBS["add_association"] = self._AddAssociation(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def add_rule(
        self,
    ) -> Callable[[compute.AddRuleNetworkFirewallPolicyRequest], compute.Operation]:
        stub = self._STUBS.get("add_rule")
        if not stub:
            stub = self._STUBS["add_rule"] = self._AddRule(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def clone_rules(
        self,
    ) -> Callable[[compute.CloneRulesNetworkFirewallPolicyRequest], compute.Operation]:
        stub = self._STUBS.get("clone_rules")
        if not stub:
            stub = self._STUBS["clone_rules"] = self._CloneRules(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def delete(
        self,
    ) -> Callable[[compute.DeleteNetworkFirewallPolicyRequest], compute.Operation]:
        stub = self._STUBS.get("delete")
        if not stub:
            stub = self._STUBS["delete"] = self._Delete(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def get(
        self,
    ) -> Callable[[compute.GetNetworkFirewallPolicyRequest], compute.FirewallPolicy]:
        stub = self._STUBS.get("get")
        if not stub:
            stub = self._STUBS["get"] = self._Get(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def get_association(
        self,
    ) -> Callable[
        [compute.GetAssociationNetworkFirewallPolicyRequest],
        compute.FirewallPolicyAssociation,
    ]:
        stub = self._STUBS.get("get_association")
        if not stub:
            stub = self._STUBS["get_association"] = self._GetAssociation(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[compute.GetIamPolicyNetworkFirewallPolicyRequest], compute.Policy]:
        stub = self._STUBS.get("get_iam_policy")
        if not stub:
            stub = self._STUBS["get_iam_policy"] = self._GetIamPolicy(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def get_rule(
        self,
    ) -> Callable[
        [compute.GetRuleNetworkFirewallPolicyRequest], compute.FirewallPolicyRule
    ]:
        stub = self._STUBS.get("get_rule")
        if not stub:
            stub = self._STUBS["get_rule"] = self._GetRule(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def insert(
        self,
    ) -> Callable[[compute.InsertNetworkFirewallPolicyRequest], compute.Operation]:
        stub = self._STUBS.get("insert")
        if not stub:
            stub = self._STUBS["insert"] = self._Insert(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def list(
        self,
    ) -> Callable[
        [compute.ListNetworkFirewallPoliciesRequest], compute.FirewallPolicyList
    ]:
        stub = self._STUBS.get("list")
        if not stub:
            stub = self._STUBS["list"] = self._List(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def patch(
        self,
    ) -> Callable[[compute.PatchNetworkFirewallPolicyRequest], compute.Operation]:
        stub = self._STUBS.get("patch")
        if not stub:
            stub = self._STUBS["patch"] = self._Patch(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def patch_rule(
        self,
    ) -> Callable[[compute.PatchRuleNetworkFirewallPolicyRequest], compute.Operation]:
        stub = self._STUBS.get("patch_rule")
        if not stub:
            stub = self._STUBS["patch_rule"] = self._PatchRule(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def remove_association(
        self,
    ) -> Callable[
        [compute.RemoveAssociationNetworkFirewallPolicyRequest], compute.Operation
    ]:
        stub = self._STUBS.get("remove_association")
        if not stub:
            stub = self._STUBS["remove_association"] = self._RemoveAssociation(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def remove_rule(
        self,
    ) -> Callable[[compute.RemoveRuleNetworkFirewallPolicyRequest], compute.Operation]:
        stub = self._STUBS.get("remove_rule")
        if not stub:
            stub = self._STUBS["remove_rule"] = self._RemoveRule(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[compute.SetIamPolicyNetworkFirewallPolicyRequest], compute.Policy]:
        stub = self._STUBS.get("set_iam_policy")
        if not stub:
            stub = self._STUBS["set_iam_policy"] = self._SetIamPolicy(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [compute.TestIamPermissionsNetworkFirewallPolicyRequest],
        compute.TestPermissionsResponse,
    ]:
        stub = self._STUBS.get("test_iam_permissions")
        if not stub:
            stub = self._STUBS["test_iam_permissions"] = self._TestIamPermissions(
                self._session, self._host, self._interceptor
            )

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub  # type: ignore

    def close(self):
        self._session.close()


__all__ = ("NetworkFirewallPoliciesRestTransport",)