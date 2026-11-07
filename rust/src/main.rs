use std::io::{self, Write};

fn main() -> io::Result<()> {
    let stdout = io::stdout();
    let mut handle = stdout.lock();
    let mut t: u32 = 0;
    let mut buffer = [0u8; 4096];

    loop {
        for byte in buffer.iter_mut() {
            let sample = ((t >> 7 | t | t >> 6).wrapping_mul(10)
                + 4 * (t & (t >> 13) | (t >> 6))) & 0xFF;
            *byte = sample as u8;
            t = t.wrapping_add(1);
        }

        if handle.write_all(&buffer).is_err() {
            break;
        }
    }
    Ok(())
}