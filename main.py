import sys
from test import run_benchmark, run_table

import javabot.java_wrapper as java_wrapper
import my_bot
from example_bots.python import (
    good_bot,
    hardcore_ai_bot,
    never_bluff_bot,
    old_bot,
    old_old_bot,
    old_old_bot2,
    random_bot,
)

bots = [
    random_bot,
    never_bluff_bot,
    old_bot,
    hardcore_ai_bot,
    old_old_bot,
    old_old_bot2,
]

lang, type = sys.argv[1], sys.argv[2]

if lang == "java":
    bots.append(java_wrapper)
else:
    bots.append(my_bot)

if type == "benchmark":
    run_benchmark(bots, int(sys.argv[3]))
else:
    run_table(bots)
