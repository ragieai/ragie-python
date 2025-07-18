# Authenticators
(*authenticators*)

## Overview

### Available Operations

* [create](#create) - Create Authenticator
* [list](#list) - List Authenticators
* [create_authenticator_connection](#create_authenticator_connection) - Create Authenticator Connection
* [delete_authenticator_connection](#delete_authenticator_connection) - Delete Authenticator

## create

Create White labeled connector credentials

### Example Usage

```python
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

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.CreateAuthenticatorPayload](../../models/createauthenticatorpayload.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.BaseGetAuthenticator](../../models/basegetauthenticator.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 400, 401, 402, 429         | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list

List all authenticators sorted by created_at in descending order. Results are paginated with a max limit of 100. When more authenticators are available, a `cursor` will be provided. Use the `cursor` parameter to retrieve the subsequent page.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.authenticators.list(request={})

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.ListAuthenticatorsRequest](../../models/listauthenticatorsrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ListAuthenticatorsResponse](../../models/listauthenticatorsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 400, 401, 402, 429         | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_authenticator_connection

Create a connector for a given authenticator. This requires credentials dependent on the provider. For google drive it is a refresh token.

### Example Usage

```python
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

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `authenticator_id`                                                                    | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `create_authenticator_connection`                                                     | [models.CreateAuthenticatorConnection](../../models/createauthenticatorconnection.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.Connection](../../models/connection.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 400, 401, 402, 429         | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_authenticator_connection

Delete an authenticator. This requires all connections created by that authenticator to be deleted first.

### Example Usage

```python
from ragie import Ragie


with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as r_client:

    res = r_client.authenticators.delete_authenticator_connection(authenticator_id="6737a874-c5c2-4d13-8234-8119b200a2b0")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `authenticator_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ResponseOK](../../models/responseok.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorMessage        | 400, 401, 402, 429         | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |