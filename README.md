# Merge Sort API

A stable merge sort implementation exposed through a small FastAPI service, with a standalone Mintlify documentation site.

## Run the API

```bash
uv sync
uv run uvicorn merge_sort_service.api:app --reload
```

The API is available at `http://localhost:8000`. Try it with:

```bash
curl -X POST http://localhost:8000/sort \
  -H 'Content-Type: application/json' \
  -d '{"values":[8,3,5,1,4]}'
```

## Run the docs

Install the [Mintlify CLI](https://www.npmjs.com/package/mint) once, then run:

```bash
cd docs
mint dev
```

The docs site opens at `http://localhost:3000`.
