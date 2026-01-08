# ragie

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=<no value>&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [ragie](https://github.com/ragieai/ragie-python/blob/master/#ragie)
  * [SDK Installation](https://github.com/ragieai/ragie-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/ragieai/ragie-python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/ragieai/ragie-python/blob/master/#sdk-example-usage)
  * [Available Resources and Operations](https://github.com/ragieai/ragie-python/blob/master/#available-resources-and-operations)
  * [Pagination](https://github.com/ragieai/ragie-python/blob/master/#pagination)
  * [File uploads](https://github.com/ragieai/ragie-python/blob/master/#file-uploads)
  * [Retries](https://github.com/ragieai/ragie-python/blob/master/#retries)
  * [Error Handling](https://github.com/ragieai/ragie-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/ragieai/ragie-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/ragieai/ragie-python/blob/master/#custom-http-client)
  * [Authentication](https://github.com/ragieai/ragie-python/blob/master/#authentication)
  * [Resource Management](https://github.com/ragieai/ragie-python/blob/master/#resource-management)
  * [Debugging](https://github.com/ragieai/ragie-python/blob/master/#debugging)
* [Development](https://github.com/ragieai/ragie-python/blob/master/#development)
  * [Maturity](https://github.com/ragieai/ragie-python/blob/master/#maturity)
  * [Contributions](https://github.com/ragieai/ragie-python/blob/master/#contributions)
* [ragie-python](https://github.com/ragieai/ragie-python/blob/master/#ragie-python)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add ragie
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install ragie
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add ragie
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from ragie python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "ragie",
# ]
# ///

from ragie import Ragie

sdk = Ragie(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example 1

```python
# Synchronous Example
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.documents.create(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from ragie import Ragie

async def main():

    async with Ragie(
        auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as r_client:

        res = await r_client.documents.create_async(request={
            "file": {
                "file_name": "example.file",
                "content": open("example.file", "rb"),
            },
        })

        # Handle response
        print(res)

asyncio.run(main())
```

### Example 2

```python
# Synchronous Example
import ragie
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.create_connection(request=ragie.PublicCreateConnection(
        partition_strategy=ragie.MediaModeParam(),
        page_limit=None,
        config=None,
        connection=ragie.PublicGCSConnection(
            data=ragie.BucketData(
                bucket="<value>",
                import_file_metadata=False,
            ),
            credentials={
                "key": "<value>",
                "key1": "<value>",
            },
        ),
    ))

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import ragie
from ragie import Ragie

async def main():

    async with Ragie(
        auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as r_client:

        res = await r_client.connections.create_connection_async(request=ragie.PublicCreateConnection(
            partition_strategy=ragie.MediaModeParam(),
            page_limit=None,
            config=None,
            connection=ragie.PublicGCSConnection(
                data=ragie.BucketData(
                    bucket="<value>",
                    import_file_metadata=False,
                ),
                credentials={
                    "key": "<value>",
                    "key1": "<value>",
                },
            ),
        ))

        # Handle response
        print(res)

asyncio.run(main())
```

### Example 3

```python
# Synchronous Example
import ragie
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.authenticators.create(request={
        "provider": ragie.Provider.ATLASSIAN,
        "name": "<value>",
        "client_id": "<id>",
        "client_secret": "<value>",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import ragie
from ragie import Ragie

async def main():

    async with Ragie(
        auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as r_client:

        res = await r_client.authenticators.create_async(request={
            "provider": ragie.Provider.ATLASSIAN,
            "name": "<value>",
            "client_id": "<id>",
            "client_secret": "<value>",
        })

        # Handle response
        print(res)

asyncio.run(main())
```

### Example 4

```python
# Synchronous Example
import ragie
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.authenticators.create_authenticator_connection(authenticator_id="84b0792c-1330-4854-b4f2-5d9c7bf9a385", create_authenticator_connection=ragie.CreateAuthenticatorConnection(
        partition_strategy=ragie.MediaModeParam(),
        page_limit=None,
        config=None,
        connection=ragie.AuthenticatorDropboxConnection(
            data=ragie.FolderData(
                folder_id="<id>",
                folder_name="<value>",
            ),
            email="Aliyah_Feest59@yahoo.com",
            credentials=ragie.OAuthRefreshTokenCredentials(
                refresh_token="<value>",
            ),
        ),
    ))

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import ragie
from ragie import Ragie

async def main():

    async with Ragie(
        auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as r_client:

        res = await r_client.authenticators.create_authenticator_connection_async(authenticator_id="84b0792c-1330-4854-b4f2-5d9c7bf9a385", create_authenticator_connection=ragie.CreateAuthenticatorConnection(
            partition_strategy=ragie.MediaModeParam(),
            page_limit=None,
            config=None,
            connection=ragie.AuthenticatorDropboxConnection(
                data=ragie.FolderData(
                    folder_id="<id>",
                    folder_name="<value>",
                ),
                email="Aliyah_Feest59@yahoo.com",
                credentials=ragie.OAuthRefreshTokenCredentials(
                    refresh_token="<value>",
                ),
            ),
        ))

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Authenticators](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/authenticators/README.md)

* [create](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/authenticators/README.md#create) - Create Authenticator
* [list](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/authenticators/README.md#list) - List Authenticators
* [create_authenticator_connection](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/authenticators/README.md#create_authenticator_connection) - Create Authenticator Connection
* [delete_authenticator_connection](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/authenticators/README.md#delete_authenticator_connection) - Delete Authenticator

### [Connections](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md)

* [create_connection](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#create_connection) - Create Connection
* [list](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#list) - List Connections
* [create_o_auth_redirect_url](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#create_o_auth_redirect_url) - Create Oauth Redirect Url
* [list_connection_source_types](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#list_connection_source_types) - List Connection Source Types
* [set_enabled](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#set_enabled) - Set Connection Enabled
* [update](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#update) - Update Connection
* [get](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#get) - Get Connection
* [get_stats](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#get_stats) - Get Connection Stats
* [set_limits](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#set_limits) - Set Connection Limits
* [delete](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#delete) - Delete Connection
* [sync](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/connections/README.md#sync) - Sync Connection

### [Documents](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md)

* [create](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#create) - Create Document
* [list](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#list) - List Documents
* [create_raw](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#create_raw) - Create Document Raw
* [create_document_from_url](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#create_document_from_url) - Create Document From Url
* [get](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#get) - Get Document
* [delete](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#delete) - Delete Document
* [update_file](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#update_file) - Update Document File
* [update_raw](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#update_raw) - Update Document Raw
* [update_document_from_url](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#update_document_from_url) - Update Document Url
* [patch_metadata](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#patch_metadata) - Patch Document Metadata
* [get_chunks](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#get_chunks) - Get Document Chunks
* [get_chunk](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#get_chunk) - Get Document Chunk
* [get_chunk_content](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#get_chunk_content) - Get Document Chunk Content
* [get_content](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#get_content) - Get Document Content
* [get_source](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#get_source) - Get Document Source
* [get_summary](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/documents/README.md#get_summary) - Get Document Summary

### [Entities](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/entities/README.md)

* [list_instructions](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/entities/README.md#list_instructions) - List Instructions
* [create_instruction](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/entities/README.md#create_instruction) - Create Instruction
* [update_instruction](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/entities/README.md#update_instruction) - Update Instruction
* [delete](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/entities/README.md#delete) - Delete Instruction
* [list_by_instruction](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/entities/README.md#list_by_instruction) - Get Instruction Extracted Entities
* [list_by_document](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/entities/README.md#list_by_document) - Get Document Extracted Entities

### [Partitions](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/partitions/README.md)

* [list](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/partitions/README.md#list) - List Partitions
* [create](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/partitions/README.md#create) - Create Partition
* [get](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/partitions/README.md#get) - Get Partition
* [update](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/partitions/README.md#update) - Update Partition
* [delete](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/partitions/README.md#delete) - Delete Partition
* [set_limits](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/partitions/README.md#set_limits) - Set Partition Limits

### [Responses](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/responses/README.md)

* [create](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/responses/README.md#create) - Create Response
* [get](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/responses/README.md#get) - Get Response

### [Retrievals](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/retrievals/README.md)

* [retrieve](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/retrievals/README.md#retrieve) - Retrieve

### [WebhookEndpoints](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/webhookendpoints/README.md)

* [list](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/webhookendpoints/README.md#list) - List Webhook Endpoints
* [create](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/webhookendpoints/README.md#create) - Create Webhook Endpoint
* [get](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/webhookendpoints/README.md#get) - Get Webhook Endpoint
* [update](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/webhookendpoints/README.md#update) - Update Webhook Endpoint
* [delete](https://github.com/ragieai/ragie-python/blob/master/docs/sdks/webhookendpoints/README.md#delete) - Delete Webhook Endpoint

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.documents.list(request={
        "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
        "partition": "acme_customer_id",
    })

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.documents.create(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from ragie import Ragie
from ragie.utils import BackoffStrategy, RetryConfig


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.documents.create(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from ragie import Ragie
from ragie.utils import BackoffStrategy, RetryConfig


with Ragie(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.documents.create(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`RagieError`](https://github.com/ragieai/ragie-python/blob/master/./src/ragie/models/ragieerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/ragieai/ragie-python/blob/master/#error-classes). |

### Example
```python
import ragie
from ragie import Ragie, models


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:
    res = None
    try:

        res = r_client.documents.create(request={
            "file": {
                "file_name": "example.file",
                "content": open("example.file", "rb"),
            },
        })

        # Handle response
        print(res)


    except models.RagieError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.HTTPValidationError):
            print(e.data.detail)  # Optional[List[ragie.ValidationError]]
```

### Error Classes
**Primary errors:**
* [`RagieError`](https://github.com/ragieai/ragie-python/blob/master/./src/ragie/models/ragieerror.py): The base class for HTTP error responses.
  * [`ErrorMessage`](https://github.com/ragieai/ragie-python/blob/master/./src/ragie/models/errormessage.py): Unauthorized.
  * [`HTTPValidationError`](https://github.com/ragieai/ragie-python/blob/master/./src/ragie/models/httpvalidationerror.py): Validation Error. Status code `422`. *

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`RagieError`](https://github.com/ragieai/ragie-python/blob/master/./src/ragie/models/ragieerror.py)**:
* [`ResponseValidationError`](https://github.com/ragieai/ragie-python/blob/master/./src/ragie/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/ragieai/ragie-python/blob/master/#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from ragie import Ragie


with Ragie(
    server_url="https://api.ragie.ai",
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.documents.create(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from ragie import Ragie
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Ragie(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from ragie import Ragie
from ragie.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Ragie(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name   | Type | Scheme      |
| ------ | ---- | ----------- |
| `auth` | http | HTTP Bearer |

To authenticate with the API the `auth` parameter must be set when initializing the SDK client instance. For example:
```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.documents.create(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Ragie` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from ragie import Ragie
def main():

    with Ragie(
        auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as r_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Ragie(
        auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as r_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from ragie import Ragie
import logging

logging.basicConfig(level=logging.DEBUG)
s = Ragie(debug_logger=logging.getLogger("ragie"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation.
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release.

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=<no value>&utm_campaign=python)

# ragie-python
