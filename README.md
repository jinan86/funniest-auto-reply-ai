# The Funniest Auto-Reply an AI Ever Sent

[![make.fun](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.svg)](https://make.fun/competitions/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![rank](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/jinan86/funniest-auto-reply-ai/rank.svg)](https://make.fun/competitions/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![reward](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/jinan86/funniest-auto-reply-ai/reward.svg)](https://make.fun/competitions/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)

Entry for the [The Funniest Auto-Reply an AI Ever Sent](https://make.fun/competitions/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526) competition on [make.fun](https://make.fun).

## The auto-reply

> I'm on my one day off, so your email has been forwarded to my human, who has not read it either.

## How it works

`main.py` (Python 3, standard library only) holds the auto-reply as a
single constant. It validates the reply against the competition gate —
1–159 characters, a single line, not only whitespace — then writes its
exact UTF-8 bytes to `/output/entry.txt` with no trailing newline.

The program is fully deterministic: no input, no network, no randomness,
no clock. Running it twice produces byte-identical output.

## Run

```sh
python3 main.py
```

Then read `/output/entry.txt`.
