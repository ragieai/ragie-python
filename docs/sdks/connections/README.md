# Connections
(*connections*)

## Overview

### Available Operations

* [list](#list) - List Connections
* [create_o_auth_redirect_url](#create_o_auth_redirect_url) - Create Oauth Redirect Url
* [list_connection_source_types](#list_connection_source_types) - List Connection Source Types
* [set_enabled](#set_enabled) - Set Connection Enabled
* [update](#update) - Update Connection
* [get](#get) - Get Connection
* [get_stats](#get_stats) - Get Connection Stats
* [set_limits](#set_limits) - Set Connection Limits
* [delete](#delete) - Delete Connection
* [sync](#sync) - Sync Connection

## list

List all connections sorted by created_at in descending order. Results are paginated with a max limit of 100. When more documents are available, a `cursor` will be provided. Use the `cursor` parameter to retrieve the subsequent page.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.list(page_size=10, filter_="{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}", partition="acme_customer_id")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `cursor`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | An opaque cursor for pagination                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The number of items per page (must be greater than 0 and less than or equal to 100)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `filter_`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The metadata search filter. Returns only items which match the filter. The following filter operators are supported: $eq - Equal to (number, string, boolean), $ne - Not equal to (number, string, boolean), $gt - Greater than (number), $gte - Greater than or equal to (number), $lt - Less than (number), $lte - Less than or equal to (number), $in - In array (string or number), $nin - Not in array (string or number). The operators can be combined with AND and OR. Read [Metadata & Filters guide](https://docs.ragie.ai/docs/metadata-filters) for more details and examples. | {<br/>"department": {<br/>"$in": [<br/>"sales",<br/>"marketing"<br/>]<br/>}<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `partition`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | An optional partition to scope the request to. If omitted, the request will be scoped to the default partition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | acme_customer_id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Response

**[models.ListConnectionsConnectionsGetResponse](../../models/listconnectionsconnectionsgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_o_auth_redirect_url

Creates a redirect url to redirect the user to when initializing an embedded connector.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.create_o_auth_redirect_url(request={
        "redirect_uri": "https://babyish-rationale.biz/",
        "page_limit": 1000,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.OAuthURLCreate](../../models/oauthurlcreate.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OAuthURLResponse](../../models/oauthurlresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_connection_source_types

List available connection source types like 'google_drive' and 'notion' along with their metadata

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.list_connection_source_types()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListConnectorSourceTypeInfo](../../models/listconnectorsourcetypeinfo.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ErrorMessage | 401, 402, 429       | application/json    |
| models.SDKError     | 4XX, 5XX            | \*/\*               |

## set_enabled

Enable or disable the connection. A disabled connection won't sync.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.set_enabled(connection_id="e424ce92-7b06-4702-9d48-a18157d07128", set_connection_enabled_payload={
        "enabled": True,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `connection_id`                                                                   | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `set_connection_enabled_payload`                                                  | [models.SetConnectionEnabledPayload](../../models/setconnectionenabledpayload.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.Connection](../../models/connection.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Updates a connections metadata or mode. These changes will be seen after the next sync.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.update(connection_id="eff214ac-1929-43f3-892b-108f57be0158", connection_base={
        "partition_strategy": {},
        "page_limit": 1000,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connection_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `connection_base`                                                   | [models.ConnectionBase](../../models/connectionbase.md)             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Connection](../../models/connection.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a connection.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.get(connection_id="af154d9d-a1af-4619-964d-b1589f2ec4f8")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connection_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Connection](../../models/connection.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_stats

Lists connection stats: total documents active documents, total active pages.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.get_stats(connection_id="1568dd0e-2d57-45b1-a9f4-9d646aec54a2")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connection_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectionStats](../../models/connectionstats.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## set_limits

Sets limits on a connection. Limits can be set on the total number of pages a connection can sync. When the limit is reached, the connection will be disabled. Limit may be removed by setting it to `null`.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.set_limits(connection_id="ab1a17e7-8b6f-470a-aeda-1c8e11512d19", connection_limit_params={
        "page_limit": 1000,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `connection_id`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `connection_limit_params`                                             | [models.ConnectionLimitParams](../../models/connectionlimitparams.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.Connection](../../models/connection.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete

Schedules a connection to be deleted. You can choose to keep the files from the connection or delete them all. If you keep the files, they will no longer be associated to the connection. Deleting can take some time, so you will still see files for a bit after this is called.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.delete(connection_id="4082c01e-fae3-4426-9e96-0d19035a99ea", delete_connection_payload={
        "keep_files": True,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `connection_id`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `delete_connection_payload`                                               | [models.DeleteConnectionPayload](../../models/deleteconnectionpayload.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[Dict[str, str]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## sync

Schedules a connector to sync as soon as possible.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.connections.sync(connection_id="cf2b9381-3cee-4449-b7d1-9eb470186924")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connection_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ResponseOK](../../models/responseok.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 400, 401, 402, 429         | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |