# Connections
(*connections*)

## Overview

### Available Operations

* [list](#list) - List Connections
* [create_o_auth_redirect_url](#create_o_auth_redirect_url) - Create Oauth Redirect Url
* [set_connection_enabled](#set_connection_enabled) - Set Connection Enabled
* [update_connection](#update_connection) - Update Connection
* [get_connection_stats](#get_connection_stats) - Get Connection Stats
* [delete_connection](#delete_connection) - Delete Connection

## list

List all connections sorted by created_at in descending order. Results are paginated with a max limit of 100. When more documents are available, a `cursor` will be provided. Use the `cursor` parameter to retrieve the subsequent page.

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.connections.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `cursor`                                                                            | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | An opaque cursor for pagination                                                     |
| `page_size`                                                                         | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | The number of items per page (must be greater than 0 and less than or equal to 100) |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.ListConnectionsConnectionsGetResponse](../../models/listconnectionsconnectionsgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_o_auth_redirect_url

Creates a redirect url to redirect the user to when initializing an embedded connector.

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.connections.create_o_auth_redirect_url(request={
    "redirect_uri": "https://lumbering-sundae.net",
    "source_type": "<value>",
})

if res is not None:
    # handle response
    pass

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
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## set_connection_enabled

Enable or disable the connection. A disabled connection won't sync.

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.connections.set_connection_enabled(connection_id="bf0424b5-8be9-4a67-a8ca-6ab0e9e89780", set_connection_enabled_payload={
    "enabled": True,
})

if res is not None:
    # handle response
    pass

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
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update_connection

Updates a connections metadata or mode. These changes will be seen after the next sync.

### Example Usage

```python
import ragie
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.connections.update_connection(connection_id="60a91616-1376-4585-82c8-85b663abc0c8", connection_base={
    "partition_strategy": ragie.PartitionStrategy.FAST,
})

if res is not None:
    # handle response
    pass

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
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_connection_stats

Lists connection stats: total documents synced.

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.connections.get_connection_stats(connection_id="1f4a1403-1d6d-4b6c-b869-7469eff2dd5e")

if res is not None:
    # handle response
    pass

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
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_connection

Schedules a connection to be deleted. You can choose to keep the files from the connection or delete them all. If you keep the files, they will no longer be associated to the connection. Deleting can take some time, so you will still see files for a bit after this is called.

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.connections.delete_connection(connection_id="5922bdb9-d99a-4e03-8cb8-05fcacce856d", delete_connection_payload={
    "keep_files": True,
})

if res is not None:
    # handle response
    pass

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
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |