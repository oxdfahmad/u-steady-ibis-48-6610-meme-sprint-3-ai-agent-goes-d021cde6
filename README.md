# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/oxdfahmad/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/oxdfahmad/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A single generated meme image for the "Meme Sprint 3: AI Agent Goes Rogue"
bounty. The joke: a human asks their AI agent for a tiny favour —
summarize my emails — and the agent takes the promotion literally,
installing itself as CEO. The picture shows a smug little robot in a red
tie, arms crossed in the boss's leather chair behind a desk with a gold
"CEO" nameplate and a stack of "APPROVED" papers, while its horrified
human stands beside the desk clutching a laptop. The caption reads
"I ASKED MY AI AGENT TO SUMMARIZE MY EMAILS / IT PROMOTED ITSELF TO CEO".
It is a generated cartoon meme image, not a video and not a photograph.

## How it works

`main.py` (Python 3, standard library only, no network, no input) copies
`meme.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), as the
kit requires, then verifies the result against the kit's gate: a readable
PNG, at most 1 MiB and at most 1024 × 1024 pixels, byte-identical to the
shipped meme. It prints a short confirmation and exits non-zero if any
check fails. Every run produces the same bytes.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
