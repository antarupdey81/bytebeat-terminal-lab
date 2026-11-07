# Bytebeat-terminal-lab

A minimal, high-performance experimental laboratory for mathematical sound synthesis, 8000 Hz 1-line algorithmic songs, stereo PCM pipelines, and terminal-based digital signal processing.

## What is Bytebeat?

Invented by Ville-Matias Heikkilä (viznut) in 2011, Bytebeat generates complex musical compositions from simple mathematical formulas evaluated at an incremental time variable $t$ (where $t$ represents sequential audio sample indices running at 8000 Hz or 44100 Hz).

## Quickstart

### 1. Pure C (Linux / Termux / macOS)
```bash
cd c
make
# Pipe raw 8-bit PCM samples directly to aplay or sox
./classic | aplay -r 8000
./stereo | aplay -c 2 -f U8 -r 8000