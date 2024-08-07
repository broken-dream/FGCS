# FGCS
repo for paper 《FGCS: A Fine-grained Scientific Information Extraction Dataset in Computer Science》
## Data format
Each line represents a instance and is organized in the following format:

```
{
  "tokens": ["We", "start", "from", "analyzing", "the", "procedures", ...],
  "ners": [
    [16, 16, "Metric"], 
    [13, 13, 16, 16, "Metric"],
    ...
  ],
  "relations": [
    [0, 1, "Hyponym-of"],
    ...
  ],
  "discontinuous": true
}
```

Entries in `ners` are organized as `[token_start, token_end, type]` for general entities and `[first_span_start, first_span_end, second_span_start, second_span_end, type]` for discontinuous entities.

Entries in `relations` are organized as `[head_entity_index, tail_entity_index, type]`.

`discontinuous` indicated whether there is a discontinuous entity in this sentence.
## Convert to PURE format
[PURE](https://github.com/princeton-nlp/PURE) is a simple but effective entity and relation extraction method. You can run `scripts/pure.py` to convert the data to the PURE format:

```
python scripts/pure.py --input_file={input_file_path} --output_file={output_file_path}
```