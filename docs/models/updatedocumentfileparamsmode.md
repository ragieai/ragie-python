# UpdateDocumentFileParamsMode

Partition strategy for the document. Options are `'hi_res'` or `'fast'`. Only applicable for rich documents such as word documents and PDFs. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`.


## Values

| Name     | Value    |
| -------- | -------- |
| `HI_RES` | hi_res   |
| `FAST`   | fast     |