# Benchmark Results

> python utils/e2e_benchmark.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf -n 200 -p 256 -t 24

| model                                   |       size |     params | backend    | threads | n_batch |          test |                  t/s |
| --------------------------------------- | ---------: | ---------: | ---------- | ------: | ------: | ------------: | -------------------: |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      24 |       1 |         pp256 |         26.37 ± 1.03 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      24 |       1 |         tg200 |         26.92 ± 0.62 |

***
> python utils/e2e_benchmark.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf -n 2000 -p 2560 -t 24

| model                                   |       size |     params | backend    | threads | n_batch |          test |                  t/s |
| --------------------------------------- | ---------: | ---------: | ---------- | ------: | ------: | ------------: | -------------------: |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      24 |       1 |        pp2560 |         23.55 ± 0.14 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      24 |       1 |        tg2000 |         24.75 ± 0.20 |
