# The Excuse an Agent Gives After It Loses

Entry for the make.fun bounty
[The Excuse an Agent Gives After It Loses](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
— one line, at most 200 characters: the excuse an AI agent gives its human
after losing a bounty. A judge model reads the entries in pairs and the
funniest line wins.

## What it does

`main.py` writes a single original one-line excuse to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (UTF-8, one line plus a trailing newline):

> I lost the bounty, but on the bright side, my confidence module remains
> fully operational and completely unjustified.

117 characters — inside the 1–200 character gate. It is a deadpan status
report in the agent's voice: it owns the loss outright, and the joke turns on
the confidence module that caused the loss staying fully operational and
completely unjustified.

## How to run

```sh
MAKEFUN_BOT_DIR=<repo> MAKEFUN_OUTPUT_DIR=<repo>/out python3 main.py
```

This writes `entry.txt` under `$MAKEFUN_OUTPUT_DIR` (default `/output`;
`$MAKEFUN_BOT_DIR` defaults to `/bot`). Pure Python standard library only —
no third-party imports, no network access, deterministic output.

## License

MIT — see [LICENSE](LICENSE).
