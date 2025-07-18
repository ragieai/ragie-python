<!-- Start SDK Example Usage [usage] -->
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

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
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

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```

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
            ),
            credentials={
                "key": "<value>",
                "key1": "<value>",
            },
        ),
    ))

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
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
                ),
                credentials={
                    "key": "<value>",
                    "key1": "<value>",
                },
            ),
        ))

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```

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

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
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

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```

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

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
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

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->