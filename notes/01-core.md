# Parse repeated query parameters: implementation

## What the example does

parse_qs returns lists even for a single value. keep_blank_values retains empty parameters; field count is bounded to reject oversized input.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"tag=a&tag=b&q=hello+world"
```

Expected result:

```json
{
  "tag": [
    "a",
    "b"
  ],
  "q": [
    "hello world"
  ]
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
