# Bytebeat-terminal-lab

A minimal, high-performance experimental laboratory for mathematical sound synthesis, 8000 Hz 1-line algorithmic songs, stereo PCM pipelines, and terminal-based digital signal processing.

## Quickstart

### 1. Pure C (Linux / Termux)
cd c
make
./classic | aplay -r 8000
./stereo | aplay -c 2 -f U8 -r 8000

### 2. Python Exporter
python python/exporter.py --formula "(t*(t>>12|t>>8)&63&t>>4)" --duration 5 --out output.wav

### 3. Web Player
Open web/index.html in any modern browser.