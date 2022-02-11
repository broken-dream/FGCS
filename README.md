# FGCS
repo for paper 《FGCS: A Fine-grained Scientific Information Extraction Dataset in Computer Science》
## Data format
Each line represents a instance and is organized in the following format:

```
{
  "tokens": [],
  "ners": [
    [0, 1, "Task"],
    [0, 1, 3, 4, "Method"],
    ...
  ],
  "relations": [
    [1, 0, "Used-for"],
  ],
  "discontinuous": true
}
```

Entries in `ners` are organized as `[token_start, token_end, type]` for general entities and `[first_span_start, first_span_end, second_span_start, second_span_end, type]` for discontinuous entities.

Entries in `relations` are organized as `[head_entity_index, tail_entity_index, type]`.

`discontinuous` indicated whether there is a discontinuous entity in this sentence.
