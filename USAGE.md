<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.documents.create(request={
    "file": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res is not None:
    # handle response
    pass
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
    res = await s.documents.create_async(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->