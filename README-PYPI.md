# ragie

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=<no value>&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasy.com/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasy.com/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+<UNSET>.git
```

Poetry
```bash
poetry add git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break

```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from ragie import Ragie

async def main():
    s = Ragie(
        auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.documents.list_async(request={
        "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
    })
    if res is not None:
        while True:
            # handle items
    
            res = res.Next()
            if res is None:
                break

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [documents](docs/sdks/documents/README.md)

* [list](docs/sdks/documents/README.md#list) - List Documents
* [create](docs/sdks/documents/README.md#create) - Create Document
* [create_raw](docs/sdks/documents/README.md#create_raw) - Create Document Raw
* [create_document_from_url](docs/sdks/documents/README.md#create_document_from_url) - Create Document From Url
* [get](docs/sdks/documents/README.md#get) - Get Document
* [delete](docs/sdks/documents/README.md#delete) - Delete Document
* [update_file](docs/sdks/documents/README.md#update_file) - Update Document File
* [update_raw](docs/sdks/documents/README.md#update_raw) - Update Document Raw
* [patch_metadata](docs/sdks/documents/README.md#patch_metadata) - Patch Document Metadata
* [get_summary](docs/sdks/documents/README.md#get_summary) - Get Document Summary

### [retrievals](docs/sdks/retrievals/README.md)

* [retrieve](docs/sdks/retrievals/README.md#retrieve) - Retrieve

### [entities](docs/sdks/entities/README.md)

* [list_instructions](docs/sdks/entities/README.md#list_instructions) - List Instructions
* [create_instruction](docs/sdks/entities/README.md#create_instruction) - Create Instruction
* [update_instruction](docs/sdks/entities/README.md#update_instruction) - Update Instruction
* [list_by_instruction](docs/sdks/entities/README.md#list_by_instruction) - Get Instruction Extracted Entities
* [list_by_document](docs/sdks/entities/README.md#list_by_document) - Get Document Extracted Entities
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


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

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.create(request={
    "file": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
})

if res is not None:
    # handle response
    pass

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from ragie import Ragie
from ragie.utils import BackoffStrategy, RetryConfig

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from ragie import Ragie
from ragie.utils import BackoffStrategy, RetryConfig

s = Ragie(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401,404                    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

### Example

```python
from ragie import Ragie, models

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
})

except models.ErrorMessage as e:
    # handle exception
    raise(e)
except models.HTTPValidationError as e:
    # handle exception
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.ragie.ai` | None |

#### Example

```python
from ragie import Ragie

s = Ragie(
    server_idx=0,
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from ragie import Ragie

s = Ragie(
    server_url="https://api.ragie.ai",
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


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

| Name        | Type        | Scheme      |
| ----------- | ----------- | ----------- |
| `auth`      | http        | HTTP Bearer |

To authenticate with the API the `auth` parameter must be set when initializing the SDK client instance. For example:
```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

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
