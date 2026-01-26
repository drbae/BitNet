# Benchmark Results

| model                                |     size |  params | backend | threads | n_batch |    test |           t/s |
| -------------------------------------| -------: | ------: | ------- | ------: | ------: | ------: | ------------: |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |      24 |       1 |  pp2560 |  23.55 ± 0.14 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |      24 |       1 |  tg2000 |  24.75 ± 0.20 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |      24 |       1 |   pp256 |  26.37 ± 1.03 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |      24 |       1 |   tg200 |  26.92 ± 0.62 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |      12 |       1 |   pp256 |  29.53 ± 0.42 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |      12 |       1 |   tg200 |  29.95 ± 0.43 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |       6 |       1 |   pp256 |  30.73 ± 0.21 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |       6 |       1 |   tg200 |  30.87 ± 0.21 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |       4 |       1 |   pp256 |  27.42 ± 0.19 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |       4 |       1 |   tg200 |  27.02 ± 0.47 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |      12 |       1 |   pp256 |  30.50 ± 0.22 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |      12 |       1 |   tg200 |  30.16 ± 0.95 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |       6 |       1 |   pp256 |  30.48 ± 0.09 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |       6 |       1 |   tg200 |  30.56 ± 0.19 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |       4 |       1 |   pp256 |  30.46 ± 0.12 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary | 1.71 GiB |  2.74 B | CPU     |       4 |       1 |   tg200 |  29.74 ± 1.46 |

***
변환: bf16 > gguf

| model                                |     size |  params | backend | threads | n_batch |    test |           t/s |
| ------------------------------------ | -------: | ------: | ------- | ------: | ------: | ------: | ------------: |
| bitnet-25 2B I2_S - 2 bpw ternary    | 1.71 GiB |  2.74 B | CPU     |       4 |       1 |   pp256 |  24.72 ± 2.81 |
| bitnet-25 2B I2_S - 2 bpw ternary    | 1.71 GiB |  2.74 B | CPU     |       4 |       1 |   tg200 |  27.66 ± 0.26 |
| bitnet-25 2B I2_S - 2 bpw ternary    | 1.71 GiB |  2.74 B | CPU     |       6 |       1 |   pp256 |  29.30 ± 0.35 |
| bitnet-25 2B I2_S - 2 bpw ternary    | 1.71 GiB |  2.74 B | CPU     |       6 |       1 |   tg200 |  29.39 ± 0.37 |
| bitnet-25 2B I2_S - 2 bpw ternary    | 1.71 GiB |  2.74 B | CPU     |      12 |       1 |   pp256 |  28.99 ± 0.82 |
| bitnet-25 2B I2_S - 2 bpw ternary    | 1.71 GiB |  2.74 B | CPU     |      12 |       1 |   tg200 |  29.65 ± 0.14 |
| bitnet-25 2B I2_S - 2 bpw ternary    | 1.71 GiB |  2.74 B | CPU     |      24 |       1 |   pp256 |  26.72 ± 0.92 |
| bitnet-25 2B I2_S - 2 bpw ternary    | 1.71 GiB |  2.74 B | CPU     |      24 |       1 |   tg200 |  27.56 ± 0.50 |
