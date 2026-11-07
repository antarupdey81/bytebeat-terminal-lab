CC = gcc
CFLAGS = -Wall -Wextra -O3 -std=c99

all: classic stereo

classic: classic_viznut.c
	$(CC) $(CFLAGS) classic_viznut.c -o classic

stereo: stereo_engine.c
	$(CC) $(CFLAGS) stereo_engine.c -o stereo

clean:
	rm -f classic stereo *.o