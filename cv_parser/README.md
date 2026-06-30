Quarto CV generator for the parent Jekyll site.

```sh
UV_CACHE_DIR=.uv-cache uv run python main.py
```

The command reads `../index.md` and `../_data/research.yml`, writes
`build/cv.qmd` and `build/references.bib`, then renders `build/cv.pdf` with
Quarto. Use `--no-render` to only generate the source files.
