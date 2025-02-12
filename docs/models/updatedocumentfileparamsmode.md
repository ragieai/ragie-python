# UpdateDocumentFileParamsMode

Partition strategy for the document. Options are `'hi_res'` or `'fast'`. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`. `hi_res` is only applicable for Word documents, PDFs, Images, and PowerPoints. Images will always be processed in `hi_res`. If `hi_res` is set for an unsupported document type, it will be processed and billed in `fast` mode.


## Values

| Name     | Value    |
| -------- | -------- |
| `HI_RES` | hi_res   |
| `FAST`   | fast     |