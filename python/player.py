import sys

def evaluate_bytebeat(formula_str, sample_rate=8000, duration_seconds=10):
    total_samples = sample_rate * duration_seconds
    for t in range(total_samples):
        try:
            sample = eval(formula_str, {"__builtins__": {}}, {"t": t}) & 0xFF
            sys.stdout.buffer.write(bytes([sample]))
        except Exception:
            break

if __name__ == "__main__":
    formula = "(t >> 6 | t | t >> (t >> 16)) * 10 + ((t >> 11) & 7)"
    if len(sys.argv) > 1:
        formula = sys.argv[1]
    evaluate_bytebeat(formula)