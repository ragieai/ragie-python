<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from ragie import Ragie

with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as ragie:

    res = ragie.documents.create(request={
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
    ) as ragie:

        res = await ragie.documents.create_async(request={
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
<!-- End SDK Example Usage [usage] -->