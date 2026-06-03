# QueryParamStatus

Optional extraction status filter. Supported values are `extracted`, `not_found`, and `error`.

## Example Usage

```python
from ragie.models import QueryParamStatus

value = QueryParamStatus.EXTRACTED
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `EXTRACTED` | extracted   |
| `NOT_FOUND` | not_found   |
| `ERROR`     | error       |