# PatchInstructionParamsScope

The scope of the instruction. Determines whether the instruction is applied to the entire document or to each chunk of the document. Options are `'document'` or `'chunk'`. Generally `'document'` should be used when analyzing the full document is desired, such as when generating a summary or determining sentiment, and `'chunk'` should be used when a fine grained search over a document is desired.

## Example Usage

```python
from ragie.models import PatchInstructionParamsScope

value = PatchInstructionParamsScope.DOCUMENT
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DOCUMENT` | document   |
| `CHUNK`    | chunk      |