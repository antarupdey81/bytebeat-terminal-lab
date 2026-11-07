import argparse
import wave

def export_wav(formula_str, duration=5.0, sample_rate=8000, out_filename="output.wav"):
    total_samples = int(sample_rate * duration)
    with wave.open(out_filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(1)
        wav_file.setframerate(sample_rate)
        
        frames = bytearray()
        for t in range(total_samples):
            val = eval(formula_str, {"__builtins__": {}}, {"t": t}) & 0xFF
            frames.append(val)
        wav_file.writeframes(frames)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--formula", type=str, default="(t*(t>>12|t>>8)&63&t>>4)")
    parser.add_argument("--duration", type=float, default=5.0)
    parser.add_argument("--rate", type=int, default=8000)
    parser.add_argument("--out", type=str, default="output.wav")
    args = parser.parse_args()
    export_wav(args.formula, args.duration, args.rate, args.out)