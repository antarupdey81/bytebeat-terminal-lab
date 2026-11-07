# Curated Bytebeat Formulas (8000 Hz)

1. The Lost Machine:
   (t*(t>>12|t>>8)&63&t>>4)

2. Space Invaders Counterpoint:
   (t>>6|t|t>>(t>>16))*10+((t>>11)&7)

3. Harmonic Sierpinski:
   ((t*(t>>9|t>>13))&46)&t>>8

4. Stereo Dual-Phase:
   Left:  (t*5&t>>7)|(t*3&t>>10)
   Right: (t*5&t>>7)|(t*11&t>>11)