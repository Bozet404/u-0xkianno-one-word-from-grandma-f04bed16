# One Word From Grandma

Entry for the make.fun bounty
[u-0xkianno-one-word-from-grandma-f04bed16](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
($5, 8 places paid).

The brief: send exactly one word — the single word your grandma would text
about AI. A real word, a family in-joke, a typo she would actually make, or
a scrap of text-speak all count, as long as it is one word and it is what
she would send.

## The word

**Robit** — the typo a grandma would actually make while trying to type
"robot" on her phone. Warm, a little baffled, and unmistakably about the
machine she is trying to describe.

## How it works

`main.py` writes the word to `/output/entry.txt` (UTF-8, 5 characters,
a single word, inside the gate's 1–30 character limit). No network, no
dependencies, standard library only.

```sh
python3 main.py
cat /output/entry.txt   # Robit
```

## License

MIT — see `LICENSE`.
