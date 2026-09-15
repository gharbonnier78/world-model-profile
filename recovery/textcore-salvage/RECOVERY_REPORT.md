# Text-core recovery report

Recovered non-destructively from the truncated staged ZIP on `rebuild/world-model-complete` using `zip -FF`.

Known damaged entries intentionally excluded from the persisted salvage:

- `archive/REPOSITORY_IMPORT_SHA256SUMS.txt` — invalid compressed data during salvage.
- `framework/accepted-v0.4/11_independent_check.py` — invalid compressed data / empty extraction.
- a duplicate `TEXT_CORE_SHA256SUMS.txt` entry — bad CRC; only the first non-empty recovered copy is retained.

The original `.import` and `.recovery` transport material is intentionally preserved.
